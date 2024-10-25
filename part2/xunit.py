class WasRun:
    wasRun: bool

    def __init__(self, name: str):
        self.wasRun = False
        self.name = name

    def run(self):
        method = getattr(self, self.name)
        method()

    def testMethod(self):
        self.wasRun = True


test = WasRun("testMethod")
print(test.wasRun)
test.run()
print(test.wasRun)
