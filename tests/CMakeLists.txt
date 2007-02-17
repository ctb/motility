INCLUDE_DIRECTORIES(../src/)
LINK_DIRECTORIES(../src/)
LINK_LIBRARIES(motility)

ADD_EXECUTABLE(test-sequence test-sequence.cc)
ADD_TEST(sequence test-sequence)

ADD_EXECUTABLE(test-find-literal test-find-literal.cc)
ADD_TEST(find-literal test-find-literal)

ADD_EXECUTABLE(test-find-pwm test-find-pwm.cc)
ADD_TEST(find-pwm test-find-pwm)

ADD_EXECUTABLE(test-find-iupac test-find-iupac.cc)
ADD_TEST(find-iupac test-find-iupac)

ADD_EXECUTABLE(test-find-op test-find-op.cc)
ADD_TEST(find-op test-find-op)
