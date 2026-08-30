from django.db import migrations


def create_default_config(apps, schema_editor):
    Config = apps.get_model('main', 'Config')
    Config.objects.get_or_create(pk=1)


def remove_default_config(apps, schema_editor):
    Config = apps.get_model('main', 'Config')
    Config.objects.filter(pk=1, site_title='Shop').delete()


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_config_address_config_email_config_phone_and_more'),
    ]

    operations = [
        migrations.RunPython(create_default_config, remove_default_config),
    ]