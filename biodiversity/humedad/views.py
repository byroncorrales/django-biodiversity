#from models import *
#import datetime
#from diversity.forms import *
#from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
#from django.template import RequestContext
#from diversity.decorators import session_required
#from django.template.defaultfilters import slugify

#def list_parse(s):
#    for c in ['[', ']', 'u', "'",]:
#        s = s.replace(c,'')
#    return s.split(',')

#@session_required
#def _get_params(request):
#    '''Sacar de la variable de sesion y formar queryset''' 
#    params = {'fecha__year': request.session['fecha']}
#    if request.session['lugares']:
#        params['zona__in'] = request.session['lugares']
#    elif request.session['pais']:
#        params['pais'] = request.session['pais']

#    return params
#    
#    
#def index(request):
#    '''Vista incluye formulario de consulta'''
#    if request.method == 'POST':
#        form = DiversityForm(request.POST)
#        if form.is_valid():
#            print form.cleaned_data['lugar']
#            request.session['lugares'] = list_parse(form.cleaned_data['lugar'])
#            request.session['fecha'] = form.cleaned_data['fecha']
#            request.session['pais'] = form.cleaned_data['fecha']
#            request.session['activa'] = True
#            activa = True
#        else:
#            activa = False
#        dicc = {'form': form, 'activa': activa}
#        return render_to_response('humedad/index.html', dicc,
#                                  context_instance = RequestContext(request))
#    else:
#        form = DiversityForm()
#        return render_to_response('humedad/index.html', {'form': form},
#                                  context_instance = RequestContext(request))

#def grafohumedad(request):
#    a = _get_params(request)
#    
#    tabla = []
#    
#    for opcion in Humedad.objects.all():
#        for mes in range(1, 13):
#            #a = mes[1]   
#        #key = (opcion[1]).replace('-','_')
#        #query = a.filter(humedad__mes = opcion[0])
#            humedad = Humedad.objects.filter(mes = mes)
#            fila = {'mes':a, 'humedad':humedad}
#        tabla.append(fila)
#        print opcion
#    # print tabla    
#    return render_to_response('humedad/grafo_humedad.html',locals(),
#                             context_instance=RequestContext(request))
