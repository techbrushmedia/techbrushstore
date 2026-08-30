from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_product_is_featured'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='external_url',
            field=models.URLField(blank=True),
        ),
    ]