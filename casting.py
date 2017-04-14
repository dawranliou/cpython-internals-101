# from http://stackoverflow.com/questions/35229877/why-is-calling-float-on-a-number-slower-than-adding-0-0-in-python


def cast_1():
    total = 0
    for _ in range(10000):
        total += float(1)

def cast_2():
    total = 0
    for _ in range(10000):
        total += 1 + 0.0
