from cowpy.cow import Cowacter

def add(a, b):
    return a + b

message = Cowacter().milk(f"3 + 5 = {add(3, 5)}")
print(message)