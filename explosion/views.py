from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response

def landing_page(request):
    context = RequestContext(request)
    return render_to_response('explosion/index.html', {}, context) 

def rules(request):
    context = RequestContext(request)
    return render_to_response('explosion/rules.html', {}, context) 
