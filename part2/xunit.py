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
    test: WasRun

    def setUp(self) -> None:
        self.test = WasRun("testMethod")

    def testRunning(self) -> None:
        self.test.run()
        assert(self.test.wasRun)

    def testSetUp(self) -> None:
        self.test.run()
        assert(self.test.wasSetUp)


if __name__ == "__main__":
    TestCaseTest("testRunning").run()
    TestCaseTest("testSetUp").run()
