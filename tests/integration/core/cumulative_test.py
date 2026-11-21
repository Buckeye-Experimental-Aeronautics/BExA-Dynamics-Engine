from sim.harness import Module, Sim


class State:
    x = 0
    y = 0


class SensorA(Module):
    def clock(self):
        self.tick_rate = 1
        self.state.x += 1


class SensorB(Module):
    def clock(self):
        self.tick_rate = 1
        self.state.y += 1


class SensorC(Module):
    def clock(self):
        self.tick_rate = 2
        self.state.x += 1
        self.state.y += 1


def test():
    sim = Sim(State, 100)
    sim.set_loop(SensorA, SensorB, SensorC)
    sim.run()

    assert sim.state.x == 150
    assert sim.state.y == 150
