from pytest_bdd import given, parsers


@given('I given hello world step')
def given_hello_world(hello_world):
    print('given:', hello_world)
    pass
