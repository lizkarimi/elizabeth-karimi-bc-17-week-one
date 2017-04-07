class school_members(object):
    name = ""

    def __init__(self, name):
        self.name = name
    def have_school_access(self):
        print "Hello, welcome to school " + self.name




class staff(school_members):
    def have_staffroom_access(self): #cant be accessed by any other school member other than staff
        print self.name + ", welcome to staffroom"
    def stay(self):
        print self.name + " stays in the staff quarters"


class student(school_members):
    def no_staffroom_access(self):
        print self.name + ", you are not allowed in staffroom"

    def stay(self):
        print self.name + " stays in the dormitories"
