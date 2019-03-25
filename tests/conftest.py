import pytest

from flask_boilerplate import create_app

@pytest.fixture
def app():
    app = create_app({
        'TESTING': True,
    })

    yield app


@pytest.fixture
def client(app):
    return app.test_client()

# This was the test used in the week 9 quiz that I needed to fix
# @pytest.fixture
# def my_number():
#     return 13
