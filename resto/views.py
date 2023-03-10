from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views import View
from django.utils.timezone import datetime
# from stripe import client_id
from products.models import OrderModel,products,comment
from .forms import item_creation
from requests import request
# from django.contrib.auth.forms import UserCreationForm
# from .forms import RegisterUserForm

def login_user(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('dash')
		else:
			messages.success(request, ("There Was An Error Logging In, Try Again..."))	
			return redirect('login')	


	else:
		return render(request, 'resto/login.html', {})
def logout(request):
    return render(request, 'resto/login.html', {})
# def dash(request):
#     return render(request,'resto/dash.html',{})


class dash(View):
    def get(self, request, *args, **kwargs):
        # get the current date
        today = datetime.today()
        tshiped=0
        tnshiped=0
        ttshiped=0
        ttnshiped=0
        orders = OrderModel.objects.filter(
            created_on__year=today.year, created_on__month=today.month, created_on__day=today.day)
        ordersm = OrderModel.objects.filter(
            created_on__year=today.year,created_on__month=today.month)

        # loop through the orders and add the price value
        total_revenue = 0
        for order in orders:
            total_revenue += order.price
            if order.isshiped == True:
                ttshiped =ttshiped +1
            if order.isshiped == False:
                ttnshiped =ttnshiped +1
    
        
        total_revenuem = 0
        for order2 in ordersm:
            total_revenuem += order2.price
            if order2.isshiped == True:
                tshiped =tshiped +1
            if order2.isshiped == False:
                tnshiped =tnshiped +1
                

        # pass total number of orders and total revenue into template
        context = {
            'orders': orders,
            'total_revenue': total_revenue,
            'total_orders': len(orders),
            'ordersm': ordersm,
            'total_revenuem': total_revenuem,
            'total_ordersm': len(ordersm),
            'shiped_orders':tshiped,
            'non_shped_order':tnshiped,
            'today_shped_order':ttshiped,
            'today_non_shiped_order':ttnshiped,
        }

        return render(request, 'resto/dash.html', context)

    # def test_func(self):
    #     return self.request.user.groups.filter(name='Staff').exists()

class manipulation(View):
    def post(self, request,pk,*args,**kwargs):
        order_id=self.kwargs["pk"]
        order=OrderModel.objects.get(id=order_id)
        order.isshiped =True
        order.ispayed=True
        order.save()
        context={
            'model':order,
        }
        return render(request, 'resto/order_manipulation.html',context)

    def get(self, request, *args, **kwargs):
        order_id=self.kwargs["pk"]
        model=OrderModel.objects.get(id=order_id)
        context={
            'model':model,
            # 'client_id':model.id,
            # 'price':model.price,
            # 'name':model.namecl,
            # 'email':model.email,
                    }
        return render(request, 'resto/order_manipulation.html',context)

class review_manipulation(View):
    def post(self, request,pk,*args,**kwargs):
        review_id=self.kwargs["pk"]
        review=comment.objects.get(id=review_id)
        # print(review_id)
        if review.is_showen == True:
            review.is_showen =False
            review.save()
        else:
            review.is_showen =True
            review.save()
        context={
            'rev':review
            }
        return render(request, 'resto/review_manipulation.html',context)

    def get(self, request, *args, **kwargs):
        review_id=self.kwargs["pk"]
        review=comment.objects.get(id=review_id)
        context={
            'rev':review,
           
                    }
        return render(request, 'resto/review_manipulation.html',context)
    
class Menu(View):
    def get(self, request, *args, **kwargs):
        menuu=products.objects.all()
        # print(menu.Category)
        context={
            'menuu':menuu,
        }
        return render(request,'resto/menu.html',context)

def deletem(request,pk):
    menu_d = products.objects.get(id=pk)
    print(menu_d.price)
    if request.method == 'GET':
        print(menu_d.price)
        menu_d.delete()
        menu=products.objects.all()
        context={
        'menu':menu,
    }
        return redirect('menu')
    menu=products.objects.all()
    context={
    'menu':menu,
    }
    return redirect('menu',context)

def orderCreation(request):
    form =item_creation()
    if request.method == 'POST':
        form = item_creation(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('menu')
        else :
            print("mablanch")
       

    context={
        'form':form,
    }
    return render(request,'resto/menu_item_creation.html',context)

def updateOrder(request, pk):
    menu= products.objects.get(id=pk)
    form =item_creation(instance=menu)
    if request.method == 'POST':
        form = item_creation(request.POST, instance=menu)
        if form.is_valid():
            form.save()
            return redirect('menu')
    context = {'form':form}
    return render(request, 'resto/update.html', context)

def review_dash(request):
    review=comment.objects.all()
    context={
        'review':review,
    }
    return render(request, 'resto/review_dash.html', context)







# menu_id = self.request.POST['pk']
        # menu_id=self.kwargs["pk"]
        # if request.method == "GET":
        #     print(menu_id)
        #     return redirect('menu')















 # # print(request.POST)
        # form= item_creation(request.POST)
        # name=request.POST['name']
        # # print(request.POST['img'])
        # img=request.POST['img']
        # price=request.POST['price']
        # category=request.POST['category']
        # # category=int(category) 
        # # catdic = {
        # #     1: "drink",
        # #     2: "sandwich",
        # #     3: "plat",
        # #     4:"drink" }
        # # cat=catdic[category]
        # item = products.objects.create(price=price,name=name )
        # item.category.set(category)

        # print(img)
        # if form.is_valid():
        #     form.save()
        #     return redirect('resto/menu.html')
        # else :
        #     print("mablanch")