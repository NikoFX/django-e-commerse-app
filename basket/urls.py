"""denteca URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
import basket.views

app_name = 'basket'
urlpatterns = [
    path('', basket.views.basket, name='basket'),
    path('ref', basket.views.refresh, name='refresh'),
    path('del', basket.views.delete, name='delete'),
    path('checkout', basket.views.checkout, name='checkout'),
    path('coupon_check', basket.views.coupon_check, name='coupon_check'),
]