from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request, 'store/index1.html')

def vehicules(request):
    vehicules = Voiture.objects.all()
    return render(request, 'store/vehicules.html', {"vehicules":vehicules})

def a_propos(request):
    return render(request, 'store/about.html')


def service(request):
    return render(request, 'store/service.html')



def reserver(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        # country = request.POST.get('country')
        article = request.POST.get('article')
        quantite = request.POST.get('quantite')
        indicatif = request.POST.get('indicatif')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        

        html = render_to_string('store/file.html', {
            'name':name,
            'email':email,
            # 'country':country,
            'article': article,
            'quantite':quantite,
            'indicatif':indicatif,
            'phone':phone,
            'message':message,
            })
        

        # message = '''
        # From:\n\t\t{}\n
        # Email:\n\t\t{}\n
        # Subject:\n\t\t{}\n
        # Message:\n\t\t{}\n
        # '''.format(form_data['name'], form_data['email'],form_data['subject'] ,form_data['message'] )
        # send_mail('You got a mail!', message, '', [settings.EMAIL_HOST_USER]) 
        send_mail('Nouvelle commande', 'this is the message', email, ['garagestmaurice0000@gmail.com'], html_message=html)


        messages.success(request, "Votre message a été envoyé avec succes !!")
        # return render(request, 'app/contact.html')
        return redirect('index')

    return render(request, 'store/appoinment.html')



#  html = render_to_string('send/emails/contactform.html', {
#                 'name':name,
#                 'email': email,
#                 'content':content
#             })
#             send_mail(objet, 'this is the message', email, ['devs.dudes@gmail.com'], html_message=html)
#             return redirect ('index')






def voiture(request, slug):
    voiture = get_object_or_404(Voiture, slug=slug)
    if request.method == 'POST':
        car = voiture.marque
        print(car)
        return render(request, 'store/appoinment.html', {'car':car})
    return render(request, 'store/department-single.html', {'voiture':voiture} )


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        # country = request.POST.get('country')
        subject = request.POST.get('subject')
        
        
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        

        html = render_to_string('store/file2.html', {
            'name':name,
            'email':email,
            'subject': subject,
            'phone':phone,
            'message':message,
            })
        

        # message = '''
        # From:\n\t\t{}\n
        # Email:\n\t\t{}\n
        # Subject:\n\t\t{}\n
        # Message:\n\t\t{}\n
        # '''.format(form_data['name'], form_data['email'],form_data['subject'] ,form_data['message'] )
        # send_mail('You got a mail!', message, '', [settings.EMAIL_HOST_USER]) 
        send_mail('Nouveau message', 'this is the message', email, ['garagestmaurice0000@gmail.com'], html_message=html)


        messages.success(request, "Votre message a été envoyé avec succes !!")
    return render(request, 'store/contact.html')
    