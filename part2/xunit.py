class TestCase:
    name: str

    def __init__(self, name: str) -> None:
        self.name = name

    def run(self) -> None:
        method = getattr(self, self.name)
        method()


class WasRun(TestCase):
    wasRun: bool
    wasSetUp: bool

    def __init__(self, name: str) -> None:
        self.wasRun = False
        self.wasSetUp = False
        super().__init__(name)

    def setUp(self) -> None:
        self.wasSetUp = True

    def testMethod(self) -> None:
        self.wasRun = True


class TestCaseTest(TestCase):
    def testRunning(self) -> None:
        test = WasRun("testMethod")
        assert(not test.wasRun)
        test.run()
        assert(test.wasRun)

    def testSetUp(self) -> None:
        test = WasRun("testMethod")
        test.run()
        assert(test.wasSetUp)


if __name__ == "__main__":
    TestCaseTest("testRunning").run()
    TestCaseTest("testSetUp").run()
