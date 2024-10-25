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
    result: TestResult

    def setUp(self) -> None:
        self.result = TestResult()

    def testTemplateMethod(self) -> None:
        test = WasRun("testMethod")
        test.run(self.result)
        assert("setUp testMethod tearDown " == test.log)

    def testResult(self) -> None:
        test = WasRun("testMethod")
        test.run(self.result)
        assert("1 run, 0 failed" == self.result.summary())

    def testFailedResult(self) -> None:
        test = WasRun("testBrokenMethod")
        test.run(self.result)
        assert("1 run, 1 failed" == self.result.summary())

    def testFailedResultFormatting(self) -> None:
        self.result.testStarted()
        self.result.testFailed()
        assert("1 run, 1 failed" == self.result.summary())

    def testSuite(self) -> None:
        suite = TestSuite()
        suite.add(WasRun("testMethod"))
        suite.add(WasRun("testBrokenMethod"))
        suite.run(self.result)
        assert("2 run, 1 failed" == self.result.summary())


if __name__ == "__main__":
    suite = TestSuite()
    suite.add(TestCaseTest("testTemplateMethod"))
    suite.add(TestCaseTest("testResult"))
    suite.add(TestCaseTest("testFailedResult"))
    suite.add(TestCaseTest("testFailedResultFormatting"))
    suite.add(TestCaseTest("testSuite"))

    result = TestResult()
    suite.run(result)
    print(result.summary())