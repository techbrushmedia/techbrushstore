from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_contactmessage'),
    ]

    operations = [
        migrations.AddField(
            model_name='config',
            name='hero_image',
            field=models.ImageField(blank=True, null=True, upload_to='site/'),
        ),
    ]