/*
 * This file is part of the motility source distribution.
 *
 * motility is part of the Cartwheel bioinformatics toolkit:
 *
 *                  http://cartwheel.caltech.edu/
 *
 * Contact author: C. Titus Brown, titus@caltech.edu.
 *
 * This program and all associated source code files are Copyright (C)
 * 2003-2007 the California Institute of Technology, Pasadena, CA,
 * 91125 USA.  It is under the Lesser GNU Public License; please see
 * the included LICENSE.txt file for more information, or contact
 * Titus directly.
 *
 */ 

//
// A module for Python that wraps the motility C++ functions.
//

#include "Python.h"

#include <DnaSequence.hh>	// from motility src/
#include <LiteralMotif.hh>
#include <IupacMotif.hh>
#include <EnergyOperator.hh>

// Provides pre-Python 2.5 compatibility
#if PY_VERSION_HEX < 0x02050000 && !defined(PY_SSIZE_T_MIN)
  typedef int Py_ssize_t;
  #define PY_SSIZE_T_MAX INT_MAX
  #define PY_SSIZE_T_MIN INT_MIN
  typedef Py_ssize_t (*lenfunc)(PyObject *);
#endif

//
// Function necessary for Python loading:
//

extern "C" {
  void init_motility();
}

// exception to raise
static PyObject *MotilityError;

/***********************************************************************/

//
// Matrix object
//

typedef struct {
  PyObject_HEAD
  double *matrix;		// double [len][5]
  unsigned int length;
} motility_MatrixObject;

static void motility_matrix_dealloc(PyObject *);
      
static PyMethodDef motility_matrix_methods[] = {
  //  {"test", (PyCFunction) motility_test, METH_VARARGS, "howdy"},
  {NULL, NULL, 0, NULL}           /* sentinel */
};

static PyObject *
motility_matrix_getattr(PyObject * obj, char * name)
{
  return Py_FindMethod(motility_matrix_methods, obj, name);
}

#define is_matrix_obj(v)  ((v)->ob_type == &motility_MatrixType)

static Py_ssize_t matrix_length(motility_MatrixObject * self)
{
  return (Py_ssize_t) self->length;
}

static PyObject * _convert_results_to_tuple(motility::MotifMatchList& matches) {
  std::vector<motility::MotifMatch *> l = matches.list();

  PyObject * t = PyTuple_New(l.size());

  try {
    for (unsigned int i = 0; i < l.size(); i++) {
      motility::MotifMatch * m = l[i];

      int orientation = m->start > m->end ? -1 : 1;
      unsigned int start = orientation < 0 ? m->end : m->start;
      unsigned int end = orientation < 0 ? m->start : m->end;
      motility::DnaSequence match_seq;
    
      if (orientation == 1) { match_seq = m->match_seq; }
      else { match_seq = m->match_seq.reverse_complement(); }

      PyObject * u = Py_BuildValue("iiis", start, end, orientation,
				   match_seq.sequence().c_str());
      PyTuple_SET_ITEM(t, i, u);
    }
    return t;
  }
  catch (...) {
    Py_DECREF(t);		// prevent memory leak in case of exception

    throw;
  }

}

static PySequenceMethods tuple_as_sequence = {
  (lenfunc)matrix_length,	/* sq_length */
  0,				/* sq_concat */
  0,				/* sq_repeat */
  0,				/* sq_item */
  0,				/* sq_slice */
  0,				/* sq_ass_item */
  0,				/* sq_ass_slice */
  0,				/* sq_contains */
};

static PyTypeObject motility_MatrixType = {
    PyObject_HEAD_INIT(NULL)
    0,
    "Matrix", sizeof(motility_MatrixObject),
    0,
    motility_matrix_dealloc,	/*tp_dealloc*/
    0,				/*tp_print*/
    motility_matrix_getattr,	/*tp_getattr*/
    0,				/*tp_setattr*/
    0,				/*tp_compare*/
    0,				/*tp_repr*/
    0,				/*tp_as_number*/
    &tuple_as_sequence,		/*tp_as_sequence*/
    0,				/*tp_as_mapping*/
    0,				/*tp_hash */
};

//
// _parse_matrix -- take a list of lists of doubles (double [][5]) in
// Python format and convert it into a motility_MatrixObject.  See
// create_matrix for direct Python access.
//

static motility_MatrixObject * _parse_matrix(PyObject * matrix_o,
					     double default_n_score)
{
  // require the matrix_o object to be a list;
  int len = PySequence_Size(matrix_o);
  if (len < 0) { return NULL; }

  unsigned int ulen = (unsigned int) len;

  // require each element of the list to have size 5.
  for (int row = 0; row < len; row++) {
    PyObject * row_o = PySequence_GetItem(matrix_o, row);
    int size = PySequence_Size(row_o);
    Py_DECREF(row_o);

    if (size < 4 || size > 5) {
      PyErr_SetString(MotilityError, "matrix must be list of lists with len 4 (A,C,G,T) or 5 (A,C,G,T,N)");
      return NULL;
    }
  }

  // fact checking over: let's transfer it into a double[][] & stuff
  // that into a matrix object.

  double *matrix = (double *) new double[ulen*5];
  bool error_exit = false;

  for (int row = 0; row < len && !error_exit; row++) {
    PyObject * row_o = PySequence_GetItem(matrix_o, row);
    for (int col = 0; col < 5 && !error_exit; col++) {
      PyObject * item_o = PySequence_GetItem(row_o, col);

      double item_val;
      if (item_o != NULL) {
	PyObject * float_o = PyNumber_Float(item_o);

	if (float_o == NULL) {
	  error_exit = true;
	  Py_DECREF(item_o);
	  break;
	}
	item_val = PyFloat_AsDouble(float_o);

	Py_DECREF(float_o);
	Py_DECREF(item_o);
      } else {
	assert(col == 5);
	PyErr_Clear();
	item_val = default_n_score;
      }

      matrix[row*5 + col] = item_val;
    }
    Py_DECREF(row_o);
  }

  if (error_exit) { delete matrix; return NULL; }

  motility_MatrixObject * matrix_obj = (motility_MatrixObject *) \
    PyObject_New(motility_MatrixObject, &motility_MatrixType);

  if (matrix_obj) {
    matrix_obj->matrix = matrix;
    matrix_obj->length = ulen;
  } else {
    delete matrix; matrix = NULL;
  }

  return matrix_obj;
}

//
// create_matrix -- Python function to create a matrix object for a
// Python-style matrix.  This is useful for pre-parsing matrices that
// will be re-used frequently.
//

static PyObject* create_matrix(PyObject * self, PyObject * args)
{
  PyObject * matrix_o;
  double default_N_value;

  if (!PyArg_ParseTuple(args, "Od:create_matrix",
			&matrix_o, &default_N_value)) {
    return NULL;
  }

  return (PyObject *) _parse_matrix(matrix_o, default_N_value);
}

//
// motility_matrix_dealloc -- clean up a matrix object.
//

static void motility_matrix_dealloc(PyObject* self)
{
  motility_MatrixObject * obj = (motility_MatrixObject *) self;

  delete obj->matrix;
  obj->length = 0;

  PyObject_Del((PyObject *) obj);
}

/***********************************************************************/

//
// find_exact: search for an exact match in the given sequence.
//

static PyObject * find_exact(PyObject * self, PyObject * args)
{
  char * seq_c, * motif_c;

  // Python arguments: sequence, motif.

  if (!PyArg_ParseTuple(args, "ss", &seq_c, &motif_c)) {
    return NULL;
  }

  try {
    motility::DnaSequence seq(seq_c);
    motility::LiteralMotif motif(motif_c);

    motility::MotifMatchList matches;

    Py_BEGIN_ALLOW_THREADS

    matches = *motif.find_matches(seq);

    Py_END_ALLOW_THREADS

    try {
      return _convert_results_to_tuple(matches);
    }
    catch (...) {
      throw;
    }
  } catch (motility::exception& exc) {
    // raise the error...
    PyErr_SetString(MotilityError, exc.msg.c_str());

    return NULL;
  }
}

//
// find_iupac: search for an IUPAC motif in the given sequence.
//

static PyObject * find_iupac(PyObject * self, PyObject * args)
{
  char * seq_c, * motif_c;
  int mismatches_allowed = 0;

  // Python arguments: sequence, motif, optional # of mismatches (default 0)

  if (!PyArg_ParseTuple(args, "ss|i", &seq_c, &motif_c, &mismatches_allowed)) {
    return NULL;
  }

  try {
    motility::DnaSequence seq(seq_c);
    motility::IupacMotif motif(motif_c);
    motif.mismatches(mismatches_allowed);

    motility::MotifMatchList matches;

    Py_BEGIN_ALLOW_THREADS

    matches = *motif.find_matches(seq);

    Py_END_ALLOW_THREADS

    return _convert_results_to_tuple(matches);
  } catch (motility::exception& exc) {
    // raise the error...
    PyErr_SetString(MotilityError, exc.msg.c_str());

    return NULL;
  }
}

//
// find_pwm: search for a position-weight matrix in the given sequence.
//

static PyObject * find_pwm(PyObject * self, PyObject * args)
{
  char * seq_c;
  PyObject * pwm_o;
  double threshold;

  // Python arguments: sequence, pwm, threshold.

  if (!PyArg_ParseTuple(args, "sOd", &seq_c, &pwm_o, &threshold)) {
    return NULL;
  }

  // require a pre-parsed matrix.

  motility_MatrixObject * matrix_o;
  if (is_matrix_obj(pwm_o)) {
    matrix_o = (motility_MatrixObject *) pwm_o;
  } else {
    return NULL;
  }

  //
  // Now do the search:
  //
  
  try {
    motility::DnaSequence seq(seq_c);
    motility::PwmMotif motif((double (*)[5])matrix_o->matrix,
			     matrix_o->length);
    motif.match_threshold(threshold);

    motility::MotifMatchList matches;

    Py_BEGIN_ALLOW_THREADS

    matches = *motif.find_matches(seq);

    Py_END_ALLOW_THREADS

    return _convert_results_to_tuple(matches);
  } catch (motility::exception& exc) {

    // raise the error...
    PyErr_SetString(MotilityError, exc.msg.c_str());

    return NULL;
  }
}

//
// find_energy: search for a position-weight matrix in the given sequence.
//

static PyObject * find_energy(PyObject * self, PyObject * args)
{
  char * seq_c;
  PyObject * energy_o;
  double threshold;

  // Python arguments: sequence, matrix, threshold.

  if (!PyArg_ParseTuple(args, "sOd", &seq_c, &energy_o, &threshold)) {
    return NULL;
  }

  // require a pre-parsed matrix.

  motility_MatrixObject * matrix_o;
  if (is_matrix_obj(energy_o)) {
    matrix_o = (motility_MatrixObject *) energy_o;
  } else {
    return NULL;
  }

  // do the search.
  
  try {
    motility::DnaSequence seq(seq_c);
    motility::EnergyOperator motif((double (*)[5])matrix_o->matrix,
				   matrix_o->length);
    motif.match_minimum(threshold);

    motility::MotifMatchList matches;

    Py_BEGIN_ALLOW_THREADS

    matches = *motif.find_matches(seq);

    Py_END_ALLOW_THREADS

    return _convert_results_to_tuple(matches);
  } catch (motility::exception& exc) {

    // raise the error...
    PyErr_SetString(MotilityError, exc.msg.c_str());

    return NULL;
  }
}

//
// calc_score: calculate the score of the match.
//

static PyObject * calc_score(PyObject * self, PyObject * args)
{
  char * motif_c;
  PyObject * energy_o;

  // Python arguments: motif, matrix.

  if (!PyArg_ParseTuple(args, "sO", &motif_c, &energy_o)) {
    return NULL;
  }
  
  // do we have a pre-parsed matrix (a MatrixObject) or is it a list-of-lists?

  motility_MatrixObject * matrix_o;
  if (is_matrix_obj(energy_o)) {
    matrix_o = (motility_MatrixObject *) energy_o;
  } else {
    return NULL;
  }

  // do the calculation.
  
  try {
    motility::DnaSequence seq(motif_c);
    motility::EnergyOperator motif((double (*)[5])matrix_o->matrix,
				   matrix_o->length);

    double score = motif.calc_score(seq, 0);

    PyObject * ret = Py_BuildValue("d", score);

    return ret;
  } catch (motility::exception& exc) {

    // raise the error...
    PyErr_SetString(MotilityError, exc.msg.c_str());

    return NULL;
  }
}

//
// calc_energy: calculate the energy of the match.
//

static PyObject * calc_energy(PyObject * self, PyObject * args)
{
  char * motif_c;
  PyObject * energy_o;

  // Python arguments: motif, matrix.

  if (!PyArg_ParseTuple(args, "sO", &motif_c, &energy_o)) {
    return NULL;
  }
  
  // require a pre-parsed matrix.

  motility_MatrixObject * matrix_o;
  if (is_matrix_obj(energy_o)) {
    matrix_o = (motility_MatrixObject *) energy_o;
  } else {
    return NULL;
  }

  // do the calculation.
  
  try {
    motility::DnaSequence seq(motif_c);
    motility::EnergyOperator motif((double (*)[5])matrix_o->matrix,
				   matrix_o->length);

    double score = motif.calc_score(seq, 0);

    PyObject * ret = Py_BuildValue("d", score);

    return ret;
  } catch (motility::exception& exc) {

    // raise the error...
    PyErr_SetString(MotilityError, exc.msg.c_str());

    return NULL;
  }
}

//
// generate_sites_under
//

static PyObject * generate_sites_under(PyObject * self, PyObject * args)
{
  PyObject * energy_o;
  double threshold;
  int allow_n;

  // Python arguments: matrix, threshold, bool.

  if (!PyArg_ParseTuple(args, "Odi", &energy_o, &threshold, &allow_n)) {
    return NULL;
  }

  // require a pre-parsed matrix.

  motility_MatrixObject * matrix_o;
  if (is_matrix_obj(energy_o)) {
    matrix_o = (motility_MatrixObject *) energy_o;
  } else {
    return NULL;
  }

  try {
    motility::EnergyOperator motif((double (*)[5])matrix_o->matrix,
				   matrix_o->length);

    bool use_n = false;
    if (allow_n) {
      use_n = true;
    }

    std::vector<std::string> l;
    l = motif.generate_sites_under(threshold, use_n);

    PyObject * los = PyTuple_New(l.size());
    
    for (unsigned int i = 0; i < l.size(); i++) {
      PyObject * s = PyString_FromString(l[i].c_str());
      PyTuple_SET_ITEM(los, i, s);
    }

    return los;
  } catch (motility::exception& exc) {

    // raise the error...
    PyErr_SetString(MotilityError, exc.msg.c_str());

    return NULL;
  }
}

//
// generate_sites_over
//

static PyObject * generate_sites_over(PyObject * self, PyObject * args)
{
  PyObject * energy_o;
  double threshold;
  int allow_n;

  // Python arguments: matrix, threshold, bool

  if (!PyArg_ParseTuple(args, "Odi", &energy_o, &threshold, &allow_n)) {
    return NULL;
  }

  // require a pre-parsed matrix.

  motility_MatrixObject * matrix_o;
  if (is_matrix_obj(energy_o)) {
    matrix_o = (motility_MatrixObject *) energy_o;
  } else {
    return NULL;
  }

  try {
    motility::EnergyOperator motif((double (*)[5])matrix_o->matrix,
				   matrix_o->length);

    bool use_n = false;
    if (allow_n) {
      use_n = true;
    }

    std::vector<std::string> l;
    l = motif.generate_sites_over(threshold, use_n);

    PyObject * los = PyTuple_New(l.size());
    
    for (unsigned int i = 0; i < l.size(); i++) {
      PyObject * s = PyString_FromString(l[i].c_str());
      PyTuple_SET_ITEM(los, i, s);
    }

    return los;
  } catch (motility::exception& exc) {

    // raise the error...
    PyErr_SetString(MotilityError, exc.msg.c_str());

    return NULL;
  }
}

//
// weight_sites_under
//

static PyObject * weight_sites_under(PyObject * self, PyObject * args)
{
  PyObject * energy_o;
  double threshold;
  double AT_bias, GC_bias;

  // Python arguments: matrix, threshold, bool.

  if (!PyArg_ParseTuple(args, "Oddd", &energy_o, &threshold,
			&AT_bias, &GC_bias)) {
    return NULL;
  }

  // require a pre-parsed matrix.

  motility_MatrixObject * matrix_o;
  if (is_matrix_obj(energy_o)) {
    matrix_o = (motility_MatrixObject *) energy_o;
  } else {
    return NULL;
  }

  try {
    motility::EnergyOperator motif((double (*)[5])matrix_o->matrix,
				   matrix_o->length);

    double weight = motif.weight_sites_under(threshold, AT_bias, GC_bias);

    return PyFloat_FromDouble(weight);
  } catch (motility::exception& exc) {

    // raise the error...
    PyErr_SetString(MotilityError, exc.msg.c_str());

    return NULL;
  }
}

//
// weight_sites_over
//

static PyObject * weight_sites_over(PyObject * self, PyObject * args)
{
  PyObject * energy_o;
  double threshold, AT_bias, GC_bias;

  // Python arguments: matrix, threshold, bool

  if (!PyArg_ParseTuple(args, "Oddd", &energy_o, &threshold,
			&AT_bias, &GC_bias)) {
    return NULL;
  }

  // require a pre-parsed matrix.

  motility_MatrixObject * matrix_o;
  if (is_matrix_obj(energy_o)) {
    matrix_o = (motility_MatrixObject *) energy_o;
  } else {
    return NULL;
  }

  try {
    motility::EnergyOperator motif((double (*)[5])matrix_o->matrix,
				   matrix_o->length);

    double weight = motif.weight_sites_over(threshold, AT_bias, GC_bias);

    return PyFloat_FromDouble(weight);
  } catch (motility::exception& exc) {

    // raise the error...
    PyErr_SetString(MotilityError, exc.msg.c_str());

    return NULL;
  }
}

//
// max_score
//

static PyObject * max_score(PyObject * self, PyObject * args)
{
  PyObject * energy_o;
  int allow_n;

  // Python arguments: matrix, threshold, bool.
  if (!PyArg_ParseTuple(args, "Oi", &energy_o, &allow_n)) {
    return NULL;
  }

  //
  // *Must* take a pre-parsed matrix as an argument.
  //

  motility_MatrixObject * matrix_o;
  if (is_matrix_obj(energy_o)) {
    matrix_o = (motility_MatrixObject *) energy_o;
  } else {
    return NULL;
  }

  try {
    motility::EnergyOperator motif((double (*)[5])matrix_o->matrix,
				   matrix_o->length);

    bool use_n = false;
    if (allow_n) {
      use_n = true;
    }

    double score = motif.max_score();

    return PyFloat_FromDouble(score);
  } catch (motility::exception& exc) {

    // raise the error...
    PyErr_SetString(MotilityError, exc.msg.c_str());

    return NULL;
  }
}

//
// min_score
//

static PyObject * min_score(PyObject * self, PyObject * args)
{
  PyObject * energy_o;
  int allow_n;

  // Python arguments: matrix, threshold, bool.
  if (!PyArg_ParseTuple(args, "Oi", &energy_o, &allow_n)) {
    return NULL;
  }

  //
  // *Must* take a pre-parsed matrix as an argument.
  //

  motility_MatrixObject * matrix_o;
  if (is_matrix_obj(energy_o)) {
    matrix_o = (motility_MatrixObject *) energy_o;
  } else {
    return NULL;
  }

  try {
    motility::EnergyOperator motif((double (*)[5])matrix_o->matrix,
				   matrix_o->length);

    bool use_n = false;
    if (allow_n) {
      use_n = true;
    }

    double score = motif.min_score(use_n);

    return PyFloat_FromDouble(score);
  } catch (motility::exception& exc) {

    // raise the error...
    PyErr_SetString(MotilityError, exc.msg.c_str());

    return NULL;
  }
}

//
// Module machinery.
//

static PyMethodDef MotilityMethods[] = {
  { "create_matrix", create_matrix, METH_VARARGS, "Create a matrix object" },
  { "find_exact", find_exact, METH_VARARGS, "Find exact matches.  Takes sequence, motif to find." },
  { "find_iupac", find_iupac, METH_VARARGS, "Find IUPAC motifs.  Takes sequence, motif to find.  Optional argument: # of mismatches." },
  { "find_pwm", find_pwm, METH_VARARGS, "Find PWM matches" },
  { "calc_score", calc_energy, METH_VARARGS, "Calculate the score of a PWM match" },
  { "find_energy", find_energy, METH_VARARGS, "Find energy operator matches" },
  { "calc_energy", calc_energy, METH_VARARGS, "Calculate the energy of an energy operator match" },
  { "generate_sites_over", generate_sites_over, METH_VARARGS,
    "Generate all sites with a score over the given threshold" },
  { "generate_sites_under", generate_sites_under, METH_VARARGS,
    "Generate all sites with a score under the given threshold"},
  { "weight_sites_over", weight_sites_over, METH_VARARGS,
    "Weight all sites with a score over the given threshold"},
  { "weight_sites_under", weight_sites_under, METH_VARARGS,
    "Weight all sites with a score under the given threshold"},
  { "max_score", max_score, METH_VARARGS,
    "Calculate the maximum possible score under this matrix." },
  { "min_score", min_score, METH_VARARGS,
    "Calculate the minimum possible score under this matrix." },
  { NULL, NULL, 0, NULL }
};

DL_EXPORT(void) init_motility(void)
{
  motility_MatrixType.ob_type = &PyType_Type;

  PyObject * m, * d;
  m = Py_InitModule("_motility", MotilityMethods);

  d = PyModule_GetDict(m);
  MotilityError = PyErr_NewException("_motility.MotilityError", NULL, NULL);
  PyDict_SetItemString(d, "MotilityError", MotilityError);  
}
