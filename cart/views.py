from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from cart.models import Cart
from products.models import Product


#def view(request):
#        if the_id:
#                cart=Cart.objects.get(id=the_id)
#                context={"cart":cart}

#        else:
#                empty_message="your Cart is Empty,please keep shopping."
#                context={ "empty" :True,"empty_message":empty_message }
        
#        template="cart/view.html"
#        return render(request,template,context) 


def add_to_cart(request,product_id,quantity):
    product=Product.objects.get(id=product_id)
    cart=Cart(request)
    cart.add(product,product.unit_price,quantity)


def remove_from_cart(request,product_id):
    product = Product.objects.get(id=product_id)
    cart = Cart(request)
    cart.remove(product)

def get_cart(request):
   # return render(request,'cart/cart.html',dict(cart=Cart(request))) 
    return render_to_response('cart/cart.html', dict(cart=Cart(request)))

#def index(request):
#    return render_to_response('cart/cart.html',
#    {
#      'cart':Cart.objects.all(),
#    },
#    context_instance=RequestContext(request))
# Create your views here.
