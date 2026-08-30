from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_rename_default_brand_to_techbrushstore'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=200)),
                ('inquiry_type', models.CharField(choices=[('general', 'General Inquiry'), ('order', 'Order Related'), ('product', 'Product Question'), ('shipping', 'Shipping & Delivery'), ('return', 'Returns & Refunds'), ('technical', 'Technical Support')], max_length=20)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_resolved', models.BooleanField(default=False)),
            ],
            options={'ordering': ['-created_at']},
        ),
    ]