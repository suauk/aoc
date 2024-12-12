import pytest
import solution

def test_safeReports():
    answer=solution.Solution()
    assert answer.safeReports(file="safe") == 1

def test_unsafeReports():
    answer=solution.Solution()
    assert answer.safeReports(file="unsafe") == 0