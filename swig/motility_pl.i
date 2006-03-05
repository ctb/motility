## should be included by motility_py.i

#
# typemap to convert MotifMatchList* return values into Perl objects.
#

%typemap(perl5, out) motility::MotifMatchList* {
    std::vector<motility::MotifMatch*> l = $1->list();

    // construct an array value to hold the return values
    AV * t = newAV();
  
    // Now, for each result, create a hash & put a reference
    // to it into the return array value 't'.

    for (unsigned int i = 0; i < l.size(); i++) {
      motility::MotifMatch * m = l[i];

      int orientation = m->start > m->end ? -1 : 1;
      unsigned int start = orientation < 0 ? m->end : m->start;
      unsigned int end = orientation < 0 ? m->start : m->end;

      // Store the results in a hash.
      HV * u = newHV();
      hv_store(u, "start", strlen("start"), newSViv(start), 0);
      hv_store(u, "end", strlen("end"), newSViv(end), 0);
      hv_store(u, "orientation", strlen("orientation"),
	       newSViv(orientation), 0);
      hv_store(u, "match", strlen("match"),
	       newSVpv(m->match_seq.sequence().c_str(), 0), 0);

      // Tack 'u' onto 't'.
      u = (HV *) sv_2mortal((SV *)u);
      av_push(t, newRV((SV *)u));
    }

    // Return a reference to t on the Perl stack.  (ick!)
    ST(argvi) = newRV((SV *)t);
    sv_2mortal(ST(argvi));

    argvi++;
    XSRETURN(argvi);
}

#
# typemap to convert a Perl list-of-hashes into a matrix suitable for PWM/
# energy operator searches.
#

%typemap(perl5, in) _DoubleMatrix* {
  if (!SvROK($input)) {
    croak("must pass in a reference to an array of hashes");
  }

  AV * perl_loh = (AV*) SvRV($input);

  unsigned int len = av_len(perl_loh) + 1;

  if (len == 0) {
    croak("must pass in an array containing at least one element");
  }

  // allocate the return info
  double * _matrix = (double *) new double[len * 5];

  for (int row = 0; row < len; row++) {
    SV ** element = av_fetch(perl_loh, row, 0);

    // check that there's an element, that it's a reference, and that it's
    // a reference to a hash.
    if (element == NULL || !SvROK(*element) || 
	SvTYPE(SvRV(*element)) != SVt_PVHV) {

      delete _matrix;
      
      croak("must pass in an array containing references to hashes in each row");
    }
    HV * hash = (HV *) SvRV(*element);

    // Get the values from the hash.
    SV ** A_val = hv_fetch(hash, "A", 1, 0);
    SV ** C_val = hv_fetch(hash, "C", 1, 0);
    SV ** G_val = hv_fetch(hash, "G", 1, 0);
    SV ** T_val = hv_fetch(hash, "T", 1, 0);
    SV ** N_val = hv_fetch(hash, "N", 1, 0);

    if (A_val == NULL || C_val == NULL || G_val == NULL ||
	T_val == NULL || N_val == NULL) {
      delete _matrix;

      croak("must define scores for A, C, G, T, and N");
    }

    if (!(SvNOK(*A_val) && SvNOK(*C_val) && SvNOK(*G_val) && 
	  SvNOK(*T_val) && SvNOK(*N_val))) {
      delete _matrix;

      croak("all hash entries must be numbers");
    }

    double A = SvNV(*A_val);
    double C = SvNV(*C_val);
    double G = SvNV(*G_val);
    double T = SvNV(*T_val);
    double N = SvNV(*N_val);

    _matrix[row*5 + 0] = A;
    _matrix[row*5 + 1] = C;
    _matrix[row*5 + 2] = G;
    _matrix[row*5 + 3] = T;
    _matrix[row*5 + 4] = N;
  }

  // construct the return argument.

  _DoubleMatrix * matrix = new _DoubleMatrix;
  matrix->length = len;
  matrix->_matrix = _matrix;
  $1 = matrix;
}
