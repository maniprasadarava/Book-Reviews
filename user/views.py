from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from bookvendor.models import upload
from user.forms import userForm, feedbackform
from user.models import userdata, feedback
from user.words import positive_words, negative_words


def userlogin(request):
    return render(request,"user/userlogin.html")

def userpage(request):
    return render(request,"user/userpage.html")


def userlogincheck(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        print(uname)
        upasswd = request.POST.get('upasswd')
        print(upasswd)
        try:
            check = userdata.objects.get(name=uname, passwd=upasswd)
            # print('usid',usid,'pswd',pswd)
            request.session['name'] = check.name
            print("name",check.name)
            status = check.status
            print(status)
            if status == "Activated":
                request.session['mail'] = check.mail
                return render(request, 'user/userpage.html')
            else:
                messages.success(request, 'user is not activated')
                return render(request, 'user/userlogin.html')

        except Exception as e:
            print('Exception is ', str(e))
            messages.success(request, 'Invalid user id and password')
        return render(request, 'user/userlogin.html')

def userregister(request):
    if request.method=='POST':
        form1=userForm(request.POST)
        if form1.is_valid():
            print("form is saved")
            form1.save()

            return render(request, "user/userlogin.html")
            #return HttpResponse("registreration succesfully completed")
        else:
            print("form not valied")
            return HttpResponse("form not valied")
    else:
        form=userForm()
        return render(request,"user/userregister.html",{"form":form})



def reviewofbooks(request):
    return render(request, 'user/usersearch1.html')

def usersearchresult1(request):
    pos, neg = 0, 0
    semantic = 'pending'
    bookname = request.GET.get('type')
    qs=feedback.objects.filter(bookname=bookname)
    pt=[]
    nt=[]
    for x in qs:
        cmmnt=x.review
        for pword in positive_words:
            if pword in cmmnt:
                pos=pos+1
                pt.append(cmmnt)
        for nword in negative_words:
            if nword in cmmnt:
                neg=neg+1
                nt.append(cmmnt)

    if pos>neg:
        semantic='positive'
    elif pos<neg:
        semantic='negative'
    elif pos==neg:
        semantic = 'nutral'
    print(pt)
    print(nt)
    return render(request,"user/bookreview.html",{"qs":qs,"sem":semantic,"dict":pt,"dict1":nt})

def search(request):
    return render(request, 'user/usersearch.html')

def usersearchresult(request):
    booktype = request.GET.get('type')
    print('product is', property, ' and its type ', type(property))
    check = upload.objects.filter(filetype=booktype)
    print(check)
    object = check.filter(filetype=booktype)
    return render(request, 'user/usersearchresult.html', {"object": object})


def viewdetails(request):
    if request.method == 'POST':
        form=feedbackform(request.POST)
        if form.is_valid():
            form.save()
            #return HttpResponse("successfully commented on book")
            return render(request, 'user/usersearch.html')
        else:
            print("form not valied")
            return HttpResponse("un-successfully commented on book")
            #return render(request,'user/viewdetails.html')
    else:
        id = request.GET.get('id')
        print('Image Id  = ', id)
        bkname1 = request.GET.get('filename')
        bktype1= request.GET.get('filetype')
        bkprice1= request.GET.get('fileprice')
        file = request.GET.get('file')
        print('bkname = ', bkname1, ' bkprice', bkprice1)
        data = upload.objects.get(id=id)
        data2 = {'bookname':data.filename, 'booktype':data.filetype, 'bookprice':data.fileprice}
        viewbooks= feedbackform(data2)
        return render(request, 'user/viewdetails.html', {'books':viewbooks ,'price':bkprice1, 'image':data.file})
