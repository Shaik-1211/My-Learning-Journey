# Heirarchical Inheritance
#            HUMAN
#            /  \
#           /    \
#         Male   Female

class Human:
    def __init__(self):
        self.eyes = 2
        self.nose = 1
        self.ears = 2
    
    def display(self):
        print(f"Human has {self.eyes} eyes")
        print(f"Human has {self.ears} ears")
        print(f"Human has {self.nose} nose")
        
#Male class is a sub class/inherited class of Human class
class Male(Human):
    def __init__(self):
        super().__init__()
        self.hair = "Short hair"
    
    def display(self):
        print(f"Male has {self.eyes} eyes")
        print(f"Male has {self.ears} ears")
        print(f"Male has {self.nose} nose")
        print(f"Male has {self.hair}")

#Female class is a sub class/inherited class of Human class
class Female(Human):
    def __init__(self):
        super().__init__()
        self.hair = "Long hair"
    
    def display(self):
        print(f"Female has {self.eyes} eyes")
        print(f"Female has {self.ears} ears")
        print(f"Female has {self.nose} nose")
        print(f"Female has {self.hair}")

human = Human()
human.display()
boy = Male()
#calls the display function in Female class but has attributes and methods of human class
boy.display()
girl = Female()
#calls the display function in Female class but has attributes and methods of human class
girl.display()
