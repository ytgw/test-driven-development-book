class TestCase:
    name: str

    def __init__(self, name: str) -> None:
        self.name = name

    def setUp(self) -> None:
        pass

    def run(self) -> None:
        self.setUp()
        method = getattr(self, self.name)
        method()


class WasRun(TestCase):
    wasRun: bool = False
    wasSetUp: bool = False

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
