
# Multi-Level Inheritance

class A():
    def __init__(self, fname):
        self.fname = fname

class B(A):
    def __init__(self, mname):
        self.mname = mname
        super().__init__('First')

class C(B):
    def __init__(self, lname):
        self.lname = lname
        super().__init__('Middle')

obj = C('Last')
print(obj.fname, obj.mname, obj.lname)
