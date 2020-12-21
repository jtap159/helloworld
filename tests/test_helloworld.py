from helloworld.helloworld import sayhello


def test_helloworld_no_params():
    assert sayhello() == "Hello World, Everyone!"


def test_helloworld_with_param():
    assert sayhello("Jeremy") == "Hello World, Jeremy"