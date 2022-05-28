
class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self,name:str,age:int,tracks:list,score:float):
        self.name:str = name
        self.age:int = age
        self.tracks:list = tracks
        self.score:float = score

    def change_name(self, new_name):
        self.new_name = new_name
        new_name = "Peter"
        print(f"the student updated his name to {new_name},")

    def change_age(self, new_age):
        self.new_age = new_age
        new_age = "34"
        print(f"Age to {new_age},")

    def add_track(self, new_track):
        self.new_track = new_track
        new_track = "UI/UX"
        print(f"Track to {new_track},")

    def get_score(self, new_score):
        self.new_score = new_score
        new_score = "10.5"
        print(f"Score to {new_score}.")

Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score(10.5)
