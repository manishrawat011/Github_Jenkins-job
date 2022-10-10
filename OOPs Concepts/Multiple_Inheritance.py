# what is multiple inheritance?
# When a class is derived from more than one base class it is called multiple Inheritance

class A:
    def feature1(self):
        print("feature 1 is working")

    def feature2(self):
        print("Feature 2: is working")


class B:
    def feature3(self):
        print("Feature 3 : is working")

    def feature4(self):
        print("Feature 4: is working")


class C():
    def feature5(self):
        print("Feature 5: is working")


class D(A,B,C):
    def feature6(self):
        print("feature 6 : is wok")


D1 = D()
D1.feature4()
D1.feature5()
D1.feature3()