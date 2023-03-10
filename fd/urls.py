"""fd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from turtle import home
from django.contrib import admin
from django.urls import path,include
from products import views
from products.views import review
from products.views import Order,CreateCheckoutSessionView,payment_cancel,payment_succes,my_webhook_view,home_view,review
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home',home_view,name='home'),
    path('review',review,name='review'),
    # path('review_send',review.as_view(),name='review'),

    path('admin/', admin.site.urls),
    path('order/', Order.as_view(), name='order'),
    path('order_confi/', Order.as_view(), name='order'),
    path('create-checkout-session/<pk>/',CreateCheckoutSessionView.as_view(),name='create-checkout-session'),
    path('payment-suceess/',payment_succes,name='payment-succes'),
    path('payment-cancel/',payment_cancel,name='payment-cancel'),
    path('webhoock/stripe',my_webhook_view,name='webhook-stripe'),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('resto.urls'))
    



    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
