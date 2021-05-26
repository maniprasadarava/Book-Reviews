from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from bookvendor.models import bookvendor, upload
from user.models import userdata
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix
import mysql.connector
import pandas as pd
from sklearn import datasets
from sklearn import metrics
from sklearn.naive_bayes import GaussianNB


def index(request):
    return render(request,"index.html")

def adminpage(request):
    return render(request,"admin/adminpage.html")

def adminlogin(request):
    return render(request, "admin/adminlogin.html")

def adminloginentered(request):
    if request.method == 'POST':
        uname=request.POST['uname']
        passwd=request.POST['upass']
        if uname == 'admin' and passwd=='admin':
            return render(request,"admin/adminloginentered.html")
        else:
            return HttpResponse("invalied credentials")


def viewvendordata(request):
    s=bookvendor.objects.all()
    return render(request,"admin/viewvendordata.html",{"qs":s})

def activatevendor(request):
    if request.method =='GET':
        uname=request.GET.get('pid')
        print(uname)
        status='Activated'
        print("pid=",uname,"status=",status)
        bookvendor.objects.filter(id=uname).update(status=status)
        qs=bookvendor.objects.all()
        return render(request,"admin/viewvendordata.html",{"qs":qs})

def logout(request):
    return render(request,'index.html')


def viewbooklist(request):
    s = upload.objects.all()
    return render(request, "admin/viewbookdata.html", {"qs": s})

def viewuserdata(request):
    s = userdata.objects.all()
    return render(request, "admin/viewuserdata.html", {"qs": s})

def activateuser(request):
    if request.method =='GET':
        uname=request.GET.get('pid')
        print(uname)
        status='Activated'
        print("pid=",uname,"status=",status)
        userdata.objects.filter(id=uname).update(status=status)
        qs=userdata.objects.all()
        return render(request,"admin/viewuserdata.html",{"qs":qs})



def svm(request):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="bookreview"
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT rating FROM userfeedback")
    myresult = mycursor.fetchall()
    dataset = pd.DataFrame(myresult)
    mycursor.execute("SELECT rating FROM userfeedback")
    myresult1 = mycursor.fetchall()
    dataset1 = pd.DataFrame(myresult1)
    dataset.shape
    X = dataset
    y = dataset1
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)
    svclassifier = SVC(kernel='linear')
    svclassifier.fit(X_train, y_train)
    y_pred = svclassifier.predict(X_test)
    m = confusion_matrix(y_test, y_pred)
    accurancy = classification_report(y_test, y_pred)
    print(m)
    print(accurancy)
    x = accurancy.split()
    print("Toctal splits ", len(x))
    dict = {

        "m": m,
        "accurancy": accurancy,
        'len0': x[0],
        'len1': x[1],
        'len2': x[2],
        'len3': x[3],
        'len4': x[4],
        'len5': x[5],
        'len6': x[6],
        'len7': x[7],
        'len8': x[8],
        'len9': x[9],
        'len10': x[10],
        'len11': x[11],
        'len12': x[12],
        'len13': x[13],
        'len14': x[14],
        'len15': x[15],
        'len16': x[16],
        'len17': x[17],
        'len18': x[18],
        'len19': x[19],
        'len20': x[20],
        'len21': x[21],
        'len22': x[22],
        'len23': x[23],
        'len24': x[24],
        'len25': x[25],
        'len26': x[26],
        'len27': x[27],
        'len28': x[28],
        'len29': x[29],
        'len30': x[30],
        'len31': x[31],


    }
    return render(request, 'admin/accuracy.html', dict)


def navie(request):
    dataset = datasets.load_iris()
    model = GaussianNB()
    model.fit(dataset.data, dataset.target)
    expected = dataset.target
    predicted = model.predict(dataset.data)
    accurancy = metrics.classification_report(expected, predicted)
    print("accurancy",accurancy)
    #print(metrics.classification_report(expected, predicted))
    print(metrics.confusion_matrix(expected, predicted))
    x = accurancy.split()
    print("Toctal splits ", len(x))
    dict = {

        "accurancy": accurancy,
        'len0': x[0],
        'len1': x[1],
        'len2': x[2],
        'len3': x[3],
        'len4': x[4],
        'len5': x[5],
        'len6': x[6],
        'len7': x[7],
        'len8': x[8],
        'len9': x[9],
        'len10': x[10],
        'len11': x[11],
        'len12': x[12],
        'len13': x[13],
        'len14': x[14],
        'len15': x[15],
        'len16': x[16],
        'len17': x[17],
        'len18': x[18],
        'len19': x[19],
        'len20': x[20],
        'len21': x[21],
        'len22': x[22],
        'len23': x[23],
        'len24': x[24],
        'len25': x[25],
        'len26': x[26],
        'len27': x[27],
        'len28': x[28],
        'len29': x[29],
        'len30': x[30],
        'len31': x[31],

    }
    return render(request, 'admin/navieaccuracy.html', dict)
    #return render(request,"admin/navieaccuracy.html",{"dict":a})