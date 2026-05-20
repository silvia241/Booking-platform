from django.shortcuts import render,redirect,get_object_or_404
from .models import Booking
from services.models import Service
from .models import Booking
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from collections import defaultdict
from django.shortcuts import render, redirect


# Buyer parts are here
@login_required
def book_service(request,service_id):
    service = Service.objects.get(id=service_id)

    if request.method =='POST':
        date=request.POST['date']
        time=request.POST['time']

        Booking.objects.create(
            user=request.user,
            service=service,
            date=date,
            time=time
        )
        messages.success(request, "✅ Booking submitted! Status: Pending")
        return redirect('/services/')

    return render(request,'bookings/book.html',{'service':service})

@login_required
def my_pending_bookings(request):
    bookings = Booking.objects.filter(
        user=request.user,
        status="Pending"
    ).select_related('service')

    return render(request, 'bookings/my_pending.html', {'bookings': bookings})

@login_required
def my_accepted_bookings(request):
    bookings = Booking.objects.filter(
        user=request.user,
        status="Accepted"
    ).select_related('service')

    return render(request, 'bookings/my_accepted.html', {'bookings': bookings})

@login_required
def my_rejected_bookings(request):
    bookings = Booking.objects.filter(
        user=request.user,
        status="Rejected"
    ).select_related('service')

    return render(request, 'bookings/my_rejected.html', {'bookings': bookings})

@login_required
def my_completed_bookings(request):
    bookings = Booking.objects.filter(
        user=request.user,
        status="Completed"
    ).select_related('service')

    return render(request, 'bookings/my_completed.html', {'bookings': bookings})


# Seller part star from here
        # Seller dashboard viewing part start from here
@login_required
def pending_bookings(request):
    if not request.user.is_seller:
        return redirect('/')

    qs = Booking.objects.filter(
        service__seller=request.user,
        status="Pending"
    ).select_related('service', 'user').order_by('-id')

    grouped = defaultdict(list)
    for b in qs:
        grouped[b.service].append(b)

    return render(request, 'bookings/pending.html', {
        'grouped_bookings': dict(grouped)
    })

@login_required
def accepted_bookings(request):
    qs = Booking.objects.filter(
        service__seller=request.user,
        status="Accepted"
    ).select_related('service', 'user')

    grouped = defaultdict(list)
    for b in qs:
        grouped[b.service].append(b)

    return render(request, 'bookings/accepted.html', {
        'grouped_bookings': dict(grouped)
    })

@login_required
def rejected_bookings(request):
    if not request.user.is_seller:
        return redirect('/')

    qs = Booking.objects.filter(
        service__seller=request.user,
        status="Rejected"
    ).select_related('service', 'user').order_by('-id')

    grouped = defaultdict(list)
    for b in qs:
        grouped[b.service].append(b)

    return render(request, 'bookings/rejected.html', {
        'grouped_bookings': dict(grouped)
    })

@login_required
def completed_bookings(request):
    if not request.user.is_seller:
        return redirect('/')

    qs = Booking.objects.filter(
        service__seller=request.user,
        status="Completed"
    ).select_related('service', 'user').order_by('-id')

    grouped = defaultdict(list)
    for b in qs:
        grouped[b.service].append(b)

    return render(request, 'bookings/completed.html', {
        'grouped_bookings': dict(grouped)
    })


          #Seller actions part start from here
@login_required
def complete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)

    # security check
    if request.user == booking.service.seller:
        booking.status = "Completed"
        booking.save()
        messages.success(request, "Marked as completed!")
    return redirect('/booking/accepted/')





@login_required
def accept_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)

    if request.user == booking.service.seller:
        booking.status = "Accepted"
        booking.save()
        messages.success(request, "Booking accepted successfully!")
    return redirect('/accounts/seller/')


@login_required
def reject_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)

    if request.user == booking.service.seller:
        booking.status = "Rejected"
        booking.save()
        messages.error(request, "Booking rejected!")
    return redirect('/accounts/seller/')
