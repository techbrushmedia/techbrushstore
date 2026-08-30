from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_config_hero_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='config',
            name='instagram_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]