class Emp:
    def __init__(self, id, name, salary) -> None:
        self.id = id
        self.name = name
        self.sal = salary
    def displayEmpInfo(self):
        print(f" Name = {self.name}, ID = {self.id}, Salary = {self.sal}")
