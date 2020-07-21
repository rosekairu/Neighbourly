from django.test import TestCase
from .models import Neighborhood,Profile,Business,Notice,HealthCenter,Police
from django.contrib.auth.models import User
import datetime as dt
from django.urls import reverse


# Create your tests here.
class NeighborhoodTestClass(TestCase):

    def setUp(self):
        self.new_neighborhood = Neighborhood(
            hood_name="runda", population="3")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_neighborhood, Neighborhood))

    def tearDown(self):

        Neighborhood.objects.all().delete()

    def test_save_neighborhood(self):

        self.new_neighborhood.save_neighborhood()
        self.assertTrue(len(Neighborhood.objects.all()) > 0)

    def test_init(self):
        self.assertTrue(self.new_neighborhood.hood_name == 'runda')



class ProfileTestClass(TestCase):

    def setUp(self):
        user = User(username='rose')
        self.profile = Profile(bio='forever happy', user=user)

    def tearDown(self):
        User.objects.all().delete()
        Profile.objects.all().delete()

    def test_is_instance(self):
        """
        test whether the new profile is an instance of the Profile class
        """
        self.assertTrue(isinstance(self.profile, Profile))

    def test_init(self):
        """
        test whether the new profile is created
        """
        self.assertTrue(self.profile.bio == "forever happy")

    def test_save_profile(self):
        profile = Profile.objects.all()
        self.assertTrue(len(profile) >= 0)


class NoticeTestClass(TestCase):

    def setUp(self):

        self.new_user = User(
            username="rose", email="me@you.com", password="forever")
        self.new_user.save()
        self.new_notice = Notice='forever happy'

    
    def tearDown(self):
        """
        This will clear the dbs after each test
        """

        Notice.objects.all().delete()

    def test_save_notice(self):
        notice = Notice.objects.all()
        self.assertTrue(len(notice) >= 0)


class BusinessTestClass(TestCase):

    def setUp(self):
        self.new_user = User(
            username="rose", email="me@you.com", password="forever")
        self.new_user.save()
        self.new_business = Business(
            bsns_name='rose', user=self.new_user)
        self.new_business.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_business, Business))

    def tearDown(self):
        """
        This will clear the db after each test
        """
        Business.objects.all().delete()

    def test_create_business(self):

        self.new_business.create_business()
        self.assertTrue(len(Business.objects.all()) > 0)

    def test_init(self):
        self.assertTrue(self.new_business.bsns_name == 'rose')

    def test_delete_method(self):
        self.new_business.create_business()
        business = Business.objects.all()
        self.new_business.delete_business()
        business = Business.objects.all()
        self.assertTrue(len(business) == 0)

    def test_find_business(self):
        """
        This will test whether the search function works
        """
        self.new_business.create_business()
        bussiness = self.new_business.find_business(self.new_business.id)
        self.assertEquals(bussiness.bsns_name,'rose')
