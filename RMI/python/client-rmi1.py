import Pyro4

# Connect to the Pyro daemon on the server
uri = "PYRO:obj_36b9a492100f4f0f82511c6869618c17@localhost:50000"
calculator = Pyro4.Proxy(uri)

# Use the Calculator object as if it were a local object
result = calculator.add(5, 3)
print(f"The result is: {result}")
