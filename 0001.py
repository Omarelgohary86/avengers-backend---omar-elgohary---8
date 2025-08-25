import datetime
class info :
    def __init__(self,first_name,last_name,GPA,birth_date):
        self.first_name = first_name
        self.last_name = last_name
        self.GPA = GPA
        self.birth_date = birth_date

    def display(self):
        print(f"name : {self.first_name} {self.last_name}")
        print(f"GPA : {self.GPA}")
        print(f"birth date : {self.birth_date}")
        print(f"age : {datetime.datetime.now().year - self.birth_date}")
        

user1=info("omar","elgohary",3.85,2005)
user1.display()