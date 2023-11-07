import Pyro4

class Calculator:
    def add(self, a, b):
        return a + b

daemon = Pyro4.Daemon()
uri = daemon.register(Calculator())

# Register the object with a name in the Pyro4 naming service
with Pyro4.locateNS() as ns:
    ns.register("my_calculator", uri)

print(f"URI: {uri}")
daemon.requestLoop()
