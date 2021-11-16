from code_challenges.stack_and_queue.stack_queue_brackets.stack_queue_brackets import *

def test_brackets_in_the_string_are_balanced():
    actual=multi_bracket_validation("{}{?Code}[Fellows](())")
    excepted = True
    assert actual == excepted

def test_brackets_in_the_string_arent_balanced():
    """
    return False, if the brackets arent balanced
    """
    actual = multi_bracket_validation("{{(})}")
    excepted= False
    assert actual == excepted

def test_no_brackets():
    actual = multi_bracket_validation("---aa")
    excepted= False
    assert actual == excepted


def test_empyt_string():
    actual = multi_bracket_validation("")
    excepted= False
    assert actual == excepted


