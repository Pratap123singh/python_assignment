class employee:
    company_name="TCS"              #class variable
    def __init__(self,emp_id,emp_name, emp_designation, emp_salary, emp_project_id_assigned, emp_skills):
        self.emp_id=emp_id                                      #instance variable
        self.emp_name=emp_name                                  #instance variable
        self.emp_designation=emp_designation                    #instance variable
        self.__emp_salary=emp_salary                            #data hiding/Private variable
        self.emp_project_id_assigned=emp_project_id_assigned    #instance variable
        self.emp_skills=emp_skills                              #instance variable
        

    def display_project_ids(self):
        print("Employee Name: ",self.emp_name,"   Project id: ", self.emp_project_id_assigned)
    
    def display_identity(self):
        print("Details of employee: ", self.emp_id, self.emp_name)

    def check_relevant_skills(self):
        #print(self.emp_skills)
        if 'Python' in self.emp_skills:
            print(f"Emploee Id: {self.emp_id}, Employee name: {self.emp_name}, Employee Skill: {self.emp_skills}")
            
    
    def emp_sal(self):
        print(f"Employee Salary: {self._employee__emp_salary}")

    @classmethod
    def display_company_details(cls):
        print("Company Name: ", cls.company_name)


emp1=employee(1111,"Paras", "MD", 15000000,{'Walgreens','PwC','P&G'},['Management','Operations'])
emp2=employee(2222,"Rohan", "Product Manager", 150000,{'L&T','KPMG','P&G'},['Management','Python','Operations'])
emp3=employee(3333,"Rashmi", "TL", 15000,{'Bell Laboratories','PwC','IBM'},['C++','Python', 'Java'])
# l=[]
# for i in range(0,3,1):
#     id=input("Enter employee id: ")
#     name=input("Enter employee name: ")
#     designation=input("Enter designation: ")
#     sal=input("Enter employee salary: ")
#     projects=input("Enter comma separated employee projects: ")
#     _projects=set(projects.split(","))
#     skill=list(input("Enter comma separated skills: "))
#     _skill=list(projects.split(","))
#     e=employee(id,name,designation,sal,_projects,_skill)
#     l.append(e)

#print(l)

#for i in range(0,3,1):
    #l[i].display_identity()
    #l[i].display_company_details()
    #l[i].display_project_ids()
    #print("emloyee with python skill: ", l[i].check_relevant_skills())
    #l[i].emp_sal()

emp1.check_relevant_skills()
emp2.check_relevant_skills()
emp3.check_relevant_skills()