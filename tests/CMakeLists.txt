INCLUDE_DIRECTORIES(../src/)
LINK_DIRECTORIES(../src/)
LINK_LIBRARIES(motility)

ADD_EXECUTABLE(test-sequence test-sequence.cc)
ADD_EXECUTABLE(test-find-literal test-find-literal.cc)
ADD_EXECUTABLE(test-find-pwm test-find-pwm.cc)
ADD_EXECUTABLE(test-find-iupac test-find-iupac.cc)
ADD_EXECUTABLE(test-find-op test-find-op.cc)
