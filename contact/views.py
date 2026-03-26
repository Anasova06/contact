from django.shortcuts import render , redirect
from .models import Contact
from .forms import ContactForm
def home(request):
    return render(request,'home.html')
def contact(request):
    contacts = Contact.objects.filter(is_active=True)
    return render(request, 'contact.html', {'contacts': contacts})

def contact_create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'contact_book.html', {'form': form})