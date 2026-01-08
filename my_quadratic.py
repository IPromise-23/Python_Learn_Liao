import math
def my_quadratic(a, b, c):
    # 先做类型检查
    if not all(isinstance(v, (int, float)) for v in (a, b, c)):
    #isinstance 只接受两个参数（对象，类型或类型元组
        raise TypeError('bad operand type')
    # a 为 0 时不是二次方程
    if a == 0:
        return None
    delta = b**2 - 4*a*c
    if delta < 0:
        return None
    elif delta == 0:
        x = -b / (2*a)
        return x
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return x1, x2
# ...existing code...
# print(my_quadratic(1, -3, 2))  # Should output (2.0, 1.0)
# print(my_quadratic(0, 2, 1))   # Should output None