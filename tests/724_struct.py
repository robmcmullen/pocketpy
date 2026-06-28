try:
    import struct
except ImportError:
    print('struct is not enabled, skipping test...')
    exit()

assert struct.calcsize("b") == 1
assert struct.calcsize("B") == 1
assert struct.calcsize("h") == 2
assert struct.calcsize("H") == 2
assert struct.calcsize("i") == 4
assert struct.calcsize("I") == 4
assert struct.calcsize("l") == 4
assert struct.calcsize("L") == 4
assert struct.calcsize("q") == 8
assert struct.calcsize("Q") == 8
assert struct.calcsize("e") == 2
assert struct.calcsize("f") == 4
assert struct.calcsize("d") == 8
assert struct.calcsize("x") == 1
assert struct.calcsize("10s") == 10

assert struct.calcsize("2h") == 4
assert struct.calcsize("2h2h2h") == 12
