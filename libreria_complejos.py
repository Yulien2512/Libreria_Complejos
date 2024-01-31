import math

def suma(a, b):

    pr = a[0] + b[0]
    pi = a[1] + b[1]

    return (pr, pi)

def producto(a, b):
    
    pr = a[0] * b[0] - a[1] * b[1]
    pi = b[0] * a[1] + b[0] * a[1]

    return (pr, pi)

def resta(a, b):

    pr = a[0] - b[0]
    pi = a[1] - b[1]

    return (pr, pi)

def division(a, b):

    num1 = (a[0]* b[0] + a[1]* b[1]) /(b[0]**2 + b[1]**2)
    num2 = (a[1]* b[0] - a[0]* b[1]) /(b[0]**2 + b[1]**2)
   
    return (num1, num2)

def modulo(a):

    num = ((a[0] ** 2 + a[1] ** 2)** 0.5)
    return num

def conjugado(c):
    a = c[0]
    b = -c[1]

    return (a, b)

def polar(c):
    r = ((c[0]**2 + c[1]**2)**0.5)
    ang = math.degrees(math.atan2(c[1], c[0]))

    return (r, ang)
    
def cartesiano(c):

    r, ang = c[0], math.radians(c[1])
    x = r * math.cos(ang)
    y = r * math.sin(ang)

    return(x,y)


def fase(c):

    pr = c[0]
    pi = c[1]

    res = math.degrees(math.atan2(pi , pr))
    return res


if __name__ == '__main__':
          
    print(suma((2.3,6.5), (1.4, -5.2)))
    print(producto((2.3,6.5), (1.4, -5.2)))
    print(resta((2.3,6.5), (1.4, -5.2)))
    print(division((2.3,6.5), (1.4, -5.2)))
    print(modulo((2.3,6.5)))
    print(conjugado((2.3,6.5)))
    print(polar((2.3,6.5)))
    print(cartesiano((2.3,6.5)))
    print(fase((2.3,6.5)))
