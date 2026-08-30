from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.urls import reverse_lazy
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('robots.txt', include('robots.urls')),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path('shipping-returns/', views.legal, {'page': 'shipping-returns'}, name='shipping_returns'),
    path('privacy/', views.legal, {'page': 'privacy'}, name='privacy'),
    path('terms/', views.legal, {'page': 'terms'}, name='terms'),
    path('login/', auth_views.LoginView.as_view(template_name='main/login.html'), name='login'),
    path('register/', views.register, name='register'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='main/password_reset.html', email_template_name='main/password_reset_email.txt', subject_template_name='main/password_reset_subject.txt', success_url=reverse_lazy('password_reset_done')), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='main/password_reset_done.html'), name='password_reset_done'),
    path('password-reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='main/password_reset_confirm.html', success_url=reverse_lazy('password_reset_complete')), name='password_reset_confirm'),
    path('password-reset/complete/', auth_views.PasswordResetCompleteView.as_view(template_name='main/password_reset_complete.html'), name='password_reset_complete'),
    path('product/', include('apps.product.urls'), name='product'),
    path('cart/', include('apps.cart.urls'), name='cart'),
    path('checkout/', include('apps.order.urls'), name='checkout'),
]
# serve media files
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

