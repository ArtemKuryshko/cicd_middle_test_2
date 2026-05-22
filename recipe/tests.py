from django.test import TestCase
from django.urls import reverse

from .models import Category, Recipe


class RecipeViewTests(TestCase):
    def test_main_view_returns_ten_random_recipes(self):
        category = Category.objects.create(name='Breakfast')
        for number in range(12):
            Recipe.objects.create(
                title=f'Recipe {number}',
                description='Description',
                instructions='Instructions',
                ingredients='Ingredients',
                category=category,
            )

        response = self.client.get(reverse('main'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main.html')
        self.assertEqual(len(response.context['recipes']), 10)
