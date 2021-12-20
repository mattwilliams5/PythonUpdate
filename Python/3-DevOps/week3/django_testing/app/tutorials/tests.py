from django.test import TestCase
from django.urls import reverse
from tutorials.models import Tutorial
import pytest

# Create your tests here.
def test_homepage_access():
    url = reverse('home')
    assert url == "/"

def test_create_tutorial():
    tutorial = Tutorial.objects.create(
        title='Pytest',
        tutorial_url='https://pytest-django.readthedocs.io/en/latest/index.html',
        description='Tutorial on how to apply pytest to a Django application',
        published=True
    )
    assert tutorial.title == "Pytest"