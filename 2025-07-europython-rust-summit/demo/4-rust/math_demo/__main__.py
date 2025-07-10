from cowpy.cow import Cowacter

from .math_demo import add

message = Cowacter().milk(f"3 + 7 = {add(3, 7)}")
print(message)
