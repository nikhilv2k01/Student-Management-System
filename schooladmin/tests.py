from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse

# Create your tests here.

class TestSample(TestCase):

    def setup(self):
        self.client=APIClient

    def test_home(self):
        url=reverse('school_admin:home')
        res=self.client.get(url)
        print(res.data)
        self.assertEquals(res.status_code,200)
        self.assertEquals(res.data,'congrats')

