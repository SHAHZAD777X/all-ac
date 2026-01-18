class Bird:
    def __init__(self):
        print("Its a Bird")
    def swim(self):
        print("Swim faster")

class flamingo(Bird):
    def __init__(self):
        super().__init__()
        print("its a flamingo")
    def migrate(self):
        print("Migratory bird")
obj1=flamingo()
obj1.migrate()
obj1.swim()