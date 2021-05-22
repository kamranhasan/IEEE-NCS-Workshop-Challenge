from django.shortcuts import render
from .forms import ContactForm
from .models import Contact
# Create your views here.
def home(request):
    contactform = ContactForm()
    return render(request, 'index.html',context={'contactform':contactform, 'respond3':'Send Message'}) 

def contacted(request):
    contactform = ContactForm()
    print('1')
    if request.method == 'POST':
        print('2')
        data = ContactForm(request.POST)
        if data.is_valid():
            print('3')
            data.save()
            return render(request, 'index.html',context={'respond3':'Your Message Has Been Sent Successfully'}) 
        else:
            print('4')
            return render(request, 'index.html',context={'contactform':contactform, 'respond3':'Your Message Has Not Been Sent Successfully'}) 
    print('5')
    return render(request, 'index.html',context={'contactform':contactform, 'respond3':'Send Message'}) 
        
def checked(request):
    return render(request, 'index.html',context={}) 
def booked(request):
    return render(request, 'index.html',context={}) 
