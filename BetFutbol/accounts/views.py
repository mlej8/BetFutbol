from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,get_user_model, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test 
from .forms import UserLoginForm, UserRegistrationForm
from django.urls import reverse

def is_not_authenticated(user):
    return not user.is_authenticated

@user_passes_test(is_not_authenticated, login_url="/") # perform a redirect to home page if the user is already authenticated (is_not_logged_in will return False)    
def login_view(request):
    if request.method == "POST":
        next = request.POST.get('next') # get the value of next to redirect the user
        form = UserLoginForm(request.POST) # set form equal to login form
        if form.is_valid(): # if form is valid, start doing the cleaning
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password ) # takes credentials as keyword arguments, username and password for the default case, checks them against each authentication backend, and returns a User object if the credentials are valid for a backend. If the credentials aren’t valid for any backend or if a backend raises PermissionDenied, it returns None.
            
            if user is not None:
                login(request, user)
                # Redirect to a success page.
                ...
                if next: # see if there was a next value, if there is redirect to next.
                    return redirect(next)
                else:
                    return redirect('/') # otherwise return to home page
            else:
                print("Failed to authenticate user") # TODO: redirect to failed authenticataion page
    elif request.method == "GET":
        next = request.POST.get('next')
        form = UserLoginForm()      

    context = {'form': form}
    return render(request, "accounts/login.html", context=context)

def register_view(request):
    if request.method == "POST": 
        next = request.POST.get('next') # get the value of next to redirect the user
        form = UserRegistrationForm(request.POST) 
        if form.is_valid(): # if form is valid, start doing the cleaning
            user = form.save(commit=False) # add commit=False to tell it to not save it in the database yet, form.save() will create a user using the attributes on the form 
            password = form.cleaned_data.get('password') # set the password on the user
            user.set_password(password) # Sets the user’s password to the given raw string, taking care of the password hashing.
            user.first_name = form.cleaned_data["first"]
            user.last_name = form.cleaned_data["last"]
            user.email = form.cleaned_data["email"]
            user.is_staff = False # does not have access to the admin site
            user.is_active = False # at first the user is inactive until admin activates it
            user.is_superuser = False # no superuser is created form UserRegistrationForm
            user.save() # save this new user to database
            new_user = authenticate(username=user.username, passowrd=user.password) # authenticate new_user 

            if new_user is not None:
                # TODO: send an email to admin to activate that user. 
                login(request, new_user) # login new user                
                if next: # see if there was a next value, if there is -> redirect to next.
                    return redirect(next)
                else:
                    return redirect('/') # otherwise return to home page
            else: 
                print("Failed to authenticate user") # TODO: redirect to failed authenticataion
    else:
        form = UserRegistrationForm() 

    context = {'form': form}
    return render(request, "accounts/register.html", context=context)

@login_required
def logout_view(request):
    logout(request)
    return redirect(reverse('FutbolPredictor:predictions')) # redirect to home page.

@login_required # this makes this a protected view that only authenticated users can view. In addition, if not logged in, it will automatically redirect to /accounts/login/ then set the current page as the "next" parameter which says that once we've logged in it will redirect to the current page.
def profile_view(request):
    return render(request, 'accounts/userprofile.html', {})