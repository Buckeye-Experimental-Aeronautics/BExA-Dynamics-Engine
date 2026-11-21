from sim.harness import Module, Sim


class State:
    x = 0


class Sensor1(Module):
    def clock(self):
        self.state.x += 1


class Sensor2(Module):
    def clock(self):
        self.state.x += 2


def test_simple():
    sim = Sim(State, 100)
    sim.set_loop(Sensor1, Sensor2)
    sim.run()

    assert sim.state.x == 300
