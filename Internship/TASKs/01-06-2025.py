""" Write a Python program that takes marks of 5 subjects from the user (as integers).
Each mark must be between 0 and 100 inclusive. After validating all 5 inputs, 
the program should calculate the total and percentage of the marks Write a Python program that takes marks of 5 subjects from the user (as integers). Each mark must be between 0 and 100 inclusive. After validating all 5 inputs, the program should calculate the total and percentage of the marks.

The passing mark for each subject is 40.
If more than 2 subjects have marks less than 40, the student is FAILED.
If only 1 or 2 subjects are below 40, the result is ATKT (Allowed to Keep Term) and the percentage should not be displayed.

If all subjects have 40 or more, then:
Calculate the percentage and assign a grade:
A Grade: percentage ≥ 75
B Grade: percentage ≥ 60 and < 75
C Grade: percentage ≥ 40 and < 60
Use only if, elif, and else statements."""

print("Enter marks for sub1 :")
S1 = int(input())

print("Enter marks for sub2 :")
S2 = int(input())

print("Enter marks for sub3 :")
S3 = int(input())

print("Enter marks for sub4 :")
S4 = int(input())

print("Enter marks for sub5 :")
S5 = int(input())

Total = S1 + S2 + S3 + S4 + S5
Fail_count = 0
# Check for invalid input
if((S1 < 0 or S2 > 100) or (S2 < 0 or S2 > 100) or (S3 < 0 or S3 > 100) or(S4 < 0 or S4 > 100) or (S5 < 0 or S5 > 100) ):
    print("invalid input")
else:
   
    if S1 < 40:
        Fail_count += 1
    if S2 < 40:
        Fail_count += 1
    if S3 < 40:
        Fail_count += 1
    if S4 < 40:
     Fail_count += 1
    if S5 < 40:
        Fail_count += 1

    if Fail_count > 2:
        print("\nFAILED")
    elif Fail_count >= 2:
        print("ATKT")
    else:
        print(f"Total is {Total}")
        percentage = Total / 5
        print(f"Percentage is {percentage}")

if percentage >= 75 :
    print("A Grade")
elif percentage >= 60 and percentage <=75:
    print("B Grade")
elif percentage >= 40 and percentage <= 60:
    print("Grade C")
else:
    print("Student is Failed")

print("Enter marks for sub1 :")
S1 = int(input())

print("Enter marks for sub2 :")
S2 = int(input())

print("Enter marks for sub3 :")
S3 = int(input())

print("Enter marks for sub4 :")
S4 = int(input())

print("Enter marks for sub5 :")
S5 = int(input())

Total = S1 + S2 + S3 + S4 + S5
Fail_count = 0
# Check for invalid input
if((S1 < 0 or S2 > 100) or (S2 < 0 or S2 > 100) or (S3 < 0 or S3 > 100) or(S4 < 0 or S4 > 100) or (S5 < 0 or S5 > 100) ):
    print("invalid input")
else:
   
    if S1 < 40:
        Fail_count += 1
    if S2 < 40:
        Fail_count += 1
    if S3 < 40:
        Fail_count += 1
    if S4 < 40:
     Fail_count += 1
    if S5 < 40:
        Fail_count += 1

    if Fail_count > 2:
        print("\nFAILED")
    elif Fail_count >= 2:
        print("ATKT")
    else:
        print(f"Total is {Total}")
        percentage = Total / 5
        print(f"Percentage is {percentage}")

if percentage >= 75 :
    print("A Grade")
elif percentage >= 60 and percentage <=75:
    print("B Grade")
elif percentage >= 40 and percentage <= 60:
    print("Grade C")
else:
    print("Student is Failed")