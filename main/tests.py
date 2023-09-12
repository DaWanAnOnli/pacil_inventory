from django.test import TestCase, Client
from main.models import Item

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')
        

class ItemTest(TestCase):
    @classmethod
    def setUpTestData(self):
        Item.objects.create(name='Paper', amount='500', description='good old paper')
    
    def test_name(self):
        item = Item.objects.get(id=1)
        the_name = item.name
        self.assertEqual(the_name, 'Paper')
        
    def test_name_max_length(self):
        item = Item.objects.get(id=1)
        field_label = item._meta.get_field('name').max_length
        self.assertEqual(field_label, 255)
        
    
