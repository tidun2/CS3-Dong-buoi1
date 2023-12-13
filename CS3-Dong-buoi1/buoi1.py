students = [
    {"maSV": 3432,
     "name": "Van A",
     "math": 8,
     "lit": 3,
     "chem": 4},
    {"maSV": 3433,
     "name": "Van B",
     "math": 5,
     "lit": 3,
     "chem": 0},
    {"maSV": 3434,
     "name": "Van C",
     "math": 4,
     "lit": 1,
     "chem": 4},
    {"maSV": 3435,
     "name": "Van D",
     "math": 7,
     "lit": 8,
     "chem": 9},
    {"maSV": 3436,
     "name": "Van E",
     "math": 8,
     "lit": 9,
     "chem": 9},
]


def tinhTB(a, b, c):
    return (a+b+c)/3


for student in students:
    score = tinhTB(student["math"], student["chem"], student["lit"])
    if score > 5:
        print(f"Sinh viên {student['name']} có điểm TB {score}")
    if student['chem'] < 5:
        print(student)
