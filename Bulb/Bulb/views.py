from django.shortcuts import render
def home(request):
    if request.method == 'POST':
        return render(request,"Bulb_on.html")
    else:
        return render(request,"Bulb_off.html")
    