from django.db import migrations


ABOUT_PAGE = """
<h2 class="font-bold text-left text-xl w-full">About TechBrushStore</h2>
<p class="py-3">TechBrushStore is an online store built around a clear collection, simple ordering, and thoughtful service.</p>
<h2 class="font-bold mt-3 text-left text-xl w-full">Our approach</h2>
<p class="py-3">We focus on detailed product information, transparent pricing, and a smooth shopping experience across every device.</p>
<h2 class="font-bold mt-3 text-left text-xl w-full">Here when you need us</h2>
<p class="py-3">For questions about a product or an order, you can reach the store through the contact details on the Contact page.</p>
"""


def rename_default_brand(apps, schema_editor):
    Config = apps.get_model('main', 'Config')
    Config.objects.filter(pk=1, site_title='techbrushshop').update(
        site_title='TechBrushStore',
        about_page=ABOUT_PAGE,
    )


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_rename_default_brand'),
    ]

    operations = [
        migrations.RunPython(rename_default_brand, migrations.RunPython.noop),
    ]