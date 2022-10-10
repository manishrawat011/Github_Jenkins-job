
class A:
    def __init__(self):
        print("Feature of A: constractor")

    def feature1(self):
        print("Feature 1 : is working")

    def feature2(self):
        print("Feature 2: is working")


class B(A):
    def __init__(self):
        super().__init__()  #if you want the init method of both A/b use this;.
        # super(B, self).__init__()
        print("Feature of B: constractor")

    def feature3(self):
        print("Feature 3 : is working")

    def feature4(self):
        print("Feature 4: is working")


a1 = B()
# a1.feature4()