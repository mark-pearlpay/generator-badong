from .steps.given import *
from .steps.when import *
from .steps.then import *

import pytest


@pytest.fixture
def hello_world():
    return 'Hello World!'
