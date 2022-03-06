from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse , HttpResponseRedirect
from django.db.models import Q

from .models import Bike, Order, PrivateMsg
from .forms import BikeForm, OrderForm, MessageForm



# Create your views here.
def home(request):
    context = {
        "title" : "Bike Rental"
    }
    return render(request,'home.html', context)

def bike_list(request):
    bike = Bike.objects.all()
    print(bike)
    query = request.GET.get('q')
    if query:
        bike = bike.filter(
                     Q(bike_name__icontains=query) |
                     Q(company_name__icontains = query) |
                     Q(cost_par_day__icontains=query)
                            )
    
    # pagination
    paginator = Paginator(bike, 12)  # Show 15 contacts per page
    page = request.GET.get('page')
    try:
        bike = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        bike = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        bike = paginator.page(paginator.num_pages)
    context = {
        'bike': bike,
    }
    
    return render(request, 'bike_list.html', context)

def bike_detail(request, id=None):
    detail = get_object_or_404(Bike,id=id)
    context = {
        "detail": detail
    }
    return render(request, 'bike_detail.html', context)

def bike_created(request):
    form = BikeForm(request.POST or None, request.FILES or None)
    
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect("/")
    context = {
        "form" : form,
        "title": "Create Bike"
    }
    return render(request, 'bike_create.html', context)

def bike_update(request, id=None):
    detail = get_object_or_404(Bike, id=id)
    form = BikeForm(request.POST or None, instance=detail)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect("/bike/newbike/")
    context = {
        "form": form,
        "title": "Update Bike"
    }
    return render(request, 'bike_create.html', context)

def bike_delete(request,id=None):
    query = get_object_or_404(Bike,id = id)
    query.delete()

    bike = Bike.objects.all()
    context = {
        'bike': bike,
    }
    return render(request, 'admin_index.html', context)
#order

def order_list(request):
    order = Order.objects.all()

    query = request.GET.get('q')
    if query:
        order = order.filter(
            Q(bike_name__icontains=query)|
            Q(employee_name__icontains=query)
        )

    # pagination
    paginator = Paginator(order, 4)  # Show 15 contacts per page
    page = request.GET.get('page')
    try:
        order = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        order = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        order = paginator.page(paginator.num_pages)
    context = {
        'order': order,
    }
    return render(request, 'order_list.html', context)

def order_detail(request, id=None):
    detail = get_object_or_404(Order,id=id)
    context = {
        "detail": detail,
    }
    return render(request, 'order_detail.html', context)

def order_created(request):
    form = OrderForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect("/bike/newbike/")

    context = {
        "form": form,
        "title": "Create Order"
    }
    return render(request, 'order_create.html', context)

def order_update(request, id=None):
    detail = get_object_or_404(Order, id=id)
    form = OrderForm(request.POST or None, instance=detail)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect("/bike/newbike/")
    context = {
        "form": form,
        "title": "Update Order"
    }
    return render(request, 'order_create.html', context)

def order_delete(request,id=None):
    query = get_object_or_404(Order,id = id)
    query.delete()
    return HttpResponseRedirect("/listOrder/")

#-----------------Admin Section-----------------

def admin_bike_list(request):
    bike = Bike.objects.order_by('-id')

    query = request.GET.get('q')
    if query:
        bike = bike.filter(
            Q(bike_name__icontains=query) |
            Q(company_name__icontains=query) |
            Q(cost_par_day__icontains=query)
        )

    # pagination
    paginator = Paginator(bike, 12)  # Show 15 contacts per page
    page = request.GET.get('page')
    try:
        bike = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        bike = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        bike = paginator.page(paginator.num_pages)
    context = {
        'bike': bike,
    }
    return render(request, 'admin_index.html', context)

def admin_msg(request):
    msg = PrivateMsg.objects.order_by('-id')
    context={
        "bike": msg,
    }
    return render(request, 'admin_msg.html', context)

def msg_delete(request,id=None):
    query = get_object_or_404(PrivateMsg, id=id)
    query.delete()
    return HttpResponseRedirect("/message/")



def newbike(request):
    new = Bike.objects.order_by('-id')
    #seach
    query = request.GET.get('q')
    if query:
        new = new.filter(
            Q(bike_name__icontains=query) |
            Q(company_name__icontains=query) |
            Q(cost_par_day__icontains=query)
        )

    # pagination
    paginator = Paginator(new, 12)  # Show 15 contacts per page
    page = request.GET.get('page')
    try:
        new = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        new = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        new = paginator.page(paginator.num_pages)
    context = {
        'bike': new,
    }
    return render(request, 'new_bike.html', context)

def like_update(request, id=None):
    new = Bike.objects.order_by('-id')
    like_count = get_object_or_404(Bike, id=id)
    like_count.like+=1
    like_count.save()
    context = {
        'bike': new,
    }
    return render(request,'new_bike.html',context)


def contact(request):
    form = MessageForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect("/car/newcar/")
    context = {
        "form": form,
        "title": "Contact With Us",
    }
    return render(request,'contact.html', context)