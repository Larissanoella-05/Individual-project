from gradebook_ALU import GradeBook


gradebook_ALU = GradeBook()

while True:
    print("Welcome to Larissa's Grade Book Application!")
    print("Please choose an action:")
    print("1. Add a student")
    print("2. Add a course")
    print("3. Register a student for a course")
    print("4. Calculate student ranking")
    print("5. Search by grade")
    print("6. Generate transcript")
    print("7. Print student list")
    print("8. Print course list")
    print("9. Exit")

    choice = input("Enter your choice (1-9): ")

    if choice == "1":
        email = input("Enter student email: ")
        names = input("Enter student names: ")
        student = gradebook_ALU.add_student(email, names)

    elif choice == "2":
        name = input("Enter course name: ")
        trimester = input("Enter course trimester: ")
        credits = int(input("Enter course credits: "))
        course = gradebook_ALU.add_course(name, trimester, credits)

    elif choice == "3":
        email = input("Enter student email: ")
        student = next(
            (s for s in gradebook_ALU.student_list if s.email == email), None)
        if student:
            name = input("Enter course name: ")
            course = next(
                (c for c in gradebook_ALU.course_list if c.name == name), None)
            if course:
                gradebook_ALU.register_student_for_course(student, course)
                print('-----------------------------------------------------')
                print(f"{student.names} registered for {
                      course.name} successfully.")
                print('----------------------------------------------------')
              
            else:
                print("Course not found.")
        else:
            print("Student not found.")

    elif choice == "4":
        gradebook_ALU.calculate_GPA()
        gradebook_ALU.calculate_ranking()
        print("Student ranking calculated successfully.")

    elif choice == "5":
        min_grade = float(input("Enter minimum grade: "))
        max_grade = float(input("Enter maximum grade: "))
        students = gradebook_ALU.search_by_grade((min_grade, max_grade))
        if students:
            print("Students found:")
            for student in students:
                print(f"- {student.names} ({student.email})")
        else:
            print("No students found within the specified grade range.")

    elif choice == "6":
        email = input("Enter student email: ")
        student = next(
            (s for s in gradebook_ALU.student_list if s.email == email), None)
        if student:
            gradebook_ALU.generate_transcript(student)
        else:
            print("Student not found.")

    elif choice == "7":
            print("Printing student list...")
            print('-----------------------------------------')
            for student in gradebook_ALU.student_list:
                print(f"- {student.names} ({student.email})")
            print('-----------------------------------------')
            break

    elif choice == "8":
            print("Printing course list...")
            print('-----------------------------------------')
            for course in gradebook_ALU.course_list:
                print(
                    f"- {course.name} ({course.trimester}) - {course.credits} credits")
            print('-----------------------------------------')
            break

    elif choice == "9":
            print("Exiting Grade Book Application...")
            break

    else:
        print("Invalid choice. Please try again.")
