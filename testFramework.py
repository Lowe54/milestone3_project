def test_are_equal(actual, expected):
    assert expected == actual, "Expected {0}, got {1}".format(expected,actual)

def test_not_equal(a, b):
    assert a != b, "did not expect {0} but got {1}".format(a,b)

def is_in_collection(collection, item):
    assert item in collection, "{0} does not contain {1}".format(collection, item)

def does_return_none(actual):
    assert actual == None, "Expected None , got {0} ".format(actual)
def is_expected_type(label,field,expectedtype):
    print("Expecting type of {0}, for field {1}".format(expectedtype,label))
    assert isinstance(field,expectedtype), "Expected type of {0}, got {1}".format(expectedtype, type(field))
    print("Test Passed")
    print("*****")