
from django.shortcuts import get_object_or_404, render

from .models import Category, Recipe


def main(request):
    recipes = Recipe.objects.order_by('?')[:10]
    return render(request, 'main.html', {'recipes': recipes})


def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    recipes = category.categories.all()
    return render(request, 'category_detail.html', {'category': recipes})
