from django.test import TestCase
from .models import Product, ProductType
from django.urls import reverse

# Create your tests here.
class ProductTest(TestCase):
    def test_stringOutput(self):
        product=Product(productname='Leonovo laptop')
    self.assertEqual(str(product), product.productname)

    def test_tablename(self):
        self.assertEqual(str(Product._meta.db_table), 'product')

#testing a view
class TestIndex(TestCase):
    def test_view_url_accessible_by_name(self):
        response=self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response=self.client.get(reverse('index'))
    self.assertTemplateUsed(response, 'techapp/index.html')