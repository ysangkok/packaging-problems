import os
with open(os.path.join(os.path.join(os.path.dirname(__file__), "sometimes_included"), "file.txt")) as f:
    print(f.read())
