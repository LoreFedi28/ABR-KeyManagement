from abr_normal import ABRNormal
from abr_flag import ABRFlag
from abr_list import ABRList

def test_abr_normal():
    abr = ABRNormal()
    keys = [10, 5, 15, 3, 7, 12, 18, 5, 10]
    for k in keys:
        abr.insert(k)
    result = abr.in_order()
    assert result == [3, 5, 7, 10, 12, 15, 18], f"ABR normal: incorrect result {result}"
    assert abr.search(7)
    assert not abr.search(4)
    print("Test ABR normal passed")

def test_abr_flag():
    abr = ABRFlag()
    keys = [10, 5, 15, 3, 7, 12, 18, 5, 10]
    for k in keys:
        abr.insert(k)
    result = abr.in_order()
    expected = {
        3: False,
        5: True,
        7: False,
        10: True,
        12: False,
        15: False,
        18: False,
    }
    for key, duplicate in result:
        assert expected[key] == duplicate, f"ABR flag: error on {key} (expected duplicate={expected[key]})"
    assert abr.search(15)
    assert not abr.search(4)
    print("Test ABR with flag passed")

def test_abr_list():
    abr = ABRList()
    keys = [10, 5, 15, 3, 7, 12, 18, 5, 10, 10]
    for k in keys:
        abr.insert(k)
    result = abr.in_order()
    expected = {
        3: 1,
        5: 2,
        7: 1,
        10: 3,
        12: 1,
        15: 1,
        18: 1,
    }
    for key, count in result:
        assert expected[key] == count, f"ABR list: error on {key} (expected={expected[key]}, found={count})"
    assert abr.search(5)
    assert not abr.search(999)
    print("Test ABR with list passed")

if __name__ == "__main__":
    print("Running unified tests:\n")
    test_abr_normal()
    test_abr_flag()
    test_abr_list()