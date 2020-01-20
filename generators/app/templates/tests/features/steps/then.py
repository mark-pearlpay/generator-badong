from pytest_bdd import then, parsers


@then('I then hello world step')
def then_hello_world(hello_world):
    print('then:', hello_world)
    pass
