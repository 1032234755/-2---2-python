
import numpy as np

# ������������ ��������� ������ (Ax + By + C = 0 � Dx + Ey + F = 0)
A1, B1, C1 = 1, -2, 1
A2, B2, C2 = -1, -1, -2

# �������� �����
x0, y0 = 3, 2

# ������� ��� ���������� ���������� �� ����� �� ������
def distance_point_line(A, B, C, x0, y0):
    return abs(A * x0 + B * y0 + C) / np.sqrt(A**2 + B**2)

# ���������� �� ����� �� ������ ������
distance1 = distance_point_line(A1, B1, C1, x0, y0)
print(f"���������� �� ����� �� ������ ������ = {distance1:.4f}")

# ���������� �� ����� �� ������ ������
distance2 = distance_point_line(A2, B2, C2, x0, y0)
print(f"���������� �� ����� �� ������ ������ = {distance2:.4f}")

# ���������� ����� ����������� ������
def intersection_point(A1, B1, C1, A2, B2, C2):
    D = A1 * B2 - A2 * B1
    if D == 0:
        return None  # ������ ����������� ��� ���������
    x = (B1 * C2 - B2 * C1) / D
    y = (A2 * C1 - A1 * C2) / D
    return (x, y)

intersection = intersection_point(A1, B1, C1, A2, B2, C2)
if intersection:
    x_inter, y_inter = intersection
    print(f"����� ����������� ������: ({x_inter:.4f}, {y_inter:.4f})")
else:
    print("������ ����������� ��� ���������.")

# ���������� �� �������� ����� �� ����� ����������� ������
if intersection:
    distance_to_intersection = np.sqrt((x0 - x_inter)**2 + (y0 - y_inter)**2)
    print(f"���������� �� �������� ����� �� ����� ����������� ������ = {distance_to_intersection:.4f}")

# ���� ����� �������
def angle_between_lines(A1, B1, A2, B2):
    cos_theta = (A1 * A2 + B1 * B2) / (np.sqrt(A1**2 + B1**2) * np.sqrt(A2**2 + B2**2))
    angle_rad = np.arccos(np.clip(cos_theta, -1.0, 1.0))
    angle_deg = np.degrees(angle_rad)
    return angle_deg

angle = angle_between_lines(A1, B1, A2, B2)
print(f"���� ����� ������� = {angle:.4f} ��������")
