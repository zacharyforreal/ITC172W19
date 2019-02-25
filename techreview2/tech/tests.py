from django.test import TestCase
from .models import Product, ProductType, Review
from .forms import ProductForm
from datetime import datetime
from django.urls import reverse

# Create your tests here.
class ProductTest(TestCase):
    def test_stringOutput(self):
        product=Product(productname='Leonovo laptop')
    self.assertEqual(str(product), product.productname)

    def test_tablename(self):
        self.assertEqual(str(Product._meta.db_table), 'product')

class ProductTypeTest(TestCase):
    def test_stringOutput(self):
        techtype=ProductType(typename='Laptop')
        self.assertEqual(str(techtype), techtype.typename)

    def test_tablename(self):
        self.assertEqual(str(TechType._meta.db_table), 'producttype')

class ReviewTest(TestCase):
    def test_stringOutput(self):
        review=Review(reviewtitle='Lenovo Laptop')
        self.assertEqual(str(review), review.reviewtitle)

    def test_tablename(self):
self.assertEqual(str(Review._meta.db_table), 'review')

#testing a view
class TestIndex(TestCase):
    def test_view_url_accessible_by_name(self):
         response=self.client.get(reverse('index'))
         self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
         response=self.client.get(reverse('index'))
         self.assertEqual(response.status_code, 200)
         self.assertTemplateUsed(response, 'tech/index.html')

class TestGetProduct(TestCase):


    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/tech/products')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('getproducts'))
        self.assertEqual(response.status_code, 200)
        
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('getproducts'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reviews/products.html')

class New_Product_Form_Test(TestCase):

    # Valid Form Data
    def test_productForm_is_valid(self):
        form = ProductForm(data={'productname': "Surface", 'techtype': "laptop", 'user': "steve", 'entrydate': "2018-12-17", 'productURL':"http:microsoft.com", 'productdescription':"lightweight laptop" })
        self.assertTrue(form.is_valid())

    # Invalid Form Data
    def test_UserForm_invalid(self):
        form = ProductForm(data={'productname': "Surface", 'techtype': "laptop", 'user': "steve", 'entrydate': "2018-12-17", 'productURL':"http:microsoft.com", 'productdescription':"lightweight laptop" })
self.assertFalse(form.is_valid())