grade = lambda marks: "Pass" if marks >= 40 else "Fail"
marks_list = [85, 35, 72, 28, 40, 55]
for marks in marks_list:
    print(marks, ":", grade(marks))
    output:
85 : Pass
35 : Fail
72 : Pass
28 : Fail
40 : Pass
55 : Pass
