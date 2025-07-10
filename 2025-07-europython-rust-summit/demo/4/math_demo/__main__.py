from cowpy.cow import Cowacter

from .math_demo import add  # type: ignore

message = Cowacter().milk("3 + 5 = " + str(add(3, 5)))
print(message)
