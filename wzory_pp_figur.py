from math import pi as PI
from math import sqrt
#wzor na pp kwadratu
a = float(input())
print(f"pp kwadratu o boku {a} = {a**2}")
#wzor na pp trojkąta
a = float(input())
h = float(input())
print(f"pp trojkata o boku {a} i wysokosci {h} = {a*h/2}")
#wzor na pp prostokąta
a = float(input())
b = float(input())
print(f"pp prostokata o bokach {a} i {b} = {a*b}")
#wzor na pp koła
r = float(input())
print(f"pp kola o promieniu {r} = {PI*r**2}")
#wzor na pp rownolegloboku
a = float(input())
h = float(input())
print(f"pp rownolegloboku o boku {a} i wysokosci {h} = {a*h}")
#wzor na pp rombu
e = float(input())
f = float(input())
print(f"pp rombu o przekatnych {e} i {f} = {e*f/2}")
#wzor na pp trapezu
a = float(input())
b = float(input())
h = float(input())
print(f"pp trapezu o bokach {a} {b} i {h} = {(a+b)*h/2}")
#wzor na pp sześciokąta foremnego
a = float(input())
print(f"pp szesciokata foremnego o boku {a} = {3*a**2*sqrt(3)/2}")
