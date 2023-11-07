import Pyro4

@Pyro4.expose
class Calculator:
    def add(self, a, b):
        return a + b

# Create a Pyro daemon
daemon = Pyro4.Daemon()

# Register the Calculator object with the Pyro daemon
calculator = Calculator()
uri = daemon.register(calculator)

# Print the URI of the object
print(f"URI: {uri}")

# Start the event loop
daemon.requestLoop()
