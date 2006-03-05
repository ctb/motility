# File : Makefile.PL
use ExtUtils::MakeMaker;
WriteMakefile(
	      'NAME' => 'motility_ext',
	      'INC' => '-I../../src -I../',
	      'OBJECT' => '_motility_extmodule.o',
	      'LIBS' => '-L../ -linterface -L../../src -lmotility -lstdc++'
	      );
