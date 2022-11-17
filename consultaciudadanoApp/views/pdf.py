from django.shortcuts import HttpResponse
from django.views import View
from consultaciudadanoApp.models import Ciudadanos

import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders

class generarPDF(View):
    def get(self, *args, **kwargs):
        
        template = get_template('ciudadanos.html')
        context = {
            'ciudadanos': Ciudadanos.objects.all(),
            
            }
        html = template.render(context)
        response = HttpResponse(content_type='application/pdf')
        #response['Content-Disposition'] = 'attachment; filename="reporte.pdf"'
        pisa_status = pisa.CreatePDF(html, dest=response)
        
        return response

