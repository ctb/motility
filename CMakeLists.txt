cmake_minimum_required(VERSION 2.6)
SET(CMAKE_VERBOSE_MAKEFILE ON)
set(CMAKE_CXX_COMPILER "/usr/bin/g++")
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fPIC")

Project(motility)


SUBDIRS(src tests python)
