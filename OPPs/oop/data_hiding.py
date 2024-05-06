#Data Hiding

class tcs:
    def __init__(self, emp_name, emp_id):
        self.emp_name=emp_name                  #instance variable
        self.emp_id=emp_id                      #instance variable
        self.__emp_moble_no = '123456789'        #hidden
    
t=tcs('Rohit', '1001')
print(t.emp_name)
print(t.emp_id)
# print(t.__emp_moble_no)   #AttributeError: 'tcs' object has no attribute '__emp_moble_no'.?
print(t._tcs__emp_moble_no)     #to see hidden data obj._ClassName__VarName

