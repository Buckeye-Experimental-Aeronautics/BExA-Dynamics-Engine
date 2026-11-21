from sim.harness import Module, Sim


class State:
    x = 0
    y = 0


class SensorX(Module):
    def clock(self):
        self.state.x += 1


class SensorY(Module):
    def clock(self):
        self.state.y += 2


def test_simple():
    sim = Sim(State, 100)
    sim.set_loop(SensorX, SensorY)
    sim.run()

    assert sim.state.x == 100
    assert sim.state.y == 200
