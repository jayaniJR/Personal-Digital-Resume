from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
import tempfile
import datetime


def home(request):
    return render(request, 'base/home.html')


def cv_pdf(request):
    # response = HttpResponse(content_type='application/pdf;')
    # response['Content-Disposition'] = 'inline; attachment; filename=cv_pdf' + \
    #     str(datetime.datetime.now())+'.pdf'
    # response['Content-Transfer-Encoding'] = 'binary'
    #
    # html_string = render_to_string('base/cv_pdf.html')
    # html = HTML(string=html_string)
    # result = html.write_pdf()
    #
    # # with tempfile.NamedTemporaryFile(delete=True) as output:
    # #     output.write(result)
    # #     output.flush()
    # #
    # #     output = open(output.name, 'rb')
    # #     response.write(output.read())
    #
    # return result
    return render(request, 'base/cv_pdf.html')



