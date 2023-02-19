import os
import generate
import simulate

for i in range(2):
    os.system("py generate.py")
    os.system("py simulate.py")