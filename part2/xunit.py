class TestCase:
    name: str

    def __init__(self, name: str) -> None:
        self.name = name

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def run(self) -> None:
        self.setUp()
        method = getattr(self, self.name)
        method()
        self.tearDown()


class WasRun(TestCase):
    log: str = ""

    def setUp(self) -> None:
        self.log += "setUp "

    def testMethod(self) -> None:
        self.log += "testMethod "

    def tearDown(self) -> None:
        self.log += "tearDown "


class TestCaseTest(TestCase):
    def testTemplateMethod(self) -> None:
        test = WasRun("testMethod")
        test.run()
        assert("setUp testMethod tearDown " == test.log)

    def testResult(self) -> None:
        test = WasRun("testMethod")
        result = test.run()
        assert("1 run, 0 failed" == result.summary())


if __name__ == "__main__":
    TestCaseTest("testTemplateMethod").run()
    TestCaseTest("testResult").run()
