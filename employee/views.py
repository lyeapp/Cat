from django.shortcuts import redirect,render
from .models import employee_details
# Create your views here.
def addProduct(request):
    return render(request,'pro.html')

def add_product_details(request):
    if request.method=='POST':
        employeeid=request.POST['employeeid']
        employeename=request.POST['employeename']
        email=request.POST['email']
        cn=request.POST['cn']
        dob=request.POST['dob']
        
        product=employee_details(employeeid=employeeid,
                          employeename=employeename,
                          employeeemail=email,
                          employeecontact=cn,
                          employeedob=dob,)
        product.save()
        print("successfully done")
        return redirect('show_products')

def show_products(request):
    products=employee_details.objects.all()
    return render(request,'show.html',{'products':products})

def editpage(request,pk):
     products=employee_details.objects.get(id=pk)
     return render(request,'edit.html',{'products':products})

def edit_product_details(request,pk):
    if request.method=='POST':
        products=employee_details.objects.get(id=pk)
        products.employeeid = request.POST.get('employeeid')
        products.employeename = request.POST.get('employeename')
        products.employeeemail = request.POST.get('email')
        products.employeecontact = request.POST.get('cn')
        products.employeedob = request.POST.get('dob')
        products.save() 
        print("successfully updated")
        return redirect('show_products')
    return render(request,'edit.html',)

def deletepage(request,pk):
     products=employee_details.objects.get(id=pk)
     return render(request,'delete.html',{'products':products})

def delete_product(request,pk):
     products=employee_details.objects.get(id=pk)
     products.delete()
     print("successfully deleted")
     return redirect('show_products')