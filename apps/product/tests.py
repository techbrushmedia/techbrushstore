from django.test import TestCase
from django.urls import reverse

from .models import Category, Product


class CategoryViewTests(TestCase):
    def test_category_is_shown_in_the_main_navigation(self):
        category = Category.objects.create(name='Accessories')

        response = self.client.get(reverse('index'))

        self.assertContains(response, category.name)
        self.assertContains(response, category.get_absolute_url())

    def test_category_page_is_available(self):
        category = Category.objects.create(name='Accessories')

        response = self.client.get(category.get_absolute_url())

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.request['PATH_INFO'], reverse('category', kwargs={'slug': category.slug}))


class ProductListPaginationTests(TestCase):
    def test_products_per_page_selector_and_pagination_preserve_filters(self):
        for number in range(12):
            Product.objects.create(
                name=f'Product {number}',
                price=number + 1,
                sku=f'PAGINATION-{number}',
                stock_quantity=1,
            )

        response = self.client.get(reverse('products'), {'per_page': 8, 'sort': 'price_low'})

        self.assertEqual(len(response.context['products']), 8)
        self.assertContains(response, 'Products per page')
        self.assertContains(response, 'per_page=8&amp;sort=price_low&amp;page=2')
