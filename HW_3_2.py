HEIGHT = 3000
WIRE_WEIGHT = {3: 0.056, 4: 0.099, 5: 0.154, 2: 0.0247, 1: 0.0062}
length = input("Enter length ")
if length.isdigit() or length.endswith('mm'):
    multiplier_l = 1
elif length.endswith('cm'):
    multiplier_l = 10
elif length.endswith('m'):
    multiplier_l = 1000
mesh_edge = input("Enter mesh cell size ")
if mesh_edge.endswith('cm'):
    multiplier_m = 10
else:
    multiplier_m = 1
length_mm = int(length.strip('cm')) * multiplier_l
mesh_edge_mm = int(mesh_edge.strip('cm')) * multiplier_m
wire_diameter = int(input('Enter wire diameter in mm '))
wire_length = 2 * length_mm / mesh_edge_mm * HEIGHT * 2 / 3 ** 0.5
wire_length_m = wire_length / 1000
from decimal import Decimal
x = Decimal(wire_length_m * WIRE_WEIGHT[wire_diameter])
x = x.quantize(Decimal('1.000'))
print(f'You need', x, 'kg of 'f'wire {wire_diameter} mm in diameter')