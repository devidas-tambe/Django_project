from django.shortcuts import redirect, render, HttpResponse
from .models import register , doc1

# Create your views here.
def home(request):
    # return HttpResponse("I am home page")
    return render(request, 'login.html')

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

        return redirect('/login')  # Redirect to the login page after saving the form
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
    return render(request, 'login.html')

def login_check(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        
        user = register.objects.filter(email=email, password=password).first()
        if user:
                request.session['user_id'] = user.id  # Store user ID in session for authentication
                return redirect('/dashboard')  # Redirect to the dashboard page after successful login
        else:
                return redirect('/login')  # Redirect back to the login page if authentication fails
    else:
        return HttpResponse("Invalid request method.")
        
   

def dashboard(request):
    if request.session.get('user_id') is not None:
          # Redirect to login if user is not authenticated
        return render(request, 'dashboard.html')
    else:
        return redirect('/login')  # Redirect to login if user is not authenticated

def logout(request):
    del request.session['user_id']  # Clear the user ID from the session to log out the user
    # Clear the session or perform any necessary logout actions
    return redirect('/login')  # Redirect to the login page after logout

def addcookie(request):
    response = HttpResponse("Cookie has been set.")
    response.set_cookie('my_cookie', 'ABC')  # Set a cookie with name 'my_cookie' and value 'cookie_value'
    return response
def viewcookie(request):
    cookie_value = request.COOKIES.get('my_cookie')  # Retrieve the value of the cookie named 'my_cookie'
    if cookie_value:
        return HttpResponse(f"Cookie value: {cookie_value}")  # Display the cookie value if it exists
    else:
        return HttpResponse("Cookie not found.")  # Inform the user if the cookie does not exist

def file(request):
    return render(request,"file.html")

def filesave(request):
    if request.method=="POST":
        name = request.POST['fullname']
        photo = request.FILES['photo']

        e = doc1(fullname=name, photo=photo)
        e.save()
        return HttpResponse("file uploaded successfully")
    else:
        return HttpResponse("Fail") 
