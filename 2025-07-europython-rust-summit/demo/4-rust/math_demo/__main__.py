from cowpy.cow import Cowacter

from .math_demo import add

message = Cowacter().milk(f"3 + 5 = {add(3, 5)}")
print(message)
