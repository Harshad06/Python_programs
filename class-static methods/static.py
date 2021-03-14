
class student():
    def __init__(self,mark):
        self.mark=mark
    
    @staticmethod
    def find_min(mark):
        return min(mark,100)

print(student.find_min(20))


# @static method decorator
# Static method is used to call function/property without 
# instantiating the class first.
# 
#  Static methods can also be accessed via class instances/or objects.