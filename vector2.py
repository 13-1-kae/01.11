__author__ = 'student'
class vector():
    def __init__(self, x, y):
        self.x=x
        self.y=y
        self.colour='violet'

    def __lt__(self, other):
        return self.x < other.x or self.x == other.x and self.y < other.y

    def __gt__(self, other):
        return self.x > other.x or self.x == other.x and self.y > other.y

    def __add__(self, other):
        return vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return vector(self.x - other.x, self.y - other.y)

    def length(self):
        l=(self.x**2 + self.y**2)**(1/2)
        return l

    def __str__(self):
        return self.x, self.y
lmax = 0
N = int(input())
for i in range(N):
    x, y = map(int, input().split())
    a = vector(x, y)
    l = a.length()
    if l > lmax:
        lmax = l
        xmax = a.x
        ymax = a.y
print(xmax, ' ', ymax)
