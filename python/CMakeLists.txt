FIND_PROGRAM(PYTHON_EXECUTABLE 
    NAMES python2.5 python2.4 python2.3
     [HKEY_LOCAL_MACHINE\\SOFTWARE\\Python\\PythonCore\\2.5\\InstallPath]
     [HKEY_LOCAL_MACHINE\\SOFTWARE\\Python\\PythonCore\\2.4\\InstallPath]
     [HKEY_LOCAL_MACHINE\\SOFTWARE\\Python\\PythonCore\\2.3\\InstallPath]
)

SET(PYTHONINTERP_FOUND)
IF(PYTHON_EXECUTABLE)
  SET(PYTHONINTERP_FOUND ON)
ENDIF(PYTHON_EXECUTABLE)

IF(PYTHONINTERP_FOUND) 
  # I needed to split into the C compiling and python compiling
  # so I could add the -L option to specify where CMake had built the
  # library (-L option)
  ADD_CUSTOM_TARGET(motility_ext ALL
       COMMAND ${PYTHON_EXECUTABLE} 
               ${CMAKE_CURRENT_SOURCE_DIR}/setup.py
               build_ext
               -t ${CMAKE_CURRENT_BINARY_DIR}
               -b ${CMAKE_CURRENT_BINARY_DIR}
               -L ${CMAKE_CURRENT_BINARY_DIR}/../lib
       WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
       DEPENDS motility
       VERBATIM
  )
  ADD_CUSTOM_TARGET(motility_py ALL
       COMMAND ${PYTHON_EXECUTABLE} 
               ${CMAKE_CURRENT_SOURCE_DIR}/setup.py
               build_py
               -d ${CMAKE_CURRENT_BINARY_DIR}
       WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
       VERBATIM
  )

  ADD_CUSTOM_TARGET(motility_py_install
	COMMAND ${PYTHON_EXECUTABLE}
		${CMAKE_CURRENT_SOURCE_DIR}/setup.py
		install
	VERBATIM
  )

  INSTALL(CODE "EXECUTE_PROCESS(COMMAND ${PYTHON_EXECUTABLE} setup.py install WORKING_DIRECTORY python)")

#  FIND_PROGRAM(NOSE nosetests)
#  ADD_TEST(paircomp_python_tests 
#           ${PYTHON_EXECUTABLE} ${NOSE}
#           -w ${CMAKE_CURRENT_SOURCE_DIR}/../
#  )
ENDIF(PYTHONINTERP_FOUND)
