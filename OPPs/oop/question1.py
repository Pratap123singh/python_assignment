class employee:
    def __init__(self, emp_id: int, emp_name: str, project_id: set, project_name: list):
        self.emp_id=emp_id
        self.emp_name=emp_name
        self.project_id=project_id
        self.project_name=project_name
    
    def display(self):
        print(f"{self.emp_id}, {self.emp_name}, {self.project_id}, {self.project_name}")

# l=list()
# for idx in range(0,2,1):
#     id=int(input("Enter emp_id: "))
#     name=input("Enter name: ")
#     projectID=int(input("enter a project id: "))
#     projectName=int(input("enter a project name: "))

emp1=employee(1,'paras',{1,2,3,5},['Walgreens', 'P&G', 'Coal India'])
emp1.display()
