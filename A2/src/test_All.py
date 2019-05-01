## @file test_All.py
#  @author Arkin Modi modia1
#  @brief pytest file for all modules
#  @date 11/02/2019

import pytest
from SeqADT import *
from DCapALst import *
from SALst import *
from Read import *


class TestSeqADT:
    def setup_method(self, method):
        self.test = SeqADT([DeptT.civil, DeptT.chemical])

    def teardown_method(self, method):
        self.test = None

    # test if init works
    def test_init(self):
        assert self.test.next() == DeptT.civil
        assert self.test.next() == DeptT.chemical

    # tests if start resets i
    def test_start(self):
        self.test.next()
        assert self.test.i == 1
        self.test.start()
        assert self.test.i == 0

    # tests if StopIteration error is raised
    def test_next_1(self):
        with pytest.raises(StopIteration):
            self.test.i = len(self.test.s)
            self.test.next()

    # tests if next() outputs correctly
    def test_next_2(self):
        assert self.test.next() == DeptT.civil
        assert self.test.next() == DeptT.chemical

    # tests if end() works
    def test_end_1(self):
        assert not self.test.end()

    # tests if end() works
    def test_end_2(self):
        self.test.i = len(self.test.s)
        assert self.test.end()
        self.test.i = len(self.test.s) + 1000
        assert self.test.end()


class TestDCapALst:
    def setup_method(self, method):
        load_stdnt_data("src/StdntData.txt")
        load_dcap_data("src/DeptCap.txt")

    def teardown_method(self, method):
        SALst.s = None
        AALst.s = None
        DCapALst.s = None

    # test if init works
    def test_init(self):
        DCapALst.init()
        assert DCapALst.s == {}

    # tests if KeyError is raised
    def test_add_1(self):
        with pytest.raises(KeyError):
            DCapALst.add(DeptT.civil, 2)

    # test if add() works
    def test_add_2(self):
        DCapALst.init()
        DCapALst.add(DeptT.civil, 2)
        assert DCapALst.elm(DeptT.civil)

    # tests if remove() works
    def test_remove_1(self):
        DCapALst.remove(DeptT.civil)
        assert not DCapALst.elm(DeptT.civil)

    # tests if remove() works
    def test_remove_2(self):
        with pytest.raises(KeyError):
            DCapALst.init()
            DCapALst.remove(DeptT.civil)

    # tests if elm() works
    def test_elm_1(self):
        assert DCapALst.elm(DeptT.civil)

    # tests if elm() works
    def test_elm_2(self):
        DCapALst.remove(DeptT.civil)
        assert not DCapALst.elm(DeptT.civil)

    # tests if capacity() works
    def test_capacity_1(self):
        assert DCapALst.capacity(DeptT.civil) == 100

    # test if KeyError is raised
    def test_capacity_2(self):
        with pytest.raises(KeyError):
            DCapALst.remove(DeptT.civil)
            DCapALst.capacity(DeptT.civil)


class TestSALst:
    def setup_method(self, method):
        load_stdnt_data("src/StdntData.txt")
        load_dcap_data("src/DeptCap.txt")

    def teardown_method(self, method):
        SALst.s = None
        AALst.s = None
        DCapALst.s = None

    # test if init works
    def test_init(self):
        SALst.init()
        assert SALst.s == {}

    # test if it can add a student
    def test_add_1(self):
        sinfo1 = SInfoT("first", "last", GenT.male, 12.0, SeqADT([DeptT.civil,
                        DeptT.chemical]), True)
        SALst.add("stdnt1", sinfo1)
        assert SALst.elm("stdnt1")
        assert SALst.info("stdnt1") == sinfo1

    # tests for KeyError when same student added twice
    def test_add_2(self):
        with pytest.raises(KeyError):
            sinfo1 = SInfoT("first", "last", GenT.male, 12.0,
                            SeqADT([DeptT.civil, DeptT.chemical]), True)
            SALst.add("stdnt1", sinfo1)
            SALst.add("stdnt1", sinfo1)

    # test if it can remove a student
    def test_remove_1(self):
        sinfo1 = SInfoT("first", "last", GenT.male, 12.0, SeqADT([DeptT.civil,
                        DeptT.chemical]), True)
        SALst.add("stdnt1", sinfo1)
        SALst.remove("stdnt1")
        assert SALst.elm

    # tests for KeyError when non-existing student is removed
    def test_remove_2(self):
        with pytest.raises(KeyError):
            SALst.remove("stdnt1")

    # test if it can find all students
    def test_elm(self):
        assert SALst.elm("macid1")
        assert SALst.elm("smithj")
        assert SALst.elm("smithj2")
        assert SALst.elm("brownc")
        assert not SALst.elm("stdnt1")

    # test if it can return the info correctly
    def test_info_1(self):
        sinfo1 = SInfoT("first", "last", GenT.male, 12.0, SeqADT([DeptT.civil,
                        DeptT.chemical]), True)
        SALst.add("stdnt1", sinfo1)
        assert SALst.info("stdnt1") == sinfo1

    # test if it raises error correctly
    def test_info_2(self):
        with pytest.raises(KeyError):
            SALst.info("stdnt1")

    # tests if sort() works for free choice
    def test_sort_1(self):
        test = SALst.sort(lambda t: t.freechoice and t.gpa >= 4.0)
        assert test[0] == "macid1"
        assert "brownc" not in test

    # tests if sort() works for non-free choice
    def test_sort_2(self):
        test = SALst.sort(lambda t: not(t.freechoice) and t.gpa >= 4.0)
        assert test[0] == "smithj"
        assert test[1] == "smithj2"
        assert "macid1" not in test

    # tests if average() works
    def test_average_1(self):
        test = SALst.average(lambda x: x.gender == GenT.male)
        assert test == pytest.approx(6.7)

    # test if ValueError is raised
    def test_average_2(self):
        with pytest.raises(ValueError):
            SALst.average(lambda x: False)

    # tests if allocate works
    def test_allocate_1(self):
        SALst.allocate()
        assert AALst.lst_alloc(DeptT.civil) == ["smithj"]

    # tests if RuntimeError is raised
    def test_allocate_2(self):
        with pytest.raises(RuntimeError):
            DCapALst.init()
            for d in DeptT:
                DCapALst.add(d, 0)
            SALst.allocate()
