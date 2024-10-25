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
    log: str = ""

    def setUp(self) -> None:
        self.log += "setUp "

    def testMethod(self) -> None:
        self.log += "testMethod "


class TestCaseTest(TestCase):
    test: WasRun

    def setUp(self) -> None:
        self.test = WasRun("testMethod")

    def testTemplateMethod(self) -> None:
        self.test.run()
        assert("setUp testMethod " == self.test.log)


if __name__ == "__main__":
    TestCaseTest("testTemplateMethod").run()
