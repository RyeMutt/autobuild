import sys

import pytest

from autobuild.executable import Executable
from tests.basetest import BaseTest


class TestExecutable(BaseTest):
    def setUp(self):
        BaseTest.setUp(self)

    def test_simple_executable(self):
        sleepExecutable = Executable(command='sleep', arguments=['1'])
        result = sleepExecutable()
        assert result == 0

    def test_compound_executable(self):
        parentExecutable = Executable(command='grep', arguments=['foobarbaz', '.'], options=['-l', '-r'])
        childExecutable = Executable(parent=parentExecutable, options=['-i'])
        otherChildExecutable = Executable(parent=parentExecutable, command='egrep', arguments=['foo','.'])
        assert childExecutable.get_options() == ['-l', '-r', '-i']
        assert childExecutable.get_command() == 'grep'
        assert otherChildExecutable.get_command() == 'egrep'
        assert otherChildExecutable.get_arguments() == ['foo','.']
        # On Windows, you can't count on grep or egrep.
        if sys.platform.startswith("win"):
            pytest.skip("On Windows, can't count on finding grep")
        result = childExecutable()
        assert result == 0, "%s => %s" % (childExecutable._get_all_arguments([]), result)
        result = parentExecutable()
        assert result == 0, "%s => %s" % (parentExecutable._get_all_arguments([]), result)

    def tearDown(self):
        BaseTest.tearDown(self)
