class Example:
    def __init__(self):
        self.a = "Parent Class"
        print("I'm Initiated")

    def sample(self):
        print("sample method")


class Sample(Example):
    def __init__(self):
        super().__init__()


    def sample(self):
        print("sample method")



a = Sample()