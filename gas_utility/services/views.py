from django.shortcuts import render, get_object_or_404, redirect
from .models import ServiceRequest, Customer
from .forms import ServiceRequestForm

def home(request):
    return render(request, 'services/home.html')


def submit_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            # Check if a customer exists
            customer = Customer.objects.first()
            if customer:  # If a customer exists, assign it to the service request
                service_request.customer = customer
                service_request.save()
                return redirect('track_requests')
            else:
                # If no customer exists, you can handle it as an error or create a default customer
                # For now, let's just show an error message
                return render(request, 'services/submit_request.html', {
                    'form': form,
                    'error': 'No customers available. Please create a customer first.',
                })
    else:
        form = ServiceRequestForm()
    return render(request, 'services/submit_request.html', {'form': form})


def track_requests(request):
    requests = ServiceRequest.objects.filter(customer=Customer.objects.first())
    return render(request, 'services/track_requests.html', {'requests': requests})
