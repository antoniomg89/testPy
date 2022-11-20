from src.project import project

class TestProject:
    def test_object_OK(self):
        self.obj_tester = project()
        assert isinstance(self.obj_tester,project)

    def test_getParam1_correctly(self):
        self.obj_tester = project()
        assert isinstance(self.obj_tester.getParam1(),int)

    def test_getParam2_correctly(self):
        self.obj_tester = project()
        assert isinstance(self.obj_tester.getParam2(),int)

    def test_getParam1_value_correctly(self):
        self.obj_tester = project()
        assert(self.obj_tester.getParam1() == 1)

    def test_getParam2_value_correctly(self):
        self.obj_tester = project()
        assert(self.obj_tester.getParam2() == 2)