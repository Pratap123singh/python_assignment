class course:
    agency_creating_course="CDAC"       #class variable
    def __init__(self, course_id, course_name, duration, total_hours_of_syllabus, contents, staff_count):
        self.course_id=course_id                                #instance variable
        self.course_name=course_name                            #instance variable
        self.duration=duration                                  #instance variable
        self.total_hours_of_syllabus=total_hours_of_syllabus    #instance variable
        self.contents=contents                                  #instance variable
        self.staff_count=staff_count                            #instance variable

    def display_info(self):                                     #instance method
        print(self.course_id,self.course_name, self.duration, self.total_hours_of_syllabus, self.contents, self.staff_count)
    @classmethod
    def display_agency(cls):                                    #class method
        print(cls.agency_creating_course)

obj1 = course('1002', 'DBDA', '6','600 hours',"pyhton, java, os, etc",'23')
obj1.display_info()                 #1002 DBDA 6 600 hours pyhton, java, os, etc 23
obj1.display_agency()               #CDAC

