class A:
    X = 100
    @classmethod
    def a(self):
        print(self.X)
    def __getattribute__(self, __name: str):
        print('ger attribute')
        return super().__getattribute__(__name)
    
a = A()

A.a()