from django.shortcuts import render
from subscribeApp.models import Customer
from subscribeApp.forms import NewSubscriber
# Create your views here.
def index(request):
    return render(request, 'subscribeApp/index.html')
def customers(request):
    customer_list = Customer.objects.order_by('first_name')
    customer_dict = {'customers' :customer_list}
    return render(request, 'subscribeApp/customers.html', context=customer_dict)

def subscribe(request):
    form = NewSubscriber()
    
    if request.method == "POST":
        form = NewSubscriber(request.POST)
        
        if form.is_valid():
            form.save(commit=True)
            return customers(request)
        else:
            print("eror:form invalid")
            
    return render(request, 'subscribeApp/subscribe.html',{'form':form})