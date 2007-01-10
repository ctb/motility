SET(LIB_SRC DnaSequence.cc motility.cc LiteralMotif.cc _MatrixMotif.cc
        PwmMotif.cc IupacMotif.cc EnergyOperator.cc
)
ADD_LIBRARY(motility ${LIB_SRC})

