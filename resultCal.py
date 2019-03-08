import pandas as pd
class ResultCalculator:
    
    def __init__(self,last_unit, cgpa, course_title, course_codes, units, grades):
        self.course_info = {}
        self.a,self.b,self.c,self.d,self.f = 5,4,3,1,0
        self.course_title = course_title
        self.courses = course_codes
        self.units = units
        self.grades = grades
        self.last_unit =last_unit
        self.carry_over = []
        self.last_cgpa = cgpa
        self.course_info['course_title'] = self.course_title
        self.course_info['courses'] = self.courses
        self.course_info['units'] = self.units
        self.course_info['grades'] = self.grades
        self.Calculator()
        
    def Calculator(self):
        grade = []
        counter = 0
        self.result = 0
        self.unit = 0
        for i in self.units:
            self.unit += int(i)
            if self.grades[counter].lower()=="a" :
                grade.append(int(i) * self.a)
            elif self.grades[counter].lower()=="b":
                grade.append(int(i) * self.b)
            elif self.grades[counter].lower()=="c":
                grade.append(int(i) * self.c)
            elif self.grades[counter].lower()=="d":
                grade.append(int(i) * self.d)
            elif self.grades[counter].lower()=="f":
                grade.append(int(i) * self.f)
                self.carry_over.append(self.courses[counter])
            counter += 1
        for r in grade:
            self.result += int(r)
        self.course_info['GPA'] = grade
            
        self.gpa = self.result/self.unit
        self.cgpaCalculator()


    def cgpaCalculator(self):
        cgpas = int(self.last_unit) * float(self.last_cgpa)
        self.current_cgpa = float(self.result) + float(cgpas)
        self.total_units = int(self.last_unit) + int(self.unit)
        print('CGpa: ',str(self.current_cgpa))
        print('Total score: ',self.current_cgpa)
        print('units: ',self.total_units)
        self.confirmed_cgpa = float(self.current_cgpa) / int(self.total_units)
        r = pd.DataFrame(self.course_info ,
                         columns = ['courses','course_title','units','grades','GPA'])
        print(r)
        print("GPA: "+str(round(self.gpa,2)))
        print("CGPA: ",str(round(self.confirmed_cgpa,2)))
        print("CO: ", str(len(self.carry_over)))

    
