import pytest


@pytest.mark.django_db
def test_hello_world():
    assert 1 == 1
