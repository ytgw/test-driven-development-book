class WasRun:
    wasRun: bool

    def __init__(self, name: str):
        self.wasRun = False

    def testMethod(self):
        pass

test = WasRun("testMethod")
print(test.wasRun)
test.testMethod()
print(test.wasRun)
