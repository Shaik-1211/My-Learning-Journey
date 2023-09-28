 #  "HYBRID INHERITANCE"
 #       UNIVERSITY
 #      /    \
 #     /      \
 #    /        \
 # COURSE      BRANCH
 #   \          /  \
 #    \        /    \
 #     \      /      \
 #      STUDENT     FACULTY

class University:
    def __init__(self,name,location):
        self.name = name
        self.location = location
    
    def display(self):
        print(f"Name of the university is {self.name}")
        print(f"Location of the university is {self.location}")

class Course(University):
    def __init__(self,name,location,course):
        super().__init__(name,location)
        self.course = course

    def display(self):
        print(f"Name of the university is {self.name}")
        print(f"Location of the university is {self.location}")
        print(f"Course choosen is {self.course}")

class Branch(University):
    def __init__(self,name,location,branch):
        super().__init__(name,location)
        self.branch  =branch

    def display(self):
        print(f"Name of the university is {self.name}")
        print(f"Location of the university is {self.location}")
        print(f"Branch choosen is {self.branch}")

class Student(Course,Branch):
    def __init__(self,name,location,course,branch,id):
        Course.__init__(self,name,location,course)
        Branch.__init__(name,location,branch)
        self.sutdent_id = id
    
    def display(self):
        print(f"Name of the university is {self.name}")
        print(f"Location of the university is {self.location}")
        print(f"Course choosen is {self.course}")
        print(f"Branch choosen is {self.branch}")
        print(f"Student id is {self.sutdent_id}")

class Faculty(Branch):
    def __init__(self,name,location,branch,faculty_name,dept):
        super().__init__(name,location,branch)
        self.faculty_name = faculty_name
        self.department = dept
    
    def display(self):
        print(f"Name of the university is {self.name}")
        print(f"Location of the university is {self.location}")
        print(f"Course choosen is {self.course}")
        print(f"Branch choosen is {self.branch}")
        print(f"Faculty name is {self.faculty_name}")
        print(f"{self.faculty_name} deals with {self.department}")

college = University("MIT","USA")
college.display()
course = Course("MIT","USA","Engineering")
course.display()
branch = Branch("MIT","USA","CSE")
branch.display()
std = Student("MIT","USA","Engineering","CSE",126)
std.display()
faculty = Faculty("MIT","USA","CSE","John Smith","Computer Science")
faculty.display()