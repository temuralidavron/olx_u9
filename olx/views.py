
from django import forms
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from account.models import CustomUser
from account.utils import check_user, send_simple_email, send_html_email
from .forms import OrderForm
from .models import Product, Order, Category


# cat detail


def get_cat(request,pk):
    cat=Category.objects.get(pk=pk)
    products=Product.objects.filter(category=cat)
    context={
        'cat':cat,
        'products':products
    }
    return render(request,'cat/detail.html',context)

def product_list(request):
    # send_simple_email()
    # send_html_email()
    products=Product.objects.all()[:5]
    cats=Category.objects.all()


    context={
        'products':products,
        'cats':cats,

    }

    return render(request,'product/list.html',context)


def product_detail(request,pk):
    product=Product.objects.get(pk=pk)
    context={
        'product':product
    }
    return render(request,"product/detail.html",context)


# sotib olish order create
# @login_required
@check_user
def create_order(request,pk):
    pk=Product.objects.get(pk=pk)
    if request.method=='POST':
        form=OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            if order.quantity>pk.quantity:
                return redirect('product-list')
            order.product=pk
            order.user = request.user
            user=CustomUser.objects.get(username=request.user)
            send_html_email(
                to_user=user.email,
                product_title=pk.title,
                product_price=pk.price,
                product_qn=order.quantity,
                total_price=(pk.price*order.quantity)


            )
            order.save()
            return redirect('product-list')
    else:
        form=OrderForm()
    return render(request,'order/create.html',{'form':form,'product':pk})
