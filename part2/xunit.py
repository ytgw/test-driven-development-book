class TestCase:
    name: str

    def __init__(self, name: str) -> None:
        self.name = name

    def run(self) -> None:
        method = getattr(self, self.name)
        method()


class TestCaseTest(TestCase):
    def testRunning(self) -> None:
        test = WasRun("testMethod")
        assert(not test.wasRun)
        test.run()
        assert(test.wasRun) 


class WasRun(TestCase):
    wasRun: bool

    def __init__(self, name: str) -> None:
        self.wasRun = False
        super().__init__(name)

    def testMethod(self) -> None:
        self.wasRun = True


if __name__ == "__main__":
    TestCaseTest("testRunning").run()
