from cowpy.cow import Cowacter


def add(a, b):
    return a + b


message = Cowacter().milk("3 + 5 = " + str(add(3, 5)))
print(message)
