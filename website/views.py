from django.shortcuts import render, redirect
from .models import Popular_Destination, Package, Image, Pack_Desc, Cab, Inclusions
# Create your views here.

def mail(request):
    subject = "Regarding Tour Booking"
    cat = {request.POST.get('select-category')}
    if cat == {None,} or cat == {"None",}:
        cat = ""
    else:
        cat = list(cat)[0]
    msg = f'''Greetings!
I want to know more about the packages that you are offering.
Name : {request.POST.get('name')}
Mobile : {request.POST.get('telphone')}
Email : {request.POST.get('email')}
Start Date : {request.POST.get('start-date')}
End Date : {request.POST.get('end-date')}
Package Category : {cat}
Query : {request.POST.get('message')}
'''
    return redirect(f"https://mail.google.com/mail/?view=cm&fs=1&to=himalayantribetravels@gmail.com&su={subject}&body={msg}")
    


def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('telphone')
        # cust = Customer(name = name, mobile = mobile, email = email)
        # cust.save()
        cat = {request.POST.get('select-category')}
        if cat == {None,} or cat == {"None",}:
            cat = ""
        else:
            cat = list(cat)[0]
        msg = f'''Name : {name}
Mobile : {mobile}
Email : {email}
Start Date : {request.POST.get('start-date')}
End Date : {request.POST.get('end-date')}
Package Category : {cat}
Query : {request.POST.get('message')}
'''
        himalayantribe = '7559700666'
        me = '7014334328'
        return redirect(f'https://wa.me/{himalayantribe}?text={msg}')
    
    
    
    context = {
        'cities':Popular_Destination.objects.all(),
        'top_packs':Package.objects.filter(top_package = True),
        'images':Image.objects.filter(to_be_shown = True)[:10],
        'cabs':Cab.objects.filter(popular = True)
    }
    return render(request,'website/index.html', context = context)





def packages(request):
    context = {
        'categories':Popular_Destination.objects.all(),
        'packages':Package.objects.all(),
    }
    return render(request, 'website/packages.html', context = context)



def pack(request, **kwargs):
    
    context = {
        'pack': Package.objects.filter(title = kwargs['pack']).first(),
        'similar' : Package.objects.filter(top_package = True)[:6]
    }
    context['descs'] = Pack_Desc.objects.filter(package = context['pack'])
    # cities = context['pack'].cities.all()
    # temp = Package.objects.filter(cities)
    # 'similars':Package.objects.filter(cat__title = 'Himachal package')

    return render(request, 'website/singlePackage.html', context = context)




def destination(request, **kwargs):

    
    pack_qs = Package.objects.filter(cities__title = kwargs['city'])
    d = {}
    for i in pack_qs:
        if i.category in d:
            d[i.category].append(i)
        else:
            d[i.category] = [i,]

    context = {
        'city': Popular_Destination.objects.filter(title = kwargs['city']).first(),
        'packages':d,
    }

    return render(request, 'website/popularDestination.html', context = context)


def cabs(request):
    context = {
        'cats' : {
            'sedan cabs':Cab.objects.filter(cat = "Sedan Cabs"),
            'muv cabs':Cab.objects.filter(cat = "MUV Cabs"),
            'suv cabs':Cab.objects.filter(cat = "SUV Cabs"),
            'minibus cabs':Cab.objects.filter(cat = "Minibus Cabs"),
            'rental vehicles':Cab.objects.filter(cat = "Rental Vehicles"),
            'bike rentals':Cab.objects.filter(cat = "rental Bikes"),
        },
        
    }
    return render(request, 'website/cabRental.html', context = context)


himalayantribe = '7559700666'
"https://wa.me/7014334328?text=heyy"

"himalayantribetravels@gmail.com"

"https://mail.google.com/mail/?view=cm&fs=1&to=someone@example.com&su=SUBJECT&body=BODY&bcc=someone.else@example.com"
"https://mail.google.com/mail/?view=cm&fs=1&tf=1&to=himalayantribetravels@gmail.com"
