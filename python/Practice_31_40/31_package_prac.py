# import package.thailand
# trip_to = package.thailand.ThailandPackage()
# trip_to.detail()

# from package.thailand import ThailandPackage
# trip_to = ThailandPackage()
# trip_to.detail()

# from package import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

from package import *
# trip_to = vietnam.VietnamPackage()
trip_to = thailand.ThailandPackage()
trip_to.detail()

import inspect
import random
print(inspect.getfile(random))
print(inspect.getfile(thailand))
