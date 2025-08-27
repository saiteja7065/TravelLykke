from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Booking, TravelOption, UserProfile


def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, 'Registration successful!')
			return redirect('home')
		else:
			for field, errors in form.errors.items():
				for error in errors:
					messages.error(request, f"{field}: {error}")
	else:
		form = UserCreationForm()
	return render(request, 'register.html', {'form': form})

def home(request):
	return render(request, 'home.html')

@login_required
def book_travel(request, travel_id):
	travel_option = get_object_or_404(TravelOption, travel_id=travel_id)
	if request.method == 'POST':
		seats_str = request.POST.get('seats', '1')
		try:
			seats = int(seats_str)
		except ValueError:
			messages.error(request, 'Please enter a valid number of seats.')
			return render(request, 'book_travel.html', {'travel_option': travel_option})
		if seats < 1 or seats > travel_option.available_seats:
			messages.error(request, 'Invalid number of seats selected.')
		else:
			total_price = travel_option.price * seats
			booking = Booking.objects.create(
				user=request.user,
				travel_option=travel_option,
				number_of_seats=seats,
				total_price=total_price,
				status='Confirmed'
			)
			travel_option.available_seats -= seats
			travel_option.save()
			messages.success(request, 'Booking successful!')
			return redirect('my_bookings')
	return render(request, 'book_travel.html', {'travel_option': travel_option})

@login_required
def profile(request):
	user_profile, created = UserProfile.objects.get_or_create(user=request.user)
	if request.method == 'POST':
		full_name = request.POST.get('full_name', '').strip()
		email = request.POST.get('email', '').strip()
		phone = request.POST.get('phone', '').strip()
		errors = []
		if not full_name:
			errors.append('Full name is required.')
		if not email:
			errors.append('Email is required.')
		if not phone:
			errors.append('Phone is required.')
		if errors:
			for error in errors:
				messages.error(request, error)
		else:
			user_profile.full_name = full_name
			user_profile.email = email
			user_profile.phone = phone
			user_profile.save()
			messages.success(request, 'Profile updated successfully!')
			return redirect('profile')
	return render(request, 'profile.html', {'profile': user_profile})


@login_required
def cancel_booking(request, booking_id):
	booking = get_object_or_404(Booking, booking_id=booking_id, user=request.user)
	if request.method == 'POST':
		booking.delete()
		messages.success(request, 'Booking cancelled successfully!')
		return redirect('my_bookings')
	return render(request, 'cancel_booking.html', {'booking': booking})
@staff_member_required
def admin_dashboard(request):
	return render(request, 'admin_dashboard.html')

@staff_member_required
def add_travel_option(request):
	if request.method == 'POST':
		type = request.POST.get('type')
		source = request.POST.get('source')
		destination = request.POST.get('destination')
		date_time = request.POST.get('date_time')
		price = request.POST.get('price')
		available_seats = request.POST.get('available_seats')
		if not all([type, source, destination, date_time, price, available_seats]):
			messages.error(request, 'All fields are required.')
		else:
			TravelOption.objects.create(
				type=type,
				source=source,
				destination=destination,
				date_time=date_time,
				price=price,
				available_seats=available_seats
			)
			messages.success(request, 'Travel option added successfully!')
			return redirect('travel_options')
	return render(request, 'add_travel_option.html')

def login_view(request):
	if request.method == 'POST':
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			user = form.get_user()
			login(request, user)
			return redirect('travel_options')
		else:
			messages.error(request, 'Invalid username or password.')
	else:
		form = AuthenticationForm()
	return render(request, 'login.html', {'form': form})

def logout_view(request):
	logout(request)
	return redirect('/')

def travel_options(request):
	source = request.GET.get('source', '')
	destination = request.GET.get('destination', '')
	date_time = request.GET.get('date_time', '')
	options = TravelOption.objects.all()
	if source:
		options = options.filter(source__icontains=source)
	if destination:
		options = options.filter(destination__icontains=destination)
	if date_time:
		options = options.filter(date_time__date=date_time)
	return render(request, 'travel_options.html', {
		'options': options,
		'source': source,
		'destination': destination,
		'date_time': date_time
	})

@login_required
def my_bookings(request):
	bookings = Booking.objects.filter(user=request.user).order_by('-booking_id')
	return render(request, 'my_bookings.html', {'bookings': bookings})
