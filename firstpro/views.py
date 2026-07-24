from django.shortcuts import redirect, render, HttpResponse
from .models import register

# Create your views here.
def home(request):
    # return HttpResponse("I am home page")
    return render(request, 'home.html')

def about(request):
    # return HttpResponse("I am about page")
    return render(request, 'about.html')

def registration(request):
    return render(request, 'reg.html')

def saveform(request):
    if request.method == "POST":
        fullname = request.POST.get('Fullname')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        password = request.POST.get('password')

        register_data = register(Fullname=fullname, email=email, contact=contact, password=password)
        register_data.save()

        return HttpResponse("Form submitted successfully!")
    else:
        return HttpResponse("Invalid request method.")
        
def viewdata(request):
    data = register.objects.all()
    return render(request, 'viewdata.html', {'data': data})

def delete_data(request):
    id=request.GET.get('id')
    register.objects.get(id=id).delete()
    
    return redirect('/viewdata')

# def edit_data(request, id):

#     data = register.objects.get(id=id)
#     return redirect('/registration')  # Redirect to the registration page for editing

def edit_data(request):
    id = request.GET.get('id')
    data = register.objects.filter(id=id)
    return render(request, 'update.html', {'data': data})  # Redirect to the registration page for editing

def update_data(request):
    if request.method == "POST":
        id = request.POST['id']
        fullname = request.POST['Fullname']
        email = request.POST['email']
        contact = request.POST['contact']
        password = request.POST['password']

        register.objects.filter(id=id).update(Fullname=fullname, email=email, contact=contact, password=password)

        return redirect('/viewdata')  # Redirect to the viewdata page after updating
    else:
        return HttpResponse("Invalid request method.")

def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = register.objects.filter(email=email, password=password).first()
            return redirect('/viewdata')  # Redirect to the viewdata page after successful login
        except register.DoesNotExist:
            return HttpResponse("Invalid email or password.")
    else:
        return render(request, 'login.html')