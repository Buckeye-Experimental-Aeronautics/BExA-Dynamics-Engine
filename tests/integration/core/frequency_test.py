from sim.harness import Module, Sim


class State:
    x = 0


class Sensor(Module):
    def clock(self):
        self.tick_rate = 2
        self.state.x += 1


def test_simple():
    sim = Sim(State, 100)
    sim.set_loop(Sensor)
    sim.run()

    assert sim.state.x == 50
