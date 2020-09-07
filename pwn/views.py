from django.shortcuts import render,redirect
from pwn.models import AdminLoginModel,CityModel,StateModel,CuisineModel
from django.contrib import messages


def showIndex(request):
    return render(request,"pwn/login.html")


def pwn_login_check(request):
    if request.method == "POST":
        try:
            admin = AdminLoginModel.objects.get(username=request.POST.get("pwn_username"),
                                                password=request.POST.get("pwn_password"))
            request.session["admin_status"] = True
            return redirect('welcome')
        except:
            return render(request, "pwn/login.html", {"error": "Invalid User"})
    else:
        request.session["admin_status"] = False
        return render(request, "pwn/login.html", {"error": "Admin Logout Success"})



def welcome(request):
    return render(request,"pwn/home.html")


def openVendor(request):
    return render(request,"pwn/openvendor.html")

def openReporsts(request):
    return render(request,"pwn/openreports.html")

 #---------------STATE--------------#

def openState(request):
    sm=StateModel.objects.all()
    return render(request, 'pwn/openstate.html', {"data":sm })


def addstate(request):
    state=request.POST.get('s1')
    photo=request.FILES["s2"]
    StateModel(name=state,photo=photo).save()
    messages.success(request,"State Added Successfully")
    return redirect('addstate')


def update(request):
    no = request.GET.get("id")
    p_data = StateModel.objects.get(id=no)
    return render(request, "pwn/openstate.html", {"pdata": p_data,"data":StateModel.objects.all()})


def updatestate(request):
    n = request.POST.get("s1")
    i = request.FILES["s2"]
    id=request.POST.get("s3")

    StateModel.objects.filter(id=id).update(name=n,photo=i)
    return redirect('addstate')


def delete(request):

    print(request.GET.get("id"))
    print(type(request.GET.get("id")))
    StateModel.objects.get(id=request.GET.get("id")).delete()
    return redirect('addstate')

#-----------CITY--------------#

def openCity(request):
    return render(request,"pwn/opencity.html",{"data":StateModel.objects.all(),"data1": CityModel.objects.all()})


def addCity(request):
    city = request.POST.get('c1')
    photo = request.FILES['c2']
    state=request.POST.get('c3')
    CityModel(name=city, photo=photo,city_state_id=state).save()

    messages.success(request,"City Added Successfully")
    return redirect('city')


def updateC(request):
    no = request.GET.get("id")
    p_data = CityModel.objects.get(id=no)
    return render(request, "pwn/opencity.html", {"pdata": p_data,"data":StateModel.objects.all(),"data1": CityModel.objects.all()})


def updateCity(request):
    n = request.POST.get("c1")
    i = request.FILES["c2"]
    id = request.POST.get("c3")
    s=request.POST.get("c4")


    CityModel.objects.filter(id=id).update(name=n, photo=i,city_state_id=s)
    return redirect('addcity')

def deleteCity(request):
    id=request.GET.get("id")
    CityModel.objects.filter(id=id).delete()
    return redirect('addcity')

  #-----------CUISINE---------------#

def openCusine(request):
    return render(request,"pwn/opencuisine.html",{"data": CuisineModel.objects.all()})

def addCuisine(request):
    cuisine=request.POST.get("cu1")
    img=request.FILES["cu2"]
    CuisineModel(type=cuisine,photo=img).save()
    messages.success(request,"Cuisene Type Added Successfully")
    return redirect('cuisine')

def updatecuisine(request):
    no = request.GET.get("id")
    cdata = CuisineModel.objects.get(id=no)
    return render(request, "pwn/opencuisine.html", {"c_data": cdata,"data":CuisineModel.objects.all()})


def cuisineTypeUpdate(request):
    cun = request.POST.get("cu1")
    cuimg = request.FILES["cu2"]
    cuid = request.POST.get("cu3")


    StateModel.objects.filter(id=cuid).update(name=cun, photo=cuimg)
    return redirect('addcuisine')


def deletecuisine(request):
    id = request.GET.get("id")
    CuisineModel.objects.filter(id=id).delete()
    return redirect('addcuisine')
