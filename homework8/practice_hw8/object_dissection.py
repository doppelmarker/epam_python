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
        pass


x = C("abc")
print(C.foo)
print(C.__init__)
print(C.hello)
print(x.hello)
print(x.foo)
print(x.__dict__)
print(x.__class__.__dict__)
