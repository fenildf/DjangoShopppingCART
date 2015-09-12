from django.conf.urls import include, url,patterns
from products.models import Product
from . import views

urlpatterns=patterns('',
#    'django'.views.generic.list_detail',
    url(r'^$',views.index,name='index'),
    url(r'^(?P<slug>[\w\-]+)/$',views.p_detail,name='p_detail'),    
    
)

