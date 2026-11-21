from abc import abstractmethod
from .modules.__state__ import State


class Sim:
    def __init__(self, state: type[State], end: int) -> None:
        """
        Wrapper class that is the simulation for the harness itself.
        Constructor is used for basic configuration.
        """
        self.end: int = end
        self.mods: list[Module] = []
        self.state: State = state()

    def set_loop(self, *modules: type[Module]) -> None:
        """
        Set the relevant modules. The order matters: the order of sensors being passed in is the order they are updated
        """
        for mod in modules:
            self.mods.append(mod(self.state))

    def run(self):
        for i in range(self.end):
            # TODO: if perf ever becomes an issue, replace this for a scheduler of some kind
            # look into rings, heap schedulers, or even just grouping them for fewer mod ops
            for mod in self.mods:
                mod._try_clock(i)



class Module:
    def __init__(self, state: State) -> None:
        """Abstract class that is used for sensors and the physics loop itself. Generically refered to as modules"""
        # TODO: write a helper that translates frequency to a relative engine tick rate
        self.state = state

        # configurable states
        self.tick_rate = 1

    def _try_clock(self, tick: int):
        if tick % self.tick_rate == 0:
            self.clock()

    @abstractmethod
    def clock(self) -> None:
        pass
