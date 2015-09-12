from django.conf.urls import include,url,patterns
from cart.models import Cart
from . import views
from django.conf import settings


urlpatterns=patterns('',
    url(r'^$',views.get_cart,name='get_cart'),
)
