from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.core.mail import EmailMultiAlternatives, send_mail
from django.template.loader import render_to_string
from django.http import HttpResponse

def landing_page(request):
    context = RequestContext(request)
    return render_to_response('explosion/index.html', {}, context) 

def rules(request):
    context = RequestContext(request)
    return render_to_response('explosion/rules.html', {}, context) 

def contact_us(request):
    if request.method == 'POST':
        name = request.POST['name']
        email_address = request.POST['email_address']
        message = request.POST['message']
        send_explosion_email('timcallagy@gmail.com', 'Someone has contacted you through playpeekaboom.com', 'email', {'name': name, 'email_address': email_address, 'message': message }, True)
    return HttpResponse('Ok')

def subscribe(request):
    if request.method == 'POST':
        print(request)
        email_address = request.POST['subscriber_email']
        send_explosion_email('timcallagy@gmail.com', 'Someone has subscribed through playpeekaboom.com', 'email', {'email_address': email_address}, True)
    return HttpResponse('Ok')

################################
###
###  Functions
###
################################


# Handles email notification sending.
def send_explosion_email(to, subject, content_name, variables, email_notifications_requested):
    if to and email_notifications_requested == True:
        from_email = 'Peekaboom_website@boom.com'
        html_content = render_to_string('explosion/emails/' + content_name + '.html', variables)
        text_content = render_to_string('explosion/emails/' + content_name + '.txt', variables)
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")

        msg.mixed_subtype = 'related'
        msg.send()
    return

