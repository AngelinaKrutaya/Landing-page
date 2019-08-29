from django.shortcuts import render_to_response
from django.shortcuts import render
# Create your views here.
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.mail import send_mail, get_connection
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from .forms import Contact
from .models import Image,Certificate,Objects
from django import forms
from django.core import serializers
from django.core.serializers import serialize
from django.http import JsonResponse
import json
from django.db.models import Count
def index(request):
      if request.method == 'POST':
          return HttpResponseRedirect('/contact/')
      else:
          return render(request, 'thank.html',)



#def contact(request):
      #  errors=[]
    #    if request.method == "POST":
      #      if not request.POST.get('name', ' '):
       #           errors.append('Введите Имя.')
       #     if not request.POST.get('subname', ' '):
       #           errors.append('Введите Фамилию.')
       #     if not request.POST.get('email',''):
       #           errors.append('Введите Email.')
      #      if request.POST.get('email') and '@' not in request.POST['email']:
     #            errors.append('Введите правильный e-mail адрес.')
     #       if not request.POST.get('message',''):
     #             errors.append('Введите текст.')
     #       if not errors:
     #             send_mail(
     #                 str(request.POST.get('name', ' ')) + ' ' + str(request.POST.get('subname', ' ')),
     #                 str(request.POST.get('phone', ' ')) + '\n' + str(request.POST.get('message', ' ')),
     #                 [request.POST.get('email', ' ')],
      #                ['angelusey@gmail.com'],
      #                fail_silently=False
      #            )
      #            return HttpResponseRedirect('/thank/')
      #  image = Image.objects.all()
      #  object = Objects.objects.all()
      #  certificate= Certificate.objects.all()
      #  return render(request,'index.html',{"images":image,"objects":object, "certificates":certificate})
    #              'errors':errors,
    #              'Имя': request.POST.get('name',''),
    #              'Фамилия': request.POST.get('subname',''),
    #              'Телефон': request.POST.get('phone',''),
    #              'Email': request.POST.get('email',''),
    #              'Текст сообщения': request.POST.get('message',''),
    #        })

def contact(request):
    if request.method == 'POST':
        form = Contact(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            #if cd['name'] not in cd:
                #raise forms.ValidationError("You have forgotten enter name!")
            send_mail(
                    str(cd['name'])+' '+ str(cd['subname']),
                    str(cd['phone'])+ '\n' + str(cd['message']),
                    [cd.get('email', 'noreply@example.com')],
                    ['angelusey@gmail.com'],
                    fail_silently=False
                )
            return HttpResponseRedirect('/thank/')
    else:
        form = Contact()
    image = Image.objects.all()
    object = Objects.objects.all()
    certificate= Certificate.objects.all()
    return render(request,'index.html', {'form': form,"images":image,"objects":object, "certificates":certificate})

def image(request):
    image= Image.objects.all()
    return render(request,'image.html',{"images": list(image)})