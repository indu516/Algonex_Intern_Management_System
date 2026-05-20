# intern_management.py
for i in range(2):
    print(i+1)

    student_dict = {}
    student_dict['name'] = input("Enter your name: ")
    student_dict['cgpa'] = float(input("Enter your cgpa: "))
    student_dict['location'] = input("Enter your location: ")
    print(student_dict)

    projects = []
    proj1 = input("Enter your project name: ")
    proj2 = input("Enter your project name: ")
    projects.append(proj1)
    projects.append(proj2)                 #projects.extends(proj1,proj2)

    student_dict['projects']=projects
    print(student_dict)

    skills = set(input("Enter skills seperated by space:").split())     # set for unique skills
    print(skills)

    student_dict['skills']=skills
    student_dict["roll nno."]=2324150


# All students
for student in students:

    print(f"Student ID : {student['student_id']}")
    print(f"Name : {student['name']}")
    print(f"Role : {student['role']}")
    print(f"CGPA : {student['cgpa']}")

    print("Projects :")

    for project in student["projects"]:
        print("-", project)

    print("Skills :", student["skills"])

    # Eligibility Check
    if student["cgpa"] >= 7:
        print("Status : Eligible")
    else:
        print("Status : Need Improvement")

        print("=" * 40)
