import Pyro4

# Look up the object using the name from the naming service
with Pyro4.locateNS() as ns:
    uri = ns.lookup("my_calculator")

calculator = Pyro4.Proxy(uri)
result = calculator.add(5, 3)
print(f"The result is: {result}")
