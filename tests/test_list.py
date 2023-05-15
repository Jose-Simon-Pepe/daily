import pytest
from daiyly.listmanager import ListManager

lm = ListManager()

def test_list_should_has_lists():
    assert lm.getHowManyLists() == 1

def test_list_should_get_toml():
    assert len(lm.loadChecklists()) > 0
