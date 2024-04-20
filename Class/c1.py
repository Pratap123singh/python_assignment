class employee:
    
    def __init__(self,empid:int,name:str,designation:str,salary:int,project_ids_assigned:set,skills:list):
        self.empid=empid
        self.name=name
        self.designation=designation
        self.__salary=salary
        self.project_ids_assigned=project_ids_assigned 
        self.skills=skills
        employee.company_name="BlackRock Pvt Ltd"

    def display_projetids(self):
        print(self.project_ids_assigned)
    def display_identity(self):
        print(self.empid,self.name)
    def check_relevant_skill(self,skill1):
        #print("self.skill: ", self.skills)
        #print("skill1: ", skill1)
        if skill1 in self.skills.lower():
            return True
        else:
            return False
    @classmethod
    def display_company_details(cls):
        print(cls.company_name)
    

emp1=employee(1,"Yulia","Marketing Manager",25000,{101,203,201},"Marketing, Python")
emp2=employee(2,"James","HR Manager",26000,{102,203,401},"HR, Java")
emp3=employee(3,"Martin","Finance Manager",27000,{103,102,203,401},"Finance, Python")


emp1.display_identity()
emp2.display_identity()
emp3.display_identity()
emp1.display_projetids()
emp2.display_projetids()
emp3.display_projetids()
emp1.display_company_details()
print("-------------------------------------------------------------------------------------")
ll=[emp1,emp2,emp3]
for e in ll:
    v=e.check_relevant_skill("python")
    #print("v: ", v)
    if v==True:
        e.display_identity()
for e in ll:
    print(e._employee__salary)
    