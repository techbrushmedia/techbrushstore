import uuid

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_address_remove_order_full_address_order_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='access_token',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]