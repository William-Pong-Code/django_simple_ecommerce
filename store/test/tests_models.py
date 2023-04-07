from django.test import TestCase
from store.models import Category, Product, User

class TestCategoriesModel(TestCase):
    '''
    Create a separate testing database
    '''
    def setUp(self):
        '''
        Create a dummy record
        '''
        self.data1 = Category.objects.create(name='django', slug='django')

    def test_category_model_entry(self):
        '''
        Test Category model data insertion/types/field attributes
        '''
        data = self.data1
        self.assertIsInstance(data, Category)

    def test_category_model_entry(self):
        '''
        Test Category model default name
        '''
        data = self.data1
        self.assertEqual(str(data), 'django')

class TestProductsModel(TestCase):
    '''
    Create a separate testing database
    '''
    def setUp(self):
        '''
        Create a dummy record
        '''
        Category.objects.create(name='django', slug='django')
        User.objects.create(username='admin')
        self.data1 = Product.objects.create(category_id=1, title='django beginners', created_by_id=1, slug='django-beginners', price='20.00', image='django')
    
    def test_product_model_entry(self):
        '''
        Test product model data insertion/types/field attributes
        '''
        data = self.data1
        self.assertIsInstance(data, Product)
        self.assertEqual(str(data), 'django beginners')