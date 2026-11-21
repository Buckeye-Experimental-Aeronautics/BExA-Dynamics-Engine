# This is the bare minimum required to add a module
# after defining a module:
#   1. define the import in __init__.py (its documented in there)
#   2. add the class name into sim.set_loop()
#
# if your module requires any extra state, make sure you edit the state class in __state__.py

# this import is required as all modules come from a parent class
from ..harness import Module

# the name of course can be whatever you'd like
# however, it MUST inherit from `Module`
class Sensor(Module):
    # this is where all the logic lives
    def clock(self):
        # these are configurable values for a module
        # default values are given, but this is how you would change one
        self.tick_rate = 1 

        # state is shared among all modules. 
        # updating state like this should only be done for core physics simulation functionality, for example, simulating drag
        self.state.x += 1

