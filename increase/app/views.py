from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import  *

# main home page
def index(request):
    return render(request, 'index.html')

# sends data to signup table
def Signup(request):
    if request.method== 'POST':
        email = request.POST['T1']
        name = request.POST['T2']
        ph = request.POST['T3']
        about = request.POST['T4']
        usertype = request.POST['T5']
        password = request.POST['T6']

        sin = signup()
        sin.name = name
        sin.ph = ph
        sin.about = about
        sin.email = email
        sin.save()

        log=login()
        log.email = email
        log.password = password
        log.usertype = usertype
        log.save()
        return render(request, 'index.html', {'data': "success"})
    else:
        return render(request, 'index.html')

# show login page
def Login(request):
    return render(request,'login.html')

# checks login information
def Logincheck(request):
    if request.method == 'POST':
        email = request.POST['T1']
        password = request.POST['T2']
        obj = login.objects.get(email=email, password=password)
        obj1 = signup.objects.get(email=email)
        usertype = obj.usertype
        name = obj1.name
        about = obj1.about
        request.session['usertype'] = usertype
        request.session['email'] = email
        request.session['name'] = name
        request.session['about'] = about
        if usertype == 'company':
            return HttpResponseRedirect('/companyhome/')
        elif usertype == 'developer':
            return HttpResponseRedirect('/developerhome/')
    else:
        return render(request, 'login.html')

# opens company home page
def Companyhome(request):
    if request.session.has_key('usertype'):
        usertype=request.session['usertype']
        email=request.session['email']
        name=request.session['name']
        about=request.session['about']
        if usertype=='company':
            return render(request,'companyhome.html', {'company':name, 'about':about})
        else:
            return render(request,'login.html')
    else:
        return render(request, 'login.html')

# opens developer home page
def Developerhome(request):
    if request.session.has_key('usertype'):
        usertype=request.session['usertype']
        email=request.session['email']
        name=request.session['name']
        about=request.session['about']
        if usertype=='developer':
            return render(request,'developerhome.html', {'developer':name, 'about':about})
        else:
            return render(request,'login.html')
    else:
        return render(request, 'login.html')

# opens company account page
def Companyaccount(request):
    if request.session.has_key('usertype'):
        usertype=request.session['usertype']
        email=request.session['email']
        name=request.session['name']
        about=request.session['about']
        obj1 = signup.objects.get(email=email)
        if usertype=='company':
            return render(request,'companyaccount.html', {'company':name, 'about':about, 'data':obj1})
        else:
            return render(request,'login.html')
    else:
        return render(request, 'login.html')

# update company new edit
def updatecompany(request):
    if request.method=='POST':
        email = request.session['email']
        name = request.POST['T1']
        ph = request.POST['T2']
        about = request.POST['T3']
        obj = signup.objects.get(email=email)
        obj.name = name
        obj.ph = ph
        obj.about = about
        obj.save()
        return render(request, 'companyaccount.html', {'data':obj})

# opens developer account page
def Developeraccount(request):
    if request.session.has_key('usertype'):
        usertype=request.session['usertype']
        email=request.session['email']
        name=request.session['name']
        about=request.session['about']
        obj1 = signup.objects.get(email=email)
        if usertype=='company':
            return render(request,'companyaccount.html', {'developer':name, 'about':about, 'data':obj1})
        else:
            return render(request,'login.html')
    else:
        return render(request, 'login.html')

# update developer new edit
def updatedeveloper(request):
    if request.method=='POST':
        email = request.session['email']
        name = request.POST['T1']
        ph = request.POST['T2']
        about = request.POST['T3']
        obj = signup.objects.get(email=email)
        obj.name = name
        obj.ph = ph
        obj.about = about
        obj.save()
        return render(request, 'developeraccount.html', {'data':obj})

# logout the user
def logout(request):
    try:
        del request.session['email']
        del request.session['usertype']
        del request.session['name']
    except:
        pass
    return HttpResponseRedirect('/login/')
