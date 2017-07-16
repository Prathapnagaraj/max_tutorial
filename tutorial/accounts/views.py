from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def home(request):
    name="Sam"
    args={'Myname':name, "numbers":[1,2,3,4,5,6]}
    return render(request, 'accounts/home.html', args)

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save();
            return redirect("/account")
    else:
        form= UserCreationForm()
        args = {'form':form}
        return render(request, 'accounts/reg_form.html', args)

