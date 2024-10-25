class TestCase:
    name: str

    def __init__(self, name: str):
        self.name = name

    def run(self):
        method = getattr(self, self.name)
        method()


class WasRun(TestCase):
    wasRun: bool

    def __init__(self, name: str):
        self.wasRun = False
        super().__init__(name)

    def testMethod(self):
        self.wasRun = True


test = WasRun("testMethod")
print(test.wasRun)
test.run()
print(test.wasRun)
