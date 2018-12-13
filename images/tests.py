from django.test import TestCase
from .models import Location, Category, Image

class LocationTestClass(TestCase):
    '''
    Tests Location class and its functions and methods
    '''
    #Set up method
    def setUp(self):
        self.location = Location(name='U.S.A')
    #Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.location, Location))
    
    def test_save_method(self):
        '''
        Function to test that location is being saved
        '''
        self.location.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

    def test_delete_method(self):
        '''
        Function that tests whether a location can be deleted
        '''
        self.location.save_location()
        self.location.delete_location()


class CategoryTestClass(TestCase):
    '''
    Tests category class and its functions and methods
    '''
    #Set up method
    def setUp(self):
        self.category = Category(name='Sports')
    #Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.category, Category))
    
    def test_save_method(self):
        '''
        Function to test that category is being saved
        '''
        self.category.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

    def test_delete_method(self):
        '''
        Function that tests whether a category can be deleted
        '''
        self.category.save_category()
        self.category.delete_category()



class ImageTestClass(TestCase):
    '''
    Tests Image class and its functions and methods
    '''
    #Set up method
    def setUp(self):
        self.location = Location(name='U.S.A')
        self.location.save_location()

        self.category = Category(name='sports')
        self.category.save_category()

    
        self.image = Image(image='image.jpeg', name='image', description = 'testing image', location=self.location, category = self.category)

    def test_instance(self):
        self.assertTrue(isinstance(self.image, Image))

    def test_save_method(self):
        '''
        Function that tests whether an image and its details is being saved
        '''
        self.image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    def test_delete_method(self):
        '''
        Function that tests whether an image can be deleted.
        '''
        self.image.save_image()
        self.image.delete_image()

       
    def test_filter_by_location(self):
        '''
        Function that tests whether you can get an image by its location
        '''
        self.image.save_image()
        images = self.image.filter_by_location(self.image.location_id)
        images = Image.objects.filter(location=self.image.location_id)
        self.assertTrue(images, images)
