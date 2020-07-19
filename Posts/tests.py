from django.test import TestCase
from __future__ import unicode_literals
from .models import *
from django.core.files.uploadedfile import SimpleUploadedFile



# Create your tests here.
class NeighborhoodTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.nairobi = location.objects.create(name="nairobi")

        self.test_neighborhood = Neighborhood.objects.create(neighborhood_name='imagesef',
                                population='1000',
                                neighborhood_location=self.nairobi,
                                )

        self.test_neighborhood.save()

    def test_save_method(self):
        self.test_neighborhood.save()
        test_neighborhoods = Neighborhood.objects.all()
        self.assertTrue(len(test_neighborhoods) > 0)

    # Testing save method
    def test_save_neighborhood(self):
        self.assertEqual(len(Neighborhood.objects.all()), 1)

    # Tear down method
    def tearDown(self):
        Neighborhood.objects.all().delete()

    def test_delete_neighborhood(self):
        Neighborhood.delete_image_by_id(self.test_neighborhood.id)
        self.assertEqual(len(Neighborhood.objects.all()), 0)


class ProjectTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.nairobi = Neighborhood.objects.create(name="nairobi")

        self.test_project = Project.objects.create(image='imagesef',
                                                   name='cat',
                                                   description='This is a description',
                                                   neighborhood_id=self.nairobi,
                                                   )

        self.test_project.save()

    def test_save_method(self):
        self.test_project.save()
        test_projects = Project.objects.all()
        self.assertTrue(len(test_projects) > 0)

    # Testing save method
    def test_save_project(self):
        self.assertEqual(len(Project.objects.all()), 1)

    # Tear down method
    def tearDown(self):
        Project.objects.all().delete()

    def test_delete_project(self):
        Project.delete_image_by_id(self.test_project.id)
        self.assertEqual(len(Project.objects.all()), 0)


class BusinessTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.nairobi = Neighborhood.objects.create(name="nairobi")

        self.test_business = Business.objects.create(image='imagesef',
                                                     business_name='cat',
                                                     business_email_address='business@gmail.com',
                                                     neighborhood_id=self.nairobi,
                                                     )

        self.test_business.save()

    def test_save_method(self):
        self.test_business.save()
        test_businesses = Business.objects.all()
        self.assertTrue(len(test_businesses) > 0)

    # Testing save method
    def test_save_business(self):
        self.assertEqual(len(Business.objects.all()), 1)

    # Tear down method
    def tearDown(self):
        Business.objects.all().delete()

    def test_delete_image(self):
        Business.delete_business_by_id(self.test_business.id)
        self.assertEqual(len(Business.objects.all()), 0)


class tagsTestClass(TestCase):

    # Set up method the test for location and instantiating the location object

    def setUp(self):
        self.test_tags = tags(name='funny')
        self.test_tags.save()

        # Testing instance

    def test_instance(self):
        self.assertTrue(isinstance(self.test_tags, tags))

        # Testing Save method

    def test_save_method(self):
        tags = tags.objects.create(name='funny')
        tags = tags.objects.all()
        self.assertTrue(len(tags) > 0)

    # Tear down method
    def tearDown(self):
        tags.objects.all().delete()

        # Testing delete method

    def test_delete_tags(self):
        self.test_tags.delete()
        self.assertEqual(len(tags.objects.all()), 0)


class LocationTestClass(TestCase):

    #Set up method the test for location and instantiating the location object


    def setUp(self):
        self.test_location = Location(name = 'Nairobi')
        self.test_location.save()

    #Testing instance

    def test_instance(self):

        self.assertTrue(isinstance(self.test_location, Location))

    #Testing Save method

    def test_save_method(self):
        locations = Location.objects.all()
        self.assertTrue(len(locations)>0)

    # Tear down method
    def tearDown(self):
        Location.objects.all().delete()

        # Testing delete method

    def test_delete_location(self):
        self.test_location.delete()
        self.assertEqual(len(Location.objects.all()), 0)



class Review(TestCase):

    def setUp(self):

        self.melissa = User.objects.create(username="melissa")
        self.picture = Image.objects.create(image='image1',
                                            user=self.melissa)
        self.comment = Review.objects.create(comment = 'nicephoto')

        self.test_review = Review.objects.create(user=self.melissa,
                                                 image=self.picture,
                                                 comment='nice photo')
        self.test_review.save()

    #Testing instance

    def test_instance(self):

        self.assertTrue(isinstance(self.test_reviews, Review))

    #Testing Save method

    def test_save_method(self):
        reviews = Review.objects.all()
        self.assertTrue(len(reviews)>0)

    def test_save_review(self):
        self.assertEqual(len(Review.objects.all()), 1)

    # Tear down method
    def tearDown(self):
        Review.objects.all().delete()

        # Testing delete method

    def test_delete_review(self):
        self.test_review.delete()
        self.assertEqual(len(Review.objects.all()), 0)
