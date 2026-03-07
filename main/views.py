from django.shortcuts import render, redirect, get_object_or_404
from main.models import contact as models
import main.forms as forms

from django.db.models import Count, Q
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login , logout , authenticate
from django.contrib.auth.decorators import login_required

#/ #/ #/ #/ #/ #/ Authentication #/ #/ #/ #/ #/ #/
def register_view(request):
    if request.POST:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("/home/")
        else:
            return redirect("/register/")
    form = UserCreationForm()
    return render(request, "auth_form.html", {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect("/home")
    if request.POST:
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user= authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                return redirect("/")
    form = AuthenticationForm()
    return render(request, "auth_form.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("/")


#/ #/ #/ Home page #/ #/ #/
@login_required(login_url="/")
def home(request):
    category_list = models.Category.objects.annotate(user_contacts_count=Count('contacts', filter=Q(contacts__user=request.user)))
    total_contacts = models.Contact.objects.filter(user=request.user).count()
    context={
        "total_contacts": total_contacts,
        "category_objects": category_list,
    }
    return render(request , "index.html", context)


#/ #/ #/ Add contact page #/ #/ #/
@login_required(login_url="/")
def add_contact(request):
    category_list = models.Category.objects.all()
    if request.POST:
        f_name = request.POST.get("name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        category_id = request.POST.get("category")
        address = request.POST.get("address")
        notes=request.POST.get("notes")
        models.Contact.objects.create(
            f_name=f_name,
            phone=phone,
            email=email,
            category_id=category_id,
            address=address,
            notes=notes,
            user=request.user
        )
        return redirect("/")
    context = {
        "category_list":category_list
    }
    return render(request, "add_contact.html", context)


#/ #/ #/ Add category page #/ #/ #/

def add_category(request):
    if request.POST:
        name=request.POST.get("name")
        models.Category.objects.create(
            name=name
        )
        return redirect("/add_category")
    return render(request, "add_category.html")


#/ #/ #/ Category list page #/ #/ #/

def category_list(request):
    category_list=models.Category.objects.all()
    context = {
        "category":category_list
    }
    return render(request, "category_list.html", context)


#/ #/ #/ Contact list page #/ #/ #/

def contact_list(request, category_id):
    contacts = models.Contact.objects.filter(user=request.user,category_id=category_id)
    context = {
        'contacts':contacts
    }
    return render(request, "contact_list.html", context)


#/ #/ #/ Contact detail page #/ #/ #/
@login_required(login_url="/")
def contact_detail(request, contact_id):
    contact_detail=models.Contact.objects.filter(id=contact_id)
    context = {
        'contact_detail': contact_detail
    }
    return render(request, "contact_detail.html", context)


#/ #/ #/ All contacts page #/ #/ #/

def all_contacts(request):
    all_contacts =models.Contact.objects.filter(user=request.user)

    context={
        'all_contacts':all_contacts,
    }
    return render(request, "all_contacts.html", context)


#/ #/ #/ Update contact page #/ #/ #/
def update_contact(request, contact_id):
    instance = get_object_or_404(models.Contact, pk=contact_id)
    category_list = models.Category.objects.all()

    if request.method == "POST":
        form = forms.ContactModelForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect("/home/")
    else:
        form = forms.ContactModelForm(instance=instance)

    context = {
        'form': form, 
        'contact': instance,
        'category_list': category_list
    }
    return render(request, "edit_contact.html", context)


#/ #/ #/ Delete contact page #/ #/ #/

def delete_contact(request, contact_id):
    instance= models.Contact.objects.get(id=contact_id)
    instance.delete()
    return redirect("/")


#/ #/ #/ Search page #/ #/ #/

def search(request):
    search=request.GET.get("search")
    contact_list=models.Contact.objects.all()
    if search:
        contact_list = contact_list.filter(f_name__icontains=search)

    context={
        "all_contacts":contact_list
    }
    return render(request, "all_contacts.html", context)



