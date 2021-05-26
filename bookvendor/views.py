from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from bookvendor.forms import bookvendorForm, UploadfileForm
from bookvendor.models import bookvendor


def vendorlogin(request):
    return render(request,"vendor/vendorlogin.html")

def bookpage(request):
    return render(request,"vendor/bookpage.html")

def vendorregister(request):
    if request.method=='POST':
        form1=bookvendorForm(request.POST)
        if form1.is_valid():
            print("form is saved")
            form1.save()

            return render(request, "vendor/vendorlogin.html")
            #return HttpResponse("registreration succesfully completed")
        else:
            print("form not valied")
            return HttpResponse("form not valied")
    else:
        form=bookvendorForm()
        return render(request,"vendor/vendorregister.html",{"form":form})




def vendorlogincheck(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        print(uname)
        upasswd = request.POST.get('upasswd')
        print(upasswd)
        try:
            check = bookvendor.objects.get(name=uname, passwd=upasswd)
            # print('usid',usid,'pswd',pswd)
            request.session['name'] = check.name
            print("name",check.name)
            status = check.status
            print(status)
            if status == "Activated":
                request.session['mail'] = check.mail
                return render(request, 'vendor/vendorinside.html')
            else:
                messages.success(request, 'vendor is not activated')
                return render(request, 'vendor/vendorlogin.html')

        except Exception as e:
            print('Exception is ', str(e))
            messages.success(request, 'Invalid user id and password')
        return render(request, 'user/userpage.html')

def uploadbook(request):
    if request.method == 'POST':
        form = UploadfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('vendor/upload_list.html')
    else:
        form = UploadfileForm()
    return render(request, 'vendor/uploadfile.html', {'form': form})
