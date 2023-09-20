from django.shortcuts import render
# Create your views here.

def homepage(request):
    return render(request , 'home.html')

    print('Dinesh')

def listpage(request):
    listdata = vehicle.objects.all()
    context = {
        'listdata': listdata,
    }
    request render(request,'list.html',context)