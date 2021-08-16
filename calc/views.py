from django.shortcuts import render
from django.http import HttpResponse
import qrcode
import qrcode.image.svg
from io import BytesIO
# Create your views here.

def genqrcode(request):
    context = {}
    if request.method == "POST":
        factory = qrcode.image.svg.SvgImage
        img = qrcode.make(request.POST.get("qr_text",""), image_factory=factory, box_size=40)
        stream = BytesIO()
        img.save(stream)
        context["svg"] = stream.getvalue().decode()

    return render(request, "home.html", context=context)
    #return render(request,'home.html',{'name':'saranya'})
def add(request):
    val_1 = int(request.POST['num1'])
    val_2 = int(request.POST['num2'])
    res = val_1 + val_2 

    return render(request, 'result.html',{"result" : res})

def result(request):
       
    return render(request,'result.html',{'name':'result'})