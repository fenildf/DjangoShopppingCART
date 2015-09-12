from django.shortcuts import render
from products.models import Product,CatalogCategory
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response,get_object_or_404

def index(request):
    return render_to_response('products/index.html',
    {
      'products':Product.objects.all().order_by('?'),
      
     },
     context_instance=RequestContext(request))
     


def p_detail(request,slug):
    show=get_object_or_404(Product,slug=slug)
    return render_to_response('products/p_detail.html',
    {
	'p_detail':Product.objects.filter(name=show),
    },
	context_instance=RequestContext(request))
	 	
# Create your views here.
