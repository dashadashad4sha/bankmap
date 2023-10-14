import json
from math import sqrt


def calculate_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def count_users_by_coordinates(json_user_data, json_bank_data):
    coordinates_count = {}

    b_data = json.loads(json_bank_data)
    u_data = json.loads(json_user_data)

    for user in u_data:
        u_coordinates = user['coordinates']
        for bank in b_data:
            b_coordinates = bank['coordinates']
            distance = calculate_distance(u_coordinates, b_coordinates)
            if distance < 0.01:
                if bank['id'] not in coordinates_count:
                    coordinates_count[bank['id']] = 1
                else:
                    coordinates_count[bank['id']] += 1
    return coordinates_count


bank_data = '''
[
    {"id": 1, "coordinates": [55.686137, 37.849832]},
    {"id": 2, "coordinates": [55.745726, 37.625702]},
    {"id": 3, "coordinates": [55.646284, 37.737542]},
    {"id": 4, "coordinates": [55.67226, 37.595707]},
    {"id": 5, "coordinates": [55.799955, 37.619221]}
]
'''
json_data = '''
[
    {"id": 1, "coordinates": [55.7999, 37.61921]},
    {"id": 2, "coordinates": [55.79949, 37.6194521]},
    {"id": 3, "coordinates": [55.7955599, 37.6194521]},
    {"id": 5, "coordinates": [55.795499, 37.6194421]},
    {"id": 6, "coordinates": [55.672246, 37.595707]},
    {"id": 7, "coordinates": [55.67266, 37.595707]},
    {"id": 8, "coordinates": [55.67266626, 37.595707]},
    {"id": 9, "coordinates": [55.67, 37.5957]},
    {"id": 10, "coordinates": [55.6722677, 37.595707]}
]
'''

result = count_users_by_coordinates(json_data, bank_data)
print(result)
