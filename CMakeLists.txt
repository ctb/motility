#SET(CMAKE_VERBOSE_MAKEFILE ON)

Project(motility)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fPIC")

SUBDIRS(src tests python)
