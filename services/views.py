from django.shortcuts import render,redirect
from .models import Service
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.contrib import messages

@login_required
def service_list(request):
    if request.user.is_seller:
        return redirect('/accounts/seller/')  # ❌ seller block

    services = Service.objects.all()
    return render(request, 'services/list.html', {'services': services})


@login_required
def add_service(request):
    if not request.user.is_seller:
        return redirect('/')

    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        price = request.POST['price']

        Service.objects.create(
            seller=request.user,
            title=title,
            description=description,
            price=price
        )
        messages.success(request, "Service added successfully!")
        return redirect('/services/my-services/')

    return render(request, 'services/add_service.html')

@login_required
def my_services(request):
    if not request.user.is_seller:
        return redirect('/')

    services = Service.objects.filter(seller=request.user)

    return render(request, 'services/my_services.html', {
        'services': services
    })

@login_required
def edit_service(request, service_id):
    service = get_object_or_404(Service, id=service_id, seller=request.user)

    if request.method == 'POST':
        service.title = request.POST['title']
        service.description = request.POST['description']
        service.price = request.POST['price']
        service.save()
        messages.success(request, "Service updated successfully!")
        return redirect('/services/my-services/')

    return render(request, 'services/edit_service.html', {
        'service': service
    })

@login_required
def delete_service(request, service_id):
    service = get_object_or_404(Service, id=service_id, seller=request.user)

    if request.method == 'POST':
        service.delete()
        messages.success(request, "Service deleted successfully!")
        return redirect('/services/my-services/')
    return render(request, 'services/delete_service.html', {
        'service': service
    })