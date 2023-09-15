# two.py

import one

print("TOP LEVEL IN TWO.PY")

one.func()

if __name__ == "__main__":
    print("Two.py is being run driectly")

else:
    print("TWO.PY has been imported")