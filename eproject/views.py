from django.shortcuts import render,redirect
from eproject.models import Product,Checkout
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
from eproject.forms import UserForm



# Create your views here.


def home(request):
    return render(request,"first.html")

@login_required
def readDetails(request):
    all_products=Product.objects.all()
    if request.method=="POST":
        itemname=request.POST.get('search')

        if itemname !='' and itemname is not None:
            all_products=all_products.filter(name__exact=itemname)
    context={
        'all_products':all_products
    }
    return render(request,"home.html",context)

class dataview(DetailView):
    model=Product

def checkout(request):

    return render(request,"checkout.html")

def formview(request):
    if request.method == "POST":
        myfname = request.POST.get("fname")
        mylname = request.POST.get("lname")
        myemail = request.POST.get("email")
        myphoneno = request.POST.get("phoneno")
        mycity = request.POST.get("city")
        mypincode = request.POST.get("pincode")
        myaddress = request.POST.get("address")
        myprice = request.POST.get("price")

        c = Checkout(firstName=myfname, lastName=mylname, emailId=myemail, phoneNo=myphoneno,
                     city=mycity, pincode=mypincode, address=myaddress, price=myprice)

        c.save()

    return render(request, "form.html")

def signUp(request):
    form = UserForm()
    if request.method=="POST":
        form=UserForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('/home')
    else:
        form = UserForm()
    return render(request, 'signup.html', {'form': form})
    


def logOut(request):
    return render(request,"logout.html")




