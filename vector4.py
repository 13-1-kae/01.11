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

    def per(self, other, other1):
        return ((self-other).length() + (self-other1).length()+ (other-other1).length())
maxper=-1
N=int(input())
a=[None]*N
for i in range(N):
    x, y=map(int, input().split())
    a[i]=vector(x, y)

for i in a:
    for j in a:
        for k in a:
            if i.per(j, k)>maxper:
                maxper=i.per(j, k)

print(maxper)






