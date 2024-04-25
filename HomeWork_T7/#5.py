from functools import reduce

def calculate_area(rooms):
    return reduce(lambda x, y: x + y['length'] * y['width'], rooms, 0)

rooms = [
    {"name": "Kitchen", "length": 6, "width": 4},
    {"name": "Room 1", "length": 5.5, "width": 4.5},
    {"name": "Room 2", "length": 5, "width": 4},
    {"name": "Room 3", "length": 7, "width": 6.3},
]

print('Площадь квартиры',calculate_area(rooms), 'м.кв')