def triangle(a, b, c):
    if a + b > c and a + c > b and b + a > c:
        print("Это треугольник")
    else:
        print("Это не треугольник")


triangle(1, 1, 2)