from pytest_bdd import when, parsers


@when('I when hello world step')
def when_hello_world(hello_world):
    print('when:', hello_world)
    pass
