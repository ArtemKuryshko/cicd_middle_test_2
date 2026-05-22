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

    def test_main_view_handles_empty_recipe_list(self):
        response = self.client.get(reverse('main'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main.html')
        self.assertEqual(list(response.context['recipes']), [])

    def test_category_detail_view_returns_recipes_for_category(self):
        target_category = Category.objects.create(name='Soups')
        other_category = Category.objects.create(name='Desserts')
        target_recipe = Recipe.objects.create(
            title='Borscht',
            description='Description',
            instructions='Instructions',
            ingredients='Ingredients',
            category=target_category,
        )
        Recipe.objects.create(
            title='Cake',
            description='Description',
            instructions='Instructions',
            ingredients='Ingredients',
            category=other_category,
        )

        response = self.client.get(
            reverse('category_detail', kwargs={'category_id': target_category.id})
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'category_detail.html')
        self.assertEqual(list(response.context['category']), [target_recipe])
