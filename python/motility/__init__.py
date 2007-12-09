##
## This file is part of the motility source distribution.
##
## motility is part of the Cartwheel bioinformatics toolkit:
##
##                 http://cartwheel.caltech.edu/
##
## Contact author: C. Titus Brown, titus@caltech.edu.
##
## This program and all associated source code files are Copyright (C) 2003
## the California Institute of Technology, Pasadena, CA, 91125 USA.  It is
## under the Lesser GNU Public License; please see the included LICENSE.txt
## file for more information, or contact Titus directly.
##
##

"""
A set of convenient OO Python interfaces to the _motility extension module.
"""

__version__ = "0.8"

import _motility

# find_exact is the straight C function
find_exact = _motility.find_exact

# find_iupac is the same.
find_iupac = _motility.find_iupac

from objects import EnergyOperator, PWM, IUPAC
import op_en
