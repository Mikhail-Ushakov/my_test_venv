def a():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    return __init__
b = a()

b(4,5)
print(type(b), b.x, b.y)