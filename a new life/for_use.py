"""
def is_prime(n:int) -> bool:
    if n <= 1:
        return False
    else:
        for i  in range(2, int(n**0.5 + 1)): #range(2, ...) это начиная с i = 2 | n**0.5 это корень из n
            if n % i == 0:
                return False
            else:
                return True
"""


"""
#Через факториал
def c_f(n:int):
    return calc_fact(n, 1, 1)

def calc_fact(n: int, i: int, sum: int) -> int:
    if i > n:
        return sum
    return calc_fact(n, i + 1, sum=i * sum)

#По обычному
def factorial(n):
    sum = 1
    for i in range(1, n+1):
        sum *= i
    return sum
"""

"""
def is_pol1(stroke:str) -> bool:
    a = stroke.lower().strip()
    x = ""
    for i in range(1, len(a) + 1):
        x += a[-i]

    if a == x:
        return True
    return False

def is_pol2(stroke: str) -> bool:
    a = stroke.lower().strip()
    return a == a[::-1] -----------------------------------------a[::-1]

def is_pol3(stroke: str) -> bool:
    a = stroke.lower().strip()
    return a == ''.join(reversed(a)) ----------------------------join
"""

def a():
    aaa = set([])
    for i in range(100, 1000):
        aa: str = ''
        while i != 1:
            if i % 2 == 1:
                aa += '1'
            elif i % 2 == 0:
                aa += '0'

            i = (i - (i%2)) / 2

        aa+='1'

        aaa.add(aa[::-1])
    return aaa

print(len(a()))


