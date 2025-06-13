students = []
size = int(input("Enter number of students: "))
for i in range(1, size + 1):
    print(f"========== student {i} marks ==========")
    eng = input("Enter eng marks: ")
    maths = input("Enter maths: ")
    phy = input("Enter phy marks: ")
    students.append({
        'eng' : eng,
        'maths' : maths.title(),
        'phy' : phy.lower(),
    })
    for std in students:
    # Each "std" is a dictionary
        for key, value in std.items():
            print(f"{key.title()}: {value}")
    print("---------------------------")



