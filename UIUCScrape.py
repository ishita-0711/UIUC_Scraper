import uiuc_api as ua

#Get course number, name, credits and description
def getCourse(courseName, year=None, quarter=None, redirect=False):
    course = ua.get_course(courseName, year, quarter, redirect)
    return course.number, course.name, course.hours, course.description
