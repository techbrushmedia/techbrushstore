from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.cart.models import Cart


class User(AbstractUser):
    phone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.username

    def get_active_cart(self):
        """Get or create active cart for user"""
        cart, created = Cart.objects.get_or_create(
            user=self,
            defaults={'session_id': None}
        )
        return cart

    def get_orders(self):
        """Get user's orders ordered by creation date"""
        return self.orders.all().order_by('-created_at')
    
about = """
<h2 class="font-bold text-left text-xl w-full">About TechBrushStore</h2>
<p class="py-3">TechBrushStore is an online store built around a clear collection, simple ordering, and thoughtful service.</p>
<h2 class="font-bold mt-3 text-left text-xl w-full">Our approach</h2>
<p class="py-3">We focus on detailed product information, transparent pricing, and a smooth shopping experience across every device.</p>
<h2 class="font-bold mt-3 text-left text-xl w-full">Here when you need us</h2>
<p class="py-3">For questions about a product or an order, you can reach the store through the contact details on the Contact page.</p>
"""

class Config(models.Model):
    site_title = models.CharField(max_length=255, default="Shop")
    header_top = models.CharField(max_length=255, default='header top offer')


    class Meta:
        verbose_name_plural = "Configs"

    def __str__(self):
        return f'{self.site_title} - Config'

    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)

    whatsapp_number = models.CharField(max_length=20, null=True, blank=True)
    messanger_url = models.URLField(null=True, blank=True)
    facebook_page_url = models.URLField( null=True, blank=True)
    instagram_url = models.URLField(null=True, blank=True)
    tiktok_url = models.URLField( null=True, blank=True)

    delivery_cost = models.IntegerField(default=0)
    delivery_cost_dhaka = models.IntegerField(default=0)

    about_page = models.TextField(null=True, blank=True, default=about)
    hero_image = models.ImageField(upload_to='site/', null=True, blank=True)


class ContactMessage(models.Model):
    INQUIRY_TYPES = [
        ('general', 'General Inquiry'),
        ('order', 'Order Related'),
        ('product', 'Product Question'),
        ('shipping', 'Shipping & Delivery'),
        ('return', 'Returns & Refunds'),
        ('technical', 'Technical Support'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    inquiry_type = models.CharField(max_length=20, choices=INQUIRY_TYPES)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_resolved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.subject} - {self.email}'