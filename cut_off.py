import re
for x in range (5):
    # Cgpa = input("Your CGPA: ")
    # Gpa = input("Your GPA: ")
    cut_of_mark = {
                "CGPA" : [range(3.0, 5.0)],
                "GPA" : [range(3.0, 5.0)] 
                } 
    # check_cgpa = re.search(str(Cgpa, cut_of_mark["CGPA"]))
    # print(check_cgpa)
    print(cut_of_mark)