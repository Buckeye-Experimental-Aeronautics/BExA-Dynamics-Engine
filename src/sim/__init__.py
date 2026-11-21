from .harness import Sim
from .modules.__state__ import State

# any user defined modules
from .modules.__module_template__ import *

end_time = 100


def main() -> None:
    sim = Sim(State, end_time)

    # define what the loop *is*
    # it updates in the order you define
    #   - this is only relevant if they have the same tick_rate
    #   - this is just a tie breaker, really
    sim.set_loop(Sensor)

    sim.start()
    print(sim.state.x)
