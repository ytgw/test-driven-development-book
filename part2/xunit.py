class TestCase:
    name: str

    def __init__(self, name: str):
        self.name = name

    def run(self):
        method = getattr(self, self.name)
        method()


class TestCaseTest(TestCase):
    def testRunning(self):
        test = WasRun("testMethod")
        assert(not test.wasRun)
        test.run()
        assert(test.wasRun) 


class WasRun(TestCase):
    wasRun: bool

    def __init__(self, name: str):
        self.wasRun = False
        super().__init__(name)

    def testMethod(self):
        self.wasRun = True

if __name__ == "__main__":
    TestCaseTest("testRunning").run()
