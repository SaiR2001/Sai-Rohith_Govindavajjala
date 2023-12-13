# contacts/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Contact
from .forms import ContactForm

def contact_list(request):
    contacts = Contact.objects.all().order_by('-created_at')  # Order by created_at in descending order
    return render(request, 'contacts/contact_list.html', {'contacts': contacts})

def new_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contacts:contact_list')
    else:
        form = ContactForm()

    return render(request, 'contacts/new_contact.html', {'form': form})

def contact_detail(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)
    return render(request, 'contacts/contact_detail.html', {'contact': contact})

def contact_edit(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)

    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contacts:contact_detail', contact_id=contact.id)
    else:
        form = ContactForm(instance=contact)

    return render(request, 'contacts/contact_edit.html', {'form': form, 'contact': contact})

def contact_delete(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)
    if request.method == 'POST':
        contact.delete()
        return redirect('contacts:contact_list')
    return render(request, 'contacts/contact_delete.html', {'contact': contact})
