from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

from apps.product.models import Category, Color, Image, Product, Size


DEMO_PRODUCTS = [
    {
        'category': 'Keyboards',
        'name': 'Arc Mechanical Keyboard',
        'sku': 'TBS-KEY-001',
        'price': 12990,
        'stock_quantity': 18,
        'is_featured': True,
        'short_description': 'A compact mechanical keyboard with a quiet, focused feel.',
        'description': 'The Arc Mechanical Keyboard is designed for clean desk setups and comfortable everyday typing.',
        'sizes': [],
        'colors': [('Graphite', '#252525'), ('Rose', '#E40078')],
        'art': ('#E40078', 'KEYBOARD'),
        'image_url': 'https://images.unsplash.com/photo-1587829741301-dc798b83add3?auto=format&fit=crop&w=1200&q=85',
    },
    {
        'category': 'Keyboards',
        'name': 'Pixel Keycap Set',
        'sku': 'TBS-KEY-002',
        'price': 3990,
        'stock_quantity': 24,
        'is_featured': True,
        'short_description': 'A vivid keycap set to give a mechanical keyboard a new character.',
        'description': 'A durable replacement keycap set for compatible mechanical keyboard layouts.',
        'sizes': [],
        'colors': [('Pink', '#E40078'), ('Cream', '#F4EDE3')],
        'art': ('#5A174A', 'KEYCAPS'),
        'image_url': 'https://images.unsplash.com/photo-1541140532154-b024d705b90a?auto=format&fit=crop&w=1200&q=85',
    },
    {
        'category': 'Mice',
        'name': 'Contour Wireless Mouse',
        'sku': 'TBS-MOU-001',
        'price': 6990,
        'stock_quantity': 31,
        'is_featured': True,
        'short_description': 'A lightweight wireless mouse shaped for long work sessions.',
        'description': 'Contour combines precise tracking and an ergonomic silhouette for desk work or gaming.',
        'sizes': [],
        'colors': [('Black', '#171717'), ('White', '#F5F5F5')],
        'art': ('#242424', 'MOUSE'),
        'image_url': 'https://images.unsplash.com/photo-1527814050087-3793815479db?auto=format&fit=crop&w=1200&q=85',
    },
    {
        'category': 'Mice',
        'name': 'Glide XL Mouse Pad',
        'sku': 'TBS-MOU-002',
        'price': 2790,
        'stock_quantity': 42,
        'is_featured': True,
        'short_description': 'An extended desk mat with a smooth, stable surface.',
        'description': 'Glide XL gives your keyboard and mouse a calm, consistent surface.',
        'sizes': ['XL'],
        'colors': [('Midnight', '#131313'), ('Fuchsia', '#E40078')],
        'art': ('#121212', 'DESK MAT'),
        'image_url': 'https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?auto=format&fit=crop&w=1200&q=85',
    },
    {
        'category': 'Desk Setup',
        'name': 'Orbit USB-C Hub',
        'sku': 'TBS-DSK-001',
        'price': 5490,
        'stock_quantity': 20,
        'is_featured': True,
        'short_description': 'An aluminium USB-C hub for the connections you use every day.',
        'description': 'Orbit keeps essential ports close at hand while keeping your workspace tidy.',
        'sizes': [],
        'colors': [('Silver', '#C6C6C6')],
        'art': ('#545454', 'USB-C HUB'),
        'image_url': 'https://images.unsplash.com/photo-1625842268584-8f3296236761?auto=format&fit=crop&w=1200&q=85',
    },
    {
        'category': 'Desk Setup',
        'name': 'Lift Laptop Stand',
        'sku': 'TBS-DSK-002',
        'price': 4590,
        'stock_quantity': 16,
        'is_featured': True,
        'short_description': 'An adjustable stand that puts your laptop at a comfortable height.',
        'description': 'Lift improves posture and opens up valuable desk space beneath your laptop.',
        'sizes': [],
        'colors': [('Silver', '#C6C6C6'), ('Black', '#171717')],
        'art': ('#BFBFBF', 'LAPTOP STAND'),
        'image_url': 'https://images.unsplash.com/photo-1496181133206-80ce9b88a853?auto=format&fit=crop&w=1200&q=85',
    },
    {
        'category': 'Audio',
        'name': 'Wave Desk Speaker',
        'sku': 'TBS-AUD-001',
        'price': 8990,
        'stock_quantity': 12,
        'is_featured': True,
        'short_description': 'A compact stereo speaker pair for music, calls, and focus.',
        'description': 'Wave brings warm, balanced sound to a small workspace without taking over the desk.',
        'sizes': [],
        'colors': [('Black', '#171717')],
        'art': ('#1D1D1D', 'SPEAKER'),
        'image_url': 'https://images.unsplash.com/photo-1545454675-3531b543be5d?auto=format&fit=crop&w=1200&q=85',
    },
    {
        'category': 'Audio',
        'name': 'Focus Headphones',
        'sku': 'TBS-AUD-002',
        'price': 10990,
        'stock_quantity': 9,
        'is_featured': True,
        'short_description': 'Comfortable over-ear headphones for workdays and playlists.',
        'description': 'Focus headphones offer an enveloping fit and clear everyday audio.',
        'sizes': [],
        'colors': [('Graphite', '#252525'), ('Fuchsia', '#E40078')],
        'art': ('#E40078', 'HEADPHONES'),
        'image_url': 'https://images.unsplash.com/photo-1505740420928-5e560c06d30e?auto=format&fit=crop&w=1200&q=85',
    },
    {
        'category': 'Cables & Power',
        'name': 'Volt 65W GaN Charger',
        'sku': 'TBS-PWR-001',
        'price': 3490,
        'stock_quantity': 26,
        'is_featured': True,
        'short_description': 'A compact fast charger for laptops, phones, and everyday carry.',
        'description': 'Volt delivers dependable USB-C charging from a compact GaN power adapter.',
        'sizes': [],
        'colors': [('White', '#F5F5F5')],
        'art': ('#F5F5F5', 'CHARGER'),
        'image_url': 'https://images.unsplash.com/photo-1587033411391-5d9e51cce126?auto=format&fit=crop&w=1200&q=85',
    },
    {
        'category': 'Cables & Power',
        'name': 'Flow Braided USB-C Cable',
        'sku': 'TBS-PWR-002',
        'price': 1990,
        'stock_quantity': 38,
        'is_featured': True,
        'short_description': 'A durable, flexible USB-C cable for reliable daily charging.',
        'description': 'Flow uses a reinforced braided jacket and a generous length for flexible setups.',
        'sizes': ['1.5 m', '2 m'],
        'colors': [('Fuchsia', '#E40078'), ('Black', '#171717')],
        'art': ('#E40078', 'USB-C CABLE'),
        'image_url': 'https://images.unsplash.com/photo-1616578272662-b6dbe6f491d0?auto=format&fit=crop&w=1200&q=85',
    },
    {
        'category': 'Lighting',
        'name': 'Halo Monitor Light',
        'sku': 'TBS-LGT-001',
        'price': 6490,
        'stock_quantity': 14,
        'is_featured': True,
        'short_description': 'A focused screen light that keeps your desk softly illuminated.',
        'description': 'Halo reduces screen glare with adjustable brightness and a clean monitor-mounted form.',
        'sizes': [],
        'colors': [('Black', '#171717')],
        'art': ('#F3D59A', 'MONITOR LIGHT'),
        'image_url': 'https://images.unsplash.com/photo-1531297484001-80022131f5a1?auto=format&fit=crop&w=1200&q=85',
    },
    {
        'category': 'Lighting',
        'name': 'Nova Desk Lamp',
        'sku': 'TBS-LGT-002',
        'price': 5990,
        'stock_quantity': 17,
        'is_featured': True,
        'short_description': 'A minimal desk lamp with warm, adjustable task lighting.',
        'description': 'Nova brings a focused pool of light to late sessions and early starts.',
        'sizes': [],
        'colors': [('Black', '#171717'), ('White', '#F5F5F5')],
        'art': ('#F3D59A', 'DESK LAMP'),
        'image_url': 'https://images.unsplash.com/photo-1507473885765-e6ed057f782c?auto=format&fit=crop&w=1200&q=85',
    },
]


def product_art(color, label):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 1200" role="img" aria-label="{label}">
<rect width="1200" height="1200" fill="#171717"/>
<circle cx="970" cy="205" r="270" fill="{color}" opacity="0.9"/>
<rect x="120" y="680" width="960" height="170" rx="28" fill="#F7F7F7"/>
<rect x="160" y="720" width="880" height="90" rx="15" fill="{color}" opacity="0.88"/>
<text x="120" y="235" fill="#FFFFFF" font-family="Arial, sans-serif" font-size="60" font-weight="700">TECHBRUSHSTORE</text>
<text x="120" y="1040" fill="#FFFFFF" font-family="Arial, sans-serif" font-size="82" font-weight="700">{label}</text>
</svg>'''


class Command(BaseCommand):
    help = 'Create an idempotent TechBrushStore demonstration catalog.'

    def handle(self, *args, **options):
        created_products = 0
        for item in DEMO_PRODUCTS:
            category, _ = Category.objects.get_or_create(name=item['category'])
            product, created = Product.objects.update_or_create(
                sku=item['sku'],
                defaults={
                    'name': item['name'],
                    'category': category,
                    'price': item['price'],
                    'stock_quantity': item['stock_quantity'],
                    'is_active': True,
                    'is_featured': item['is_featured'],
                    'short_description': item['short_description'],
                    'description': item['description'],
                },
            )
            created_products += created
            for size in item['sizes']:
                Size.objects.get_or_create(product=product, name=size)
            for name, hex_code in item['colors']:
                Color.objects.get_or_create(product=product, name=name, defaults={'hex_code': hex_code})
            primary_image = product.images.filter(is_primary=True).first() or product.images.order_by('pk').first()
            if primary_image:
                if not primary_image.is_primary:
                    primary_image.is_primary = True
                primary_image.external_url = item['image_url']
                primary_image.save(update_fields=['is_primary', 'external_url'])
            else:
                color, label = item['art']
                image = Image(product=product, alt_text=item['name'], is_primary=True)
                image.image.save(
                    f'{product.slug}.svg',
                    ContentFile(product_art(color, label).encode()),
                    save=True,
                )
                image.external_url = item['image_url']
                image.save(update_fields=['external_url'])

        self.stdout.write(self.style.SUCCESS(
            f'Demo catalog ready: {len(DEMO_PRODUCTS)} products, {created_products} newly created.'
        ))