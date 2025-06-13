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

mark_list = []
# print("Enter 5 subjects marks :")
for i in range(5):
    mark = int(input(f"Enter marks for subject from 0 - 100:"))
    # if mark < 0 or mark >100:
    #     print("invalid marks")
    #     break
    # else:
    #     mark_list.append(mark)
print(mark_list)

Total = mark_list[0] + mark_list[1] + mark_list[2] + mark_list[3] + mark_list[4]
Fail_count = 0

if((mark_list[0] < 0 or mark_list[0] > 100) or (mark_list[1] < 0 or mark_list[1] > 100) or (mark_list[2] < 0 or mark_list[2] > 100) or(mark_list[3] < 0 or mark_list[3] > 100) or (mark_list[4] < 0 or mark_list[4] > 100) ):
    print("invalid input")




