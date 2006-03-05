## should be included by motility.i

#
# typemap to convert MotifMatchList* return values into Python objects.
#

%typemap(python, out) motility::MotifMatchList* {
    std::vector<motility::MotifMatch*> l = $1->list();
    PyObject * t = PyTuple_New(l.size());

    for (unsigned int i = 0; i < l.size(); i++) {
      motility::MotifMatch * m = l[i];

      int orientation = m->start > m->end ? -1 : 1;
      unsigned int start = orientation < 0 ? m->end : m->start;
      unsigned int end = orientation < 0 ? m->start : m->end;

      PyObject * u = Py_BuildValue("iiis", start, end, orientation,
				   m->match_seq.sequence().c_str());
      PyTuple_SET_ITEM(t, i, u);
    }

    $result = t;
}

#
# typemap to convert a Python list-of-lists into a matrix suitable for PWM/
# energy operator searches.
#

%typemap(python, in) _DoubleMatrix* {
    PyObject * matrix_o = $input;

    int len = PySequence_Size(matrix_o);
    if (len < 0) { $1 = NULL; }
    else {
      unsigned int ulen = (unsigned int) len;

      // require each element of the list to have size 5.
      for (int row = 0; row < len; row++) {
	PyObject * row_o = PySequence_GetItem(matrix_o, row);
	int size = PySequence_Size(row_o);
	Py_DECREF(row_o);

	if (size != 5) {
	  $1 = NULL;
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
	  PyObject * float_o = PyNumber_Float(item_o);

	  if (float_o == NULL) {
	    error_exit = true;
	    Py_DECREF(item_o);
	    break;
	  }

	  matrix[row*5 + col] = PyFloat_AsDouble(float_o);

	  Py_DECREF(float_o);
	  Py_DECREF(item_o);
	}
	Py_DECREF(row_o);
      }

      if (error_exit) { free(matrix); return NULL; }

      _DoubleMatrix * matrix_obj = (_DoubleMatrix *) malloc(sizeof(_DoubleMatrix));
      matrix_obj->_matrix = matrix;
      matrix_obj->length = ulen;

      $1 = matrix_obj;
    }
}

