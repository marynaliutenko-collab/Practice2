def fibonacci(p):
    a = 0
    b = 1
    if p < 0:
        return 0

    if p == 0:
        return 1
    else:
          while b <= p:
               a, b = b, a + b
          return b
