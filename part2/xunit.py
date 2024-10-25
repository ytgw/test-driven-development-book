class TestResult:
    runCount: int
    errorCount: int

    def __init__(self) -> None:
        self.runCount = 0
        self.errorCount = 0

    def testStarted(self) -> None:
        self.runCount += 1

    def testFailed(self) -> None:
        self.errorCount += 1

    def summary(self) -> str:
        return f"{self.runCount} run, {self.errorCount} failed"


class TestCase:
    name: str

    def __init__(self, name: str) -> None:
        self.name = name

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def run(self, result: TestResult) -> None:
        result.testStarted()
        self.setUp()
        try:
            method = getattr(self, self.name)
            method()
        except Exception as e:
            result.testFailed()
            print(f"{self.name} raise an exception: {e}")
        self.tearDown()


class TestSuite:
    tests: list[TestCase] = []

    def __init__(self) -> None:
        self.tests = []

    def add(self, test: TestCase) -> None:
        self.tests.append(test)

    def run(self, result: TestResult) -> None:
        for test in self.tests:
            test.run(result)


class WasRun(TestCase):
    log: str = ""

    def setUp(self) -> None:
        self.log += "setUp "

    def testMethod(self) -> None:
        self.log += "testMethod "

    def testBrokenMethod(self) -> None:
        raise Exception

    def tearDown(self) -> None:
        self.log += "tearDown "


class TestCaseTest(TestCase):
    def testTemplateMethod(self) -> None:
        test = WasRun("testMethod")
        result = TestResult()
        test.run(result)
        assert("setUp testMethod tearDown " == test.log)

    def testResult(self) -> None:
        test = WasRun("testMethod")
        result = TestResult()
        test.run(result)
        assert("1 run, 0 failed" == result.summary())

    def testFailedResult(self) -> None:
        test = WasRun("testBrokenMethod")
        result = TestResult()
        test.run(result)
        assert("1 run, 1 failed" == result.summary())

    def testFailedResultFormatting(self) -> None:
        result = TestResult()
        result.testStarted()
        result.testFailed()
        assert("1 run, 1 failed" == result.summary())

    def testSuite(self) -> None:
        suite = TestSuite()
        suite.add(WasRun("testMethod"))
        suite.add(WasRun("testBrokenMethod"))
        result = TestResult()
        suite.run(result)
        assert("2run, 1 failed" == result.summary())


if __name__ == "__main__":
    result = TestResult()
    TestCaseTest("testTemplateMethod").run(result)
    TestCaseTest("testResult").run(result)
    TestCaseTest("testFailedResult").run(result)
    TestCaseTest("testFailedResultFormatting").run(result)
    TestCaseTest("testSuite").run(result)
    print(result.summary())