class Example3():
    @staticmethod
    def hello():
        print('hello world')

    @classmethod
    def hello2(cls):
        print('Hello', cls.__name__)


Example3.hello()
ob4 = Example3
ob4.hello()
Example3.hello2()
ob4.hello2()
