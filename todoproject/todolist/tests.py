from django.test import TestCase
from .models import Todo, Category
from .forms import TodoForm, CategoryForm
# Create your tests here.

class TodoTest(TestCase):
    def test_string(self):
        title=Todo(title="Something")
        self.assertEqual(str(title),title.title)

    def text_table(self):
        self.assertEqual(str(Todo._mata.db.table), 'Todo' )


class CategoryTest(TestCase):
    def test_string(self):
        name=Category(name="Something")
        self.assertEqual(str(name),name.name)

    def text_table(self):
        self.assertEqual(str(Category._mata.db.table), 'Category' )


class Category_Form_Test(TestCase):
    def test_form_is_valid(self):
        form=CategoryForm(data={'name':"blah",'date_created':"blah"})
        self.assertTrue(form.is_valid())