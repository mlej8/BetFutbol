from django import forms
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404

# Global variable for User model. Instead of importing the User model from Django.contrib.auth, get_user_model will use the default Django User model if no custom model was defined and use the custom model if it was defined.
User = get_user_model() 

class UserLoginForm(forms.Form): # this class inherits from Django's Form class. Forms allow us to custom way to capture user data
    username = forms.CharField() # every class variables are used to create the forms (in this case it will create a first input field with label "Email:")
    password = forms.CharField(widget=forms.PasswordInput) # treat this field as a password text input

    def clean(self, *args, **kwargs): # applied everytime the form is submitted, it is a way of ensuring that information passed in is what you want to be. Ensure that we pass in *args and **kwargs
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
       
        # check both email and password are passed in verify if this user exists and that the password matches the username, mark it as authenticated
        if username and password:           
           
            user = authenticate(username=username, password=password)  # if the given credentials are valid, authenticate returns a User object.
            if user is not None: # backend authenticated with credentials
                user = get_object_or_404(User, username=username) # get the user object
            else: # no backend authenticated the credentials
                raise forms.ValidationError("User does not exist") # raise validation error on the Django form            
            
        # if user is authenticated call the clean method from the super class
        return super(UserLoginForm, self).clean(*args, **kwargs)


class UserRegistrationForm(UserCreationForm): # inherit from UserCreationForm
    
    username = forms.CharField(label='Username')
    first = forms.CharField(label='First Name')
    last = forms.CharField(label='Last Name')
    email = forms.EmailField(label='Email Address') # if label attribute is not specified it will use the class variable to create a label 
    password1 = forms.CharField(widget=forms.PasswordInput, label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta: # add class Meta so we can specify the model
        model = User # the model we are using is User
        fields = [ # order of the fields in the form
            'username',
            'first',
            'last',
            'email',
            'password1',
            'password2',
        ]
    
    def clean(self,*args, **kwargs):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError("Password must match.")
        
        # check if this email exists 
        email_qs = User.objects.filter(email=email)

        # if the query set is not empty, means that someone already has the eamil, throw error
        if email_qs.exists(): 
            raise forms.ValidationError("This email is already used.")
        return super(UserRegistrationForm, self).clean(*args, **kwargs) # otherwise call superclass' clean method.


    

        