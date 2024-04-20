class course:
    #agency_creating_course="CDAC" ---- class variable
    def __init__(self,course_id,course_name,duration,total_hours_of_syllabus,content,staff_count):
        self.course_id=course_id
        self.course_name=course_name
        self.duration=duration
        self.total_hours_of_syllabus=total_hours_of_syllabus
        self.content=content
        self.staff_count=staff_count
        course.agency_creating_course="CDAC"  #---- class variable
        
    def display_info(self):
        print(self.course_id,self.course_name,self.duration,self.total_hours_of_syllabus,self.content,self.staff_count)
        
    @classmethod
    def display_agency(cls):
        print(cls.agency_creating_course)

dbda=course(1,"dbda",6,900,"python, linux, cloud, sql,etc",20)
ditiss=course(2,"ditiss",6,900,"linux, cloud, OS, etc",20)

dbda.display_info()
dbda.display_agency()
ditiss.display_agency()
ditiss.display_info()

print(course.__dict__)
