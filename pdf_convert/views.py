from django.shortcuts import render
from astro.models import Astro_details
from django.http import HttpResponse
from django.template.loader import  get_template
from xhtml2pdf import pisa

# Create your views here.

def show_details(request):
    detail = Astro_details.objects.all()
    context = { 'details': detail  }
    return render(request, 'showinfo.html', context)
  
def pdf_report_create(request):
    detail = Astro_details.objects.all()

    template_path = 'pdf_report.html'
    context = {'details': detail}   
    response = HttpResponse(content_type='application/pdf')
   # response['Content-Disposition'] = 'attachment; filename="report.pdf"' //attachment option directly download without file open
    response['Content-Disposition'] = 'filename="report.pdf"'
  
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response