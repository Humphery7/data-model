class CGPA:
    
    total,cgpa,total_units = (0,0,0)
    
    def __init__(self,name,department,faculty,institutionGPA):
        self.name = name
        self.department = department
        self.faculty = faculty
        self.GPA = institutionGPA
    
    def courses(self,num_courses):
        courses = []
        units = []
        result = []
        for i in range(num_courses):
            course = input("input the next course : ")
            unit_of_course = int(input("enter the unit of this course"))
            result_of_course = int(input("enter the result of this course"))
            courses.append(course)
            units.append(unit_of_course)
            result.append(result_of_course)

            @staticmethod
            def calculate_cgpa():
                total_units = sum(units)
                for i in result:
                    if 70 <= i <= 100:
                        total += (5*units[i])
                    elif 60 <=i < 70:
                        total += (4*units[i]) 
                    
                    elif 50 <=i < 60:
                        total += (3*units[i])
                    
                    elif 45 <=i < 50:
                        total += (2*units[i])
                    
                    elif 40 <=i < 45:
                        total += (1*units[i])
                    
                    elif 0 <=i < 40:
                        total += (0*units[i])
                    else:
                        print('not a possible result')
                        exit()

                cgpa = round(total/total_units,2) 
                return f'This is your CGPA for this Semester, {cgpa}'
            calculate_cgpa()
Student1 = CGPA('ufuoma','elect/elect','technology',5)

print(Student1.courses(8))





