from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import redirect, render
from apps.product.models import Product
from .models import Config, ContactMessage, about
from .forms import ContactForm, UserRegistrationForm


LEGAL_PAGES = {
    'shipping-returns': {
        'title': 'Shipping & Returns',
        'sections': [
            ('Delivery', 'Delivery costs and estimated times are confirmed at checkout. Please make sure your delivery address and phone number are accurate.'),
            ('Returns', 'If an item arrives damaged or incorrect, contact the store with your order number so we can review your request.'),
        ],
    },
    'privacy': {
        'title': 'Privacy Policy',
        'sections': [
            ('Information we collect', 'We use the contact and delivery information you provide to process orders and respond to messages.'),
            ('How we use it', 'Your information is used only to operate the store, fulfill orders, and provide customer support.'),
        ],
    },
    'terms': {
        'title': 'Terms & Conditions',
        'sections': [
            ('Orders', 'Submitting an order is a request to purchase the selected products. Stock availability is confirmed before fulfillment.'),
            ('Pricing', 'Product prices and delivery charges are shown in the store and may be updated before an order is placed.'),
        ],
    },
}


def index(request):
    featured_products = Product.objects.filter(is_active=True, is_featured=True)
    context = {
        "featured_products": featured_products
    }
    return render(request, 'index.html', context)

def about(request):
    config = Config.objects.first()
    about_page = config.about_page if config else about
    return render(request, 'main/about.html', {"about_page": about_page})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            ContactMessage.objects.create(**form.cleaned_data)
            messages.success(request, 'Thanks for reaching out. Your message has been received.')
            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'main/contact.html', {'form': form})


def legal(request, page):
    content = LEGAL_PAGES.get(page)
    if not content:
        raise Http404
    return render(request, 'main/legal.html', content)


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserRegistrationForm()

    return render(request, 'main/register.html', {'form': form})