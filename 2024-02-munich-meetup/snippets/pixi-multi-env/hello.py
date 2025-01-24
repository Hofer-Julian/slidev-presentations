from sys import version_info as vi
from cowpy.cow import Cowacter

python_version = f"Python {vi.major}.{vi.minor}"
msg = Cowacter().milk(f"Hello from {python_version}!")
print(msg)
