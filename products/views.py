# from django.shortcuts import render
# # Create your views here.
# from .models import products,Category,OrderModel

from unicodedata import name
from django.views import View
from django.shortcuts import redirect, render,get_object_or_404
from requests import request
from .models import products, Category, OrderModel,comment
from django.core.mail import send_mail


# def get(request,*args, **kwargs):
#     salade = products.objects.filter(category__name__contains='salade')
#     plat = products.objects.filter(category__name__contains='plat')
#     sandwich = products.objects.filter(category__name__contains='sandwich')
#     drinks = products.objects.filter(category__name__contains='drink')
#     context={
#         'salade': salade,
#         'plat': plat,
#         'sandwich': sandwich,
#         'drinks': drinks,
#     }
#     return render(request, "home.html", context)



def review(request):
    if request.method == "POST":
        fnamecl=request.POST.get('clname')
        email=request.POST.get('email')
        rate=request.POST.get('rating')
        gender=request.POST.get('gender')
        review=request.POST.get('comment')
        print(fnamecl)
        print(email)
        print(rate)
        print(gender)
        print(review)
        cmt=comment.objects.create(fname=fnamecl,email=email,rating=rate,gender=gender,comment=review)

        return render(request, 'home.html',{})
    else:
        return render(request,'review.html',{})
 


def home_view(request):
        salade = products.objects.filter(category__name__contains='salade')
        plat = products.objects.filter(category__name__contains='plat')
        sandwich = products.objects.filter(category__name__contains='sandwich')
        drinks = products.objects.filter(category__name__contains='drink')
        rev=comment.objects.all()
        # print(rev.fname)
        context={
            'salade': salade,
            'plat': plat,
            'sandwich': sandwich,
            'drinks': drinks,
            'rev':rev,
        }
        return render(request,'home.html', context)


   
    
        
        


# class Index(View):
#     return render(request, 'customer/index.html')

class Order(View):
    def get(self, request, *args, **kwargs):
        # get every item from each category
        salade = products.objects.filter(category__name__contains='salade')
        plat = products.objects.filter(category__name__contains='plat')
        sandwich = products.objects.filter(category__name__contains='sandwich')
        drinks = products.objects.filter(category__name__contains='drink')

        # pass into context
        context = {
            'salade': salade,
            'plat': plat,
            'sandwich': sandwich,
            'drinks': drinks,
        }

        # render the template
        return render(request, 'product/order.html', context)

    def post(self, request, *args, **kwargs):
        namecl=request.POST.get('clname')
        email=request.POST.get('email')
        number=request.POST.get('number')
        adresse=request.POST.get('adresse')
        order_items = {
            'items': []
        }

        items = request.POST.getlist('items[]')
        
        for item in items:
            menu_item = products.objects.get(pk=int(item))
            item_data = {
                'id': menu_item.pk,
                'name': menu_item.name,
                'price': menu_item.price          
            }

            order_items['items'].append(item_data)

        price = 0
        item_ids = []

        for item in order_items['items']:
            price += item['price']
            item_ids.append(item['id'])

        order = OrderModel.objects.create(price=price,namecl=namecl,email=email,number=number,adressecl=adresse )
        order.items.add(*item_ids)
        # order_f=get_object_or_404(OrderModel,pk=id)
        # order_id= self.kwargs["pk"]
        
        # title='confirmation your order'
        body=(f'hello {namecl}'' thank you for your order \n your order is begin made and will be delivred soon \n' f'your total is: {price}'
        '\n thank you for trusting us')
    
        send_mail(
            'confirmation your order',
            body,
            'mehdiezzahir27@gmail.com',
            [email],
            fail_silently=False
        )
     
        context = {
            'items': order_items['items'],
            'price': price,
            'namecl':namecl,
            'email':email,
            'number':number,
            'adresse':adresse,
            'oreder_id':order.id
        }

        return render(request, 'product/order_confi.html', context)


# for payment

import stripe
from django.conf import settings
from django.views import generic

stripe.api_key =settings.STRIPE_SECRET_KEY
endpoint_secret = settings.STRIPE_WEBHOOK_SECRET


class CreateCheckoutSessionView(generic.View):
    def post(self, request,*args,**kwargs):
        order_id=self.kwargs["pk"]
        model=OrderModel.objects.get(id=order_id)
        price=int(model.price) 
        date=model.created_on
        print(date)
        YOUR_DOMAIN = "http://127.0.0.1:8000"
        checkout_session=stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        #  'name': menu_item.name,
                        # 'price': menu_item.price
                        'currency': 'mad',
                        'unit_amount': price*100,
                        'product_data': {
                            'name': order_id,
                            # 'images': ['https://i.imgur.com/EHyR2nP.png'],
                        },
                    },
                    'quantity': 1,
                },
            ],  
            mode='payment',
            success_url=YOUR_DOMAIN + '/payment-suceess/',
            cancel_url=YOUR_DOMAIN + '/payment-cancel/',
        )
        return redirect(checkout_session.url,code=303)

def payment_succes(request):
    salade = products.objects.filter(category__name__contains='salade')
    plat = products.objects.filter(category__name__contains='plat')
    sandwich = products.objects.filter(category__name__contains='sandwich')
    drinks = products.objects.filter(category__name__contains='drink')
 
    rev=comment.objects.all()
        # pass into context
    context = {
            'salade': salade,
            'plat': plat,
            'sandwich': sandwich,
            'drinks': drinks,
            'rev':rev,
        }
   
    return render(request,'home.html', context)
        
def payment_cancel(request):
    context ={
        'payment_status':'cancel'
    }
    return render(request,'product/pay_conf.html', context)

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def my_webhook_view(request):
  payload = request.body
  sig_header = request.META['HTTP_STRIPE_SIGNATURE']
  event = None

  try:
    event = stripe.Webhook.construct_event(payload, sig_header, endpoint_secret)
  except ValueError as e:
    # Invalid payload
    return HttpResponse(status=400)
  except stripe.error.SignatureVerificationError as e:
    # Invalid signature
    return HttpResponse(status=400)

  # Handle the checkout.session.completed event
  if event['type'] == 'checkout.session.completed':
    session = event['data']['object']
    # Fulfill the purchase...
    line_item=session.list_line_items(session.id,limit=1).data[0]
    order_id=line_item['description']
    print("**********************************")
    print(order_id)
    fulfill_order(order_id)

  # Passed signature verification
  return HttpResponse(status=200)

def fulfill_order(order_id):
  order=OrderModel.objects.get(id=order_id)
  order.ispayed= True
  order.save()
  body=(f'hello {order.namecl}'' your paiment is done correctly congratulation'
        '\n thank you for trusting us')
    
  send_mail(
            'confirmation your order',
            body,
            'mehdiezzahir27@gmail.com',
            [order.email],
            fail_silently=False
        )
  
  print("Fulfilling order")




















 # order_f=get_object_or_404(OrderModel,pk=id)
        # order_id= self.kwargs["pk"]
        # print("*******************************************")
        # print(order_id)
        # order=OrderModel.objects.get(id=100)
        # print(order.price)

# items = request.POST.getlist('items[]')
#         print(items)
#         order_price = OrderModel.objects.get(pk=int(items))
#         data = {
#                 'priceT': order_price.price          
#             }
# items = request.POST.getlist('items[]')
# menu_item = products.objects.get(pk=int(items))

#  order_items = {
#             'items': []
#         }
#         items = request.POST.getlist('items[]')
        
#         for item in items:
#             menu_item = products.objects.get(pk=int(item))
#             item_data = {
#                 # 'id': menu_item.pk,
#                 'name': menu_item.name,
#                 'price': menu_item.price
#             }
#             order_items['items'].append(item_data)
#         price = 0
#         # item_ids = []

#         for item in order_items['items']:
#             price += item['price']
#             print(price)
#             # item_ids.append(item['id'])

#         # order = OrderModel.objects.create(price=price)
#         # order.items.add(*item_ids)
#         print(price)


# import json
# import stripe

# from django.conf import settings
# from django.views.generic import TemplateView
# from django.views.decorators.csrf import csrf_exempt
# from django.http import JsonResponse, HttpResponse
# from django.views import View

# class SuccessView(TemplateView):
#     template_name = "success.html"


# class CancelView(TemplateView):
#     template_name = "cancel.html"
#    product = products.objects.get(name="salade name5")
#         context = super(Order, self)
#            "product": product,
#             "STRIPE_PUBLIC_KEY": settings.STRIPE_PUBLIC_KEY
    # def get_context_data(self, **kwargs):
    #     product = products.objects.get()
    #     context = super(Order, self).get_context_data(**kwargs)
    #     context.update({
    #         "product": product,
    #         "STRIPE_PUBLIC_KEY": settings.STRIPE_PUBLIC_KEY
    #      })
    #     return context


# stripe.api_key = settings.STRIPE_SECRET_KEY

# class CreateCheckoutSessionView(View):
#     def post(self, request, *args, **kwargs):
#         product_id = self.kwargs["pk"]
#         product = products.objects.get(id=product_id)
#         YOUR_DOMAIN = "http://127.0.0.1:8000"
#         checkout_session = stripe.checkout.Session.create(
#             payment_method_types=['card'],
#             line_items=[
#                 {
#                     'price_data': {
#                         'currency': 'usd',
#                         'unit_amount': product.price,
#                         'product_data': {
#                             'name': product.name,
#                             # 'images': ['https://i.imgur.com/EHyR2nP.png'],
#                         },
#                     },
#                     'quantity': 1,
#                 },
#             ],
#             metadata={
#                 "product_id": product.id
#             },
#             mode='payment',
#             success_url=YOUR_DOMAIN + '/success/',
#             cancel_url=YOUR_DOMAIN + '/cancel/',
#         )
#         return JsonResponse({
#             'id': checkout_session.id
#         })