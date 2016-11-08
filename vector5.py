_author__ = 'student'
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

    def vpro(self, other, other1):
        v= abs((self.x-other.x)*(self.y-other1.y) - (self.y-other.y)*(self.x-other1.x)) / 2

maxs=-1000000
N=int(input())
a=[]*N
for i in range(N):
    x, y=map(int, input().split())
    a.append(vector(x, y))
for i in a:
    for j in a:
        for k in a:
            s=i.vpro(j, k)

            if s > maxs:
                maxs=s
print(maxs)

