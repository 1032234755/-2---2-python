
import numpy as np

# Коэффициенты уравнений прямых (Ax + By + C = 0 и Dx + Ey + F = 0)
A1, B1, C1 = 1, -2, 1
A2, B2, C2 = -1, -1, -2

# Заданная точка
x0, y0 = 3, 2

# Функция для вычисления расстояния от точки до прямой
def distance_point_line(A, B, C, x0, y0):
    return abs(A * x0 + B * y0 + C) / np.sqrt(A**2 + B**2)

# Расстояние от точки до первой прямой
distance1 = distance_point_line(A1, B1, C1, x0, y0)
print(f"Расстояние от точки до первой прямой = {distance1:.4f}")

# Расстояние от точки до второй прямой
distance2 = distance_point_line(A2, B2, C2, x0, y0)
print(f"Расстояние от точки до второй прямой = {distance2:.4f}")

# Нахождение точки пересечения прямых
def intersection_point(A1, B1, C1, A2, B2, C2):
    D = A1 * B2 - A2 * B1
    if D == 0:
        return None  # Прямые параллельны или совпадают
    x = (B1 * C2 - B2 * C1) / D
    y = (A2 * C1 - A1 * C2) / D
    return (x, y)

intersection = intersection_point(A1, B1, C1, A2, B2, C2)
if intersection:
    x_inter, y_inter = intersection
    print(f"Точка пересечения прямых: ({x_inter:.4f}, {y_inter:.4f})")
else:
    print("Прямые параллельны или совпадают.")

# Расстояние от заданной точки до точки пересечения прямых
if intersection:
    distance_to_intersection = np.sqrt((x0 - x_inter)**2 + (y0 - y_inter)**2)
    print(f"Расстояние от заданной точки до точки пересечения прямых = {distance_to_intersection:.4f}")

# Угол между прямыми
def angle_between_lines(A1, B1, A2, B2):
    cos_theta = (A1 * A2 + B1 * B2) / (np.sqrt(A1**2 + B1**2) * np.sqrt(A2**2 + B2**2))
    angle_rad = np.arccos(np.clip(cos_theta, -1.0, 1.0))
    angle_deg = np.degrees(angle_rad)
    return angle_deg

angle = angle_between_lines(A1, B1, A2, B2)
print(f"Угол между прямыми = {angle:.4f} градусов")
