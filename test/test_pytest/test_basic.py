def test_basic_stuff():
    assert True


def test_list():
    lst = [1, 3, 5, 6]
    assert [1, 3, 4] == lst


def test_string():
    assert 'unitest' == 'unittest'


def test_dict():
    dct = {'pt': 'Português', 'es': 'Espanhol'}
    assert dct['pt'] == 'Português'
