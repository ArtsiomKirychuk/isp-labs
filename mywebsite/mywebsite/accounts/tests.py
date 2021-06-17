import pytest
from django.contrib.auth.models import User
from.models import Customer, Product, Order, Tag
from django.test import RequestFactory, Client
from .views import *

@pytest.fixture
def user(db):
    user = User.objects.create_user(username='testusername', email='testemail', password='testpassword')
    return user

@pytest.mark.django_db
def test_home(user):
    factory = RequestFactory()
    request = factory.get('')
    request.user = user
    response = home(request)
    assert response.status_code == 200

@pytest.mark.django_db
def test_login(user):
    factory = RequestFactory()
    request = factory.get('login')
    request.user = user
    response = login.as_view()(request)
    assert response.status_code == 200


@pytest.mark.django_db
def test_logout(user):
    factory = RequestFactory()
    request = factory.get('')
    request.user = user
    response = logout(request)
    assert response.status_code == 200


