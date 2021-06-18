
# Multiple Inheritance   [Diamond problem]

class A:
    def m(self):
        print("In Class A")

class B(A):
    def m(self):
        print("In Class B")


class C(A):
    def m(self):
        print("In Class A")

class D(B,C):
    pass

obj = D()
obj.m()             # In Class B

# print(D.mro())    # [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
