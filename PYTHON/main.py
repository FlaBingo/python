import os


if (not os.path.exists("PYTHON\data")):
    os.mkdir("PYTHON\data")


for i in range(1, 101):
    os.mkdir(f"PYTHON\data\Day{i}")











