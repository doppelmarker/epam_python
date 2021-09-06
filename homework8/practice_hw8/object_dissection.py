class C:
    cls_attr = 10

    def __init__(self, name):
        a = 1
        self.a = a
        self.name = name

    def hello(self):
        print("test")

    @classmethod
    def foo(cls):
        print("foo")

    @staticmethod
    def staticmethod():
        print("staticmethod")


x = C("abc")
print(C.__init__)
print()
print(C.hello)
print()
print(C.foo)
print()
print(C.staticmethod)
print()
print(C.__dict__)
print()
print()
print(x.__init__)
print()
print(x.hello)
print()
print(x.foo)
print()
print(x.staticmethod)
print()
print(x.__dict__)
