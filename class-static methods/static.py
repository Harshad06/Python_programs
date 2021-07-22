
class Student():
    def __init__(self, mark):
        self.mark=mark
    
    @staticmethod
    def find_min(mark):
        return min(mark,100)
        
print(Student.find_min(20))


# @static method decorator
# Static method is used to call function/property without instantiating the class first.
# Static methods can also be accessed via class instances/or objects.

# Whenever a class is instantiated "__new__" and "__init__" methods are called. 
# "__new__" method will be called when an object is created and "__init__" method will be called to initialize the object.