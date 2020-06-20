from django.contrib import auth
from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .models import Test23
from .models import Conference
from .models import Conference_material
from django.http import HttpResponse
from django.shortcuts import render, redirect, render_to_response
from django.template import Context, loader
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import ContactForm
from .forms import ContactFormForm
from .forms import ConferenceForm
from .forms import Conference_materialForm
from .forms import Conference_materialForm2
from .models import Position
from .forms import PositionForm
from .models import Organization
from .forms import OrganizationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db import connection
from .forms import NameForm
from .forms import NameForm2
from .forms import NameForm3
from .forms import Prof_user
from .forms import New_pass
from .forms import New_pass2
from .forms import Pass
from django.contrib.auth.models import AbstractUser
import subprocess
import time
import time
import shlex
import os
from subprocess import call
from pytils import translit
from .forms import CommentForm
from .models import Comment
from .models import Section
from .forms import SectionForm
from .models import Section
from django.contrib import messages
from .models import User_conference
from django.contrib.auth import views
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.core.files.storage import default_storage
import re
from .forms import Foto_userForm
from .models import Foto_user
from .models import Branch_science
from .models import Years


#PostgreSQL была заменена на SQLLITE3 

# def post_list(request):
    # posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    # return render(request, 'new/post_list.html', {'posts': posts})

#Список конференций
def post_list(request):
    conferences = Conference.objects.all().order_by('-id');
    nauks = Branch_science.objects.all().order_by('-id')
    orgs = Organization.objects.all().order_by('-id')
    years = Years.objects.all().order_by('-id')
    # confs = Conference.objects.all().order_by('-id')
    # return render(request, 'new/conferents_list.html', {'nauks': nauks, 'orgs': orgs, 'years': years, 'confs': confs})
    return render(request, 'new/conferents_list.html', {'conferences': conferences})
	
	
def post_detail(request, pk):
        post = get_object_or_404(Post, pk=pk)
        return render(request, 'new/post_detail.html', {'post': post})	
		
def test_list(request):
    testr = Test23.objects.all(); 
    return render(request, 'new/test_list.html', {'testr': testr})
   #post2 = Test23.objects.filter(user_id=1)
    #return render(request, 'new/test_list.html', {'post2': post2})	


#def contact(request):
   # if request.POST:
       # form = ContactForm(request.POST)
        # Если форма прошла валидацию
       # if form.is_valid():
          #  cd = form.cleaned_data
            # ... сохранение в базу, к примеру
            # здесь мы просто выведем результат на экран
           # return HttpResponse(
              #  'Name: %s, Email: %s, Message: %s' %
               # (cd['name'], cd['email'], cd['message']))
   # else:
        #form = ContactForm()
    #return render(request, 'new/contact.html', {'form': form})

#Список конференций
def conferents_list(request):
    conferences = Conference.objects.all().order_by('-id');
    nauks = Branch_science.objects.all().order_by('-id')
    orgs = Organization.objects.all().order_by('-id')
    years = Years.objects.all().order_by('-id')
    # confs = Conference.objects.all().order_by('-id')
    # return render(request, 'new/conferents_list.html', {'nauks': nauks, 'orgs': orgs, 'years': years, 'confs': confs})
    return render(request, 'new/conferents_list.html', {'conferences': conferences})


def post_detail_confer(request, pk):
    conference = get_object_or_404(Conference, pk=pk)
   # if User_conference.objects.filter(user = request.user.pk, conference = pk).exists():
       # messages.error(request, 'участник комнат')
        #dd='1'
    return render(request, 'new/post_detail_confer2.html', {'conference': conference})
   # else:
      #  return render(request, 'new/post_detail_confer.html', {'conference': conference})



#def post_detail_confer2(request, conference_id):
    #confs = get_object_or_404(Conference_material, pk=conference_id)

    #return render(request, 'new/post_detail_confer.html', {'confs': confs})

#def contact_new(request):
    #form = ContactForm()
   # return render(request, 'new/contact_new.html', {'form': form})


#def contact_new(request):
    #if request.method == "POST":
      #  form = ContactForm(request.POST)
       # if form.is_valid():
         #   post = form.save(commit=False)
           # post.published_contact = timezone.now()
         #   post.save()
          #  return HttpResponse('Спасибо за ваше сообщение!')
   # else:
       # form = ContactForm()
   # return render(request, 'new/contact_new.html', {'form': form})

#Список всех заявок для создания комнаты
def contacts_list(request):
    contacts = ContactForm.objects.all()
    return render(request, 'new/contacts_list.html', {'contacts': contacts})

#Страница подробнее для определенной заявки на создание комнаты
def contact_ditails(request, pk):
    contact = get_object_or_404(ContactForm, pk=pk)
    return render(request, 'new/contact_ditails.html', {'contact': contact})


# Механизм комментирования отказа в публикации материала (идеи и предложения)
def conttwstper(request, id):
    ss = id
    if request.method == "POST":
        form = NameForm2(request.POST)
        if form.is_valid():
           dd2 = form.cleaned_data['your_name']
           cursor2 = connection.cursor()
           cursor2.execute("UPDATE new_contactform SET message_com = %s WHERE id=%s", [dd2, ss])
        contacts = ContactForm.objects.all()
        return render(request, 'new/contacts_list.html', {'contacts': contacts})
    else:
       cursor = connection.cursor()
       cursor.execute("UPDATE new_contactform SET status_id='3' WHERE id=%s", [ss])
       form = NameForm2()
       # return render(request, 'new/conttwstper.html', {'form': form})
       return render(request, 'new/conttwstper.html', {'form': form})


#Страница подачи заявки от пользователя к админу (заявки на создание комнаты)
@login_required
def contact_new(request):
    if request.method == "POST":
        form = ContactFormForm(request.POST)
        if form.is_valid():
            dd2 = form.cleaned_data['nameconfer']
            #dd1 = form.cleaned_data['login_user']
            dd3 = form.cleaned_data['org']
            dd4 = form.cleaned_data['branch_science']
            dd5 = form.cleaned_data['date_launch_s']
            dd6 = form.cleaned_data['date_launch_po']
            dd7 = form.cleaned_data['srok_podacha']
            dd8 = form.cleaned_data['srok_prin_resh_itog']
            dd9 = form.cleaned_data['message']
            dd10 = form.cleaned_data['trebovania']
            dd11 = form.cleaned_data['sostav_orgkomitet']
            # dd12 = form.cleaned_data['published_contact']
        if Conference.objects.filter(titleconf=dd2).exists():
            messages.error(request, 'Конференция с такой темой уже опубликована! Введите другую тему комнат.')
            form = ContactFormForm(
                initial={'status': 1, 'login_user': request.user, 'org': dd3, 'branch_science': dd4, 'date_launch_s': dd5,
                         'date_launch_po': dd6, 'srok_podacha': dd7, 'srok_prin_resh_itog': dd8, 'message': dd9,
                         'trebovania': dd10,
                         'sostav_orgkomitet': dd11, 'published_contact':timezone.now()})
            return render(request, 'new/contact_new.html', {'form': form})
        else:

            post = form.save(commit=False)
            post.login_user = request.user
            post.published_contact = timezone.now()
            post.save()
        return render(request, 'new/spasibo.html', {'post': post})
    else:
        # items = get_object_or_404(auth, id=user_id)
        form = ContactFormForm(initial={'status': 1, 'message':'', 'published_contact':timezone.now()})
        return render(request, 'new/contact_new.html', {'form': form})

# def conference_new(request, contact_nameconfer):
#     if request.method == "POST":
#         form = ConferenceForm(request.POST)
#         if form.is_valid():
#            form.published_dateconf = timezone.now();
#            form.titleconf = contact_nameconfer;
#            #form.authorconf = ContactForm.login;
#            #form.titleconf = ContactForm.nameconfer;
#            form.save()
#         return render(request, 'new/conference_new.html', {'form': form})
#     else:
#         item = get_object_or_404(Conference, id=1)
#         form = ConferenceForm(instance=item)
#       #  form.titleconf = contact_nameconfer;
#         form.published_dateconf = timezone.now();
#     return render(request, 'new/conference_new.html', {'form': form})

#Форма для добавления комнаты со страницы с заявкой
def conference_new2(request,id):
     # items = Conference.objects.all();
     if request.method == "POST":
         form = ConferenceForm(request.POST)

         if form.is_valid():
             dd2 = form.cleaned_data['titleconf']
             dd1 = form.cleaned_data['authorconf']
             dd3 = form.cleaned_data['org']
             dd4 = form.cleaned_data['branch_science']

             dd5 = form.cleaned_data['date_launch_s']
             dd6 = form.cleaned_data['date_launch_po']

             dd7 = form.cleaned_data['srok_podacha']
             dd8 = form.cleaned_data['srok_prin_resh_itog']
             dd9 = form.cleaned_data['textconf']
             dd10 = form.cleaned_data['trebovania']
             dd11 = form.cleaned_data['sostav_orgkomitet']


             if Conference.objects.filter(titleconf=dd2).exists():
                 messages.error(request, 'Конференция с такой темой уже опубликована! Введите другую тему комнат или вернитесь в заявку и отклоните публикацию.')
                 form = ConferenceForm(initial={ 'published_dateconf': timezone.now(),
                                                'authorconf': dd1, 'branch_science': dd4,
                                                'date_launch_s': dd5,
                                                'date_launch_po': dd6,
                                                'srok_podacha': dd7,
                                                'srok_prin_resh_itog': dd8,
                                                'trebovania': dd10,
                                                'sostav_orgkomitet': dd11,
                                                'org': dd3, 'textconf':dd9, 'titleconf':dd2, 'otmenpublic':True})
                 # return render(request, 'new/conference_new2.html', {'items': items})
                 return render(request, 'new/conference_new2.html', {'form': form})
             else:
                 # PostgreSQL Запрос на обновление статуса в таблице заявок на создание комнат
                 ss = id
                 cursor = connection.cursor()
                 cursor.execute("UPDATE new_contactform SET status_id='2' WHERE id=%s", [ss])

                 # PostgreSQL Запрос на обновление статуса в таблице заявок на создание комнат END

                 form.published_dateconf = timezone.now();
                 form.titleconf = id;
                 form.save()

                 cursor2 = connection.cursor()
                 cursor2.execute("select max(id) from new_conference;")
                 row2 = cursor2.fetchone()
                 cursor3 = connection.cursor()
                 cursor3.execute("select titleconf from new_conference where id=%s;", [row2])
                 row = cursor3.fetchone()

                 cursor30 = connection.cursor()
                 cursor30.execute("select authorconf_id from new_conference where id=%s;", [row2])
                 us = cursor30.fetchone()

                 cursor4 = connection.cursor()
                 cursor4.execute("INSERT INTO new_section (section_name, comentsection, confer_id) VALUES(%s, '', %s)", [row, row2])
                 fg = timezone.now();
                 cursor20 = connection.cursor()
                 cursor20.execute(
                     "INSERT INTO new_user_conference (message, published_us_confr, conference_id, status_role_id, status_user_id, user_id) values(' ', %s, %s, 1, 2, %s)",
                     [fg, row2, us])
         return render(request, 'new/conferdobavlen.html', {'form': form})
     else:
         #взять из таблицы/модели contactform nameconfer  по id
        zinfo= get_object_or_404(ContactForm, id=id)
        form = ConferenceForm(initial={'titleconf': zinfo.nameconfer, 'published_dateconf': timezone.now(), 'authorconf':zinfo.login_user, 'branch_science':zinfo.branch_science,
                                       'date_launch_s': zinfo.date_launch_s, 'date_launch_po': zinfo.date_launch_po, 'srok_podacha': zinfo.srok_podacha,
                                       'srok_prin_resh_itog': zinfo.srok_prin_resh_itog, 'trebovania': zinfo.trebovania, 'sostav_orgkomitet': zinfo.sostav_orgkomitet,
                                       'org': zinfo.org, 'otmenpublic':True, 'textconf':zinfo.message})

        return render(request, 'new/conference_new2.html', {'form': form})


#Форма для добавления материала (идеи и предложения)
def material_new(request, id):
    # items = Conference.objects.all();
    if request.method == "POST":
        form = Conference_materialForm(id, request.POST, request.FILES)
        if form.is_valid():

            form.published_datematerial = timezone.now()

            dd2 = form.cleaned_data['file_obj'].name
           #dd7 = form.cleaned_data['file_obj']._require_file()
            dd11 = form.cleaned_data['titlematirial']
            dd777 = form.cleaned_data['titlematirial']
           #dd77 = re.sub(r"[#%!@*'/`~<>=+:;,$&?.]", "", dd777)
            dd12 = form.cleaned_data['conference']
            dd22 = form.cleaned_data['authormatirial2']
            dd29 = form.cleaned_data['authormatirial']
            org = form.cleaned_data['org']

            ddslo2 = form.cleaned_data['annotation_rus']
            ddslo3 = form.cleaned_data['annotation_usa']
            ddslo4 = form.cleaned_data['keywords_rus']
            ddslo5 = form.cleaned_data['keywords_usa']

            if Conference_material.objects.filter(titlematirial=dd11, conference=dd12).exists():
                messages.error(request, 'Материал с таким заголовком уже существует в данной комнат (измените заголовок и загрузите файл).')
                matfo = get_object_or_404(Conference, id=id)
                form = Conference_materialForm(id, initial={'conference': matfo.id,
                                                            'published_datematerial': timezone.now(),
                                                            'authormatirial': request.user,
                                                            'branch_science': matfo.branch_science, 'status': 4, 'authormatirial2':dd22, 'org':org, 'otmenpublic':True,
                                                            'annotation_rus':ddslo2,'annotation_usa':ddslo3, 'keywords_rus': ddslo4, 'keywords_usa':ddslo5 })

                return render(request, 'new/material_new.html', {'form': form})
            else:
                if '.pdf' in dd2:

                    if User_conference.objects.filter(user=request.user.pk, conference=id).exists():
                        post = form.save(commit=False)
                        post.save()
                    else:
                         post = form.save(commit=False)
                         post.save()
                         dd4 = request.user.pk
                         dd3 = timezone.now()
                         cursor7 = connection.cursor()
                         cursor7.execute("INSERT INTO new_user_conference (message, published_us_confr, conference_id, status_role_id, status_user_id, user_id) values('текст', %s, %s, 3, 2, %s)",[dd3, id, dd4])
                else:
                    if User_conference.objects.filter(user=request.user.pk, conference=dd12).exists():
                        post = form.save(commit=False)
                        post.save()
                    else:
                        post = form.save(commit=False)
                        post.save()
                        dd3 = timezone.now()
                        dd4 = request.user.pk
                        cursor9 = connection.cursor()
                        cursor9.execute("INSERT INTO new_user_conference (message, published_us_confr, conference_id, status_role_id, status_user_id, user_id) values('', %s, %s, 3, 2, %s)",[dd3, id, dd4])

                    time.sleep(3)
# -----------------------------Конвертор для удаленного ПК-----------------------------------------------
                   # os.system(
                     #'call "C:/Program Files (x86)/OpenOffice 4/program/python.exe" C:/unoconvr/unoconv --format pdf --output C:/Users/tatyana/AppData/Local/Programs/Python/Python35/Scripts/mysite/media/media/conf/conf_{0}/{1}.pdf C:/Users/tatyana/AppData/Local/Programs/Python/Python35/Scripts/mysite/media/media/conf/conf_{0}/{1}.docx'.format(
                       # id, translit.slugify(dd11)))

#-----------------------------Конвертор для моего ПК-----------------------------------------------------
                    os.system(
                     'call "C:/Program Files (x86)/LibreOffice 5/program/python.exe" C:/unoconvr/unoconv --format pdf --output C:/djangoconf/media/media/conf/conf_{0}/{1}.pdf C:/djangoconf/media/media/conf/conf_{0}/{1}.docx'.format(
                       id, translit.slugify(dd11)))

#--------------------------------------------------------------------------------------------------------
                   # os.system(
                    # 'call "C:/Program Files (x86)/OpenOffice 4/program/python.exe" C:/unoconvr/unoconv --format pdf --output C:/Users/tatyana/AppData/Local/Programs/Python/Python35/Scripts/mysite/media/media/conf/conf_{0}/{1}.pdf C:/Users/tatyana/AppData/Local/Programs/Python/Python35/Scripts/mysite/media/media/conf/conf_{0}/{1}.docx'.format(
                     # id, dd2))
            return redirect('new.views.opisanie_material', pk=post.pk)
                #return render(request, 'new/materialdob.html', {'form': form})
    else:
        # взять из таблицы/модели contactform nameconfer  по id
        matfo = get_object_or_404(Conference, id=id)

        if request.user.patronymic == None:
            im = request.user.last_name + ' ' + request.user.first_name
        else:
            im= request.user.last_name + ' ' + request.user.first_name + ' ' + request.user.patronymic

        #matfo2 = get_object_or_404(Section, confer_id = id)
        #dd = Section.objects.order_by('child ren__date')
        # items = get_object_or_404(Conference, id=id)
        # form = ConferenceForm(instance=items)
        #form.fields["section"].queryset =Section.objects.filter(confer=id)
        form = Conference_materialForm(id, initial={'conference': matfo.id, 'published_datematerial': timezone.now(),
                                       'authormatirial': request.user, 'branch_science': matfo.branch_science, 'status':4, 'authormatirial2':im, 'org':request.user.organization, 'otmenpublic':True})

        # return render(request, 'new/conference_new2.html', {'items': items})
        return render(request, 'new/material_new.html', {'form': form})
#Страница подробнее для материала (идеи и предложения) комнаты
def opisanie_material(request, pk):
    op = get_object_or_404(Conference_material, pk=pk)
    return render(request, 'new/opisanie_material.html', {'op': op})

#-----------------------------------Механизмы для обновления справочников (это для дальнейшей системы поиска по отделам, году, секции или предпочтений пользователя)-------------------------
def position_dob(request):
    if request.method == "POST":
        form = PositionForm(request.POST)
        if form.is_valid():
            dd11 = form.cleaned_data['full_name']
            if Position.objects.filter(full_name=dd11).exists():
                messages.error(request, 'Такая должность уже есть в справочнике.')
                form = PositionForm()
                return render(request, 'new/position_dob.html', {'form': form})
            else:
                post = form.save(commit=False)
                post.save()
        posits = Position.objects.all();
        return render(request, 'new/positionspisok.html', {'posits': posits})
    else:
        #items = get_object_or_404(auth, id=user_id)
        form = PositionForm()
        return render(request, 'new/position_dob.html', {'form': form})

def reference(request):
    testr = Test23.objects.all();
    return render(request, 'new/reference.html', {'testr': testr})


def organization_dob(request):
    if request.method == "POST":
        form = OrganizationForm(request.POST)
        if form.is_valid():
           dd11 = form.cleaned_data['full_name']
           if Organization.objects.filter(full_name=dd11).exists():
               messages.error(request, 'Такая организация уже есть в справочнике.')
               form = OrganizationForm()
               return render(request, 'new/organization_dob.html', {'form': form})
           else:
               post = form.save(commit=False)
               post.save()
        orgs = Organization.objects.all();
        return render(request, 'new/vseorganization.html', {'orgs': orgs})
    else:
        #items = get_object_or_404(auth, id=user_id)
        form = OrganizationForm()
        return render(request, 'new/organization_dob.html', {'form': form})



def vseorganization(request):
    orgs = Organization.objects.all();
    return render(request, 'new/vseorganization.html', {'orgs': orgs})

def positionspisok(request):
    posits = Position.objects.all();
    return render(request, 'new/positionspisok.html', {'posits': posits})

# def positionspisok(request):
#     posits = Position.objects.all();
#     return render(request, 'new/positionspisok.html', {'posits': posits})

#-----------------------------------Механизмы для обновления справочников  (это для дальнейшей системы поиска по отделам, году, секции или предпочтений пользователя)-------------------------

#Список пользователей
def user_list(request):
    user4 = User.objects.all();
    return render(request, 'new/user_list.html', {'user4': user4})


def detail_user(request, pk):
    user4 = get_object_or_404(User, pk=pk)
    return render(request, 'new/detail_user.html', {'user4': user4})

#Форма для редактирования идеи и предложения-------------------------------
def edit_material(request, id):
    post = get_object_or_404(Conference_material, pk=id)
    # items = Conference.objects.all();
   # form = Conference_materialForm(id, request.POST, request.FILES)
    if request.method == "POST":
        matfo = get_object_or_404(Conference_material, id=id)
        #default_storage.delete(matfo.file_obj.name)
        dd26 = matfo.file_obj.name
        if '.pdf' in dd26:
             default_storage.delete(matfo.file_obj.name)
        else:
             if '.docx' in dd26:
                  dd3 = dd26[:-4]
                  dd4 = dd3 + 'pdf'
                  default_storage.delete(dd4)
                  default_storage.delete(matfo.file_obj.name)
             else:
                 dd3 = dd26[:-3]
                 dd4 = dd3 + 'pdf'
                 default_storage.delete(dd4)
                 default_storage.delete(matfo.file_obj.name)
        form = Conference_materialForm2(request.POST, request.FILES, instance=post)
        if form.is_valid():
            dd2 = form.cleaned_data['file_obj'].name
            dd11 = form.cleaned_data['titlematirial']
            dd12 = form.cleaned_data['conference']
            dd27 = matfo.conference.id
            dd26 = matfo.file_obj.name
            if '.pdf' in dd2:
                post = form.save(commit=False)
                post.save()
            else:
               # dd5 = 'C:\\dev\\python\\djangoconf\\media\\media\\conf\\conf_{0}\\{1}'.format(id, dd2)
               # dd7 = 'C:\\dev\\python\\djangoconf\\media\\media\\conf\\conf_{0}\\{1}.pdf'.format(id, dd2)
                # dd6 = 'unoconv --format pdf -o "C:\\dev\\python\\djangoconf\\media\\media\\conf\\conf_{0}\\" "C:\\dev\\python\\djangoconf\\media\\media\\conf\\conf_{0}\\{1}"'.format(id,dd2)
               # dd6 = 'call C:/Program Files (x86)/LibreOffice 5/program/python.exe C:/unoconvr/unoconv --format pdf --output C:/dev/python/djangoconf/media/media/conf/conf_{0}/{1}.pdf C:/dev/python/djangoconf/media/media/conf/conf_{0}/{1}'.format(
                   # id, dd2)
                # dd6 = 'unoconv --format pdf --output C:/dev/python/djangoconf/media/media/conf/conf_{0}/{1}.pdf C:/dev/python/djangoconf/media/media/conf/conf_{0}//{1}'.format(id,dd2)
                # dd7 = 'unoconv --format pdf --output C:/dev/python/djangoconf/media/media/conf/conf_{0}/{1}.pdf C:/dev/python/djangoconf/media/media/conf/conf_{0}/{1}'.format(id,dd2)

                post = form.save(commit=False)
                #post.tit
                post.save()
                time.sleep(3)
               # os.system(
                   # 'call "C:/Program Files (x86)/OpenOffice 4/program/python.exe" C:/unoconvr/unoconv --format pdf --output C:/Users/tatyana/AppData/Local/Programs/Python/Python35/Scripts/mysite/media/media/conf/conf_{0}/{1}.pdf C:/Users/tatyana/AppData/Local/Programs/Python/Python35/Scripts/mysite/media/media/conf/conf_{0}/{1}.docx'.format(
                      # dd27, translit.slugify(dd11)))
                os.system(
                   'call "C:/Program Files (x86)/LibreOffice 5/program/python.exe" C:/unoconvr/unoconv --format pdf --output C:/djangoconf/media/media/conf/conf_{0}/{1}.pdf C:/djangoconf/media/media/conf/conf_{0}/{1}.docx'.format(
                       dd27, translit.slugify(dd11)))
            ##form.published_datematerial = timezone.now();
            #form.save()
          #  post = form.save(commit=False)
           # post.save()
        return redirect('new.views.opisanie_material', pk=post.pk)
        #return render(request, 'new/post_list.html', {'form': form})
    else:
        # взять из таблицы/модели contactform nameconfer  по id
        matfo = get_object_or_404(Conference_material, id=id)

        form = Conference_materialForm2(initial={'conference': matfo.conference, 'published_datematerial': timezone.now(),
                                                    'authormatirial': request.user, 'titlematirial':matfo.titlematirial,
                                                    'branch_science': matfo.branch_science, 'status': 4,
                                                    'authormatirial2': matfo.authormatirial2, 'org': matfo.org, 'section':matfo.section, 'otmenpublic':True,
                                                 'annotation_rus': matfo.annotation_rus, 'annotation_usa': matfo.annotation_usa,
                                                 'keywords_rus': matfo.keywords_rus, 'keywords_usa': matfo.keywords_usa})
        # return render(request, 'new/conference_new2.html', {'items': items})

        #default_storage.delete(matfo.file_obj.name)
        return render(request, 'new/edit_material.html', {'form': form})
#------------------------------------------------------------------
#Форма для редактирования комнаты
def edit_conferences(request, id):
    post = get_object_or_404(Conference, pk=id)
    if request.method == "POST":
        form = ConferenceForm(request.POST, instance=post)
        if form.is_valid():
            dd2 = form.cleaned_data['titleconf']
            dd3 = id
            dd7 = form.cleaned_data['otmenpublic']

            if Conference.objects.filter(titleconf=dd2).exclude(id=dd3).exists():
                messages.error(request, 'Такая тема комнат уже опубликована! Введите другую тему.')
                zinfo = get_object_or_404(Conference, id=id)
                form = ConferenceForm(initial={'published_dateconf': zinfo.published_dateconf,
                                               'authorconf': zinfo.authorconf, 'branch_science': zinfo.branch_science,
                                               'date_launch_s': zinfo.date_launch_s,
                                               'date_launch_po': zinfo.date_launch_po,
                                               'srok_podacha': zinfo.srok_podacha,
                                               'srok_prin_resh_itog': zinfo.srok_prin_resh_itog,
                                               'trebovania': zinfo.trebovania,
                                               'sostav_orgkomitet': zinfo.sostav_orgkomitet,
                                               'org': zinfo.org, 'textconf': zinfo.textconf, 'otmenpublic':dd7})
                return render(request, 'new/edit_conferences.html', {'form': form})
            else:
                #messages.error(request, dd2 + dd3)
                post = get_object_or_404(Conference, pk=id)
                ff = post.titleconf
                cursor2 = connection.cursor()
                cursor2.execute("select min(id) from new_section where confer_id=%s and section_name=%s;", [dd3, ff])
                row = cursor2.fetchone()
                row2 = min(row)
                # cursor3 = connection.cursor()
                # cursor3.execute("select id from new_section where section_name=%s;", [dd2])
                # row = cursor3.fetchone()
                # row2 = min(row)
                if row2 is None:
                    form.published_dateconf = timezone.now()
                    form.save()
                else:
                    cursor = connection.cursor()
                    cursor.execute("UPDATE new_section SET section_name=%s WHERE id=%s", [dd2, row2])
                    form.published_dateconf = timezone.now()
                    form.save()
            return render(request, 'new/post_list.html', {'form': form})
    else:
        # взять из таблицы/модели contactform nameconfer  по id
        zinfo = get_object_or_404(Conference, id=id)
        form = ConferenceForm(initial={'titleconf': zinfo.titleconf, 'published_dateconf':zinfo.published_dateconf,
                                       'authorconf': zinfo.authorconf, 'branch_science': zinfo.branch_science,
                                       'date_launch_s': zinfo.date_launch_s, 'date_launch_po': zinfo.date_launch_po,
                                       'srok_podacha': zinfo.srok_podacha,
                                       'srok_prin_resh_itog': zinfo.srok_prin_resh_itog, 'trebovania': zinfo.trebovania,
                                       'sostav_orgkomitet': zinfo.sostav_orgkomitet,
                                       'org': zinfo.org, 'textconf':zinfo.textconf, 'otmenpublic':zinfo.otmenpublic})
        # return render(request, 'new/conference_new2.html', {'items': items})
        return render(request, 'new/edit_conferences.html', {'form': form})

#Список моих комнат
def my_conferents(request, pk):
    conferences = Conference.objects.filter(authorconf = pk);
    return render(request, 'new/my_conferents.html', {'conferences': conferences})

#Список моих идей и предложений
def my_material(request, pk):
    materials = Conference_material.objects.filter(authormatirial = pk);
    return render(request, 'new/my_material.html', {'materials': materials})

#Список моих заявок на создание\публикацию идеи и предложения
def my_contact(request, pk):
    contacts = ContactForm.objects.filter(login_user = pk);
    return render(request, 'new/my_contact.html', {'contacts': contacts})

def edit_material_my_conferents(request, pk):
    conference = get_object_or_404(Conference, pk=pk)

    return render(request, 'new/edit_material_my_conferents.html', {'conference': conference})

#Страница подробнее для идеи и предложения из списка (зале для разделения тем по секциям)
def ditailsmaterial(request, pk):
    if request.method == "POST":
      # PostgreSQL Запрос на обновление статуса в таблице материалов для комнат
        ss = pk
        cursor = connection.cursor()
        cursor.execute("UPDATE new_conference_material SET status_id='4' WHERE id=%s", [ss])
      # PostgreSQL Запрос на обновление статуса в таблице материалов для комнат END

        return render(request, 'new/mes_stat_material.html')
    else:
        material = get_object_or_404(Conference_material, pk=pk)
        return render(request, 'new/ditailsmaterial.html', {'material': material})
#Механизм комментирования отказа в публикации идей и предложений
def Twstper(request, id):
    ss = id
    if request.method == "POST":
       form = NameForm(request.POST)
       if form.is_valid():
          dd2 = form.cleaned_data['your_name']
          cursor2 = connection.cursor()
          cursor2.execute("UPDATE new_conference_material SET message_com = %s WHERE id=%s", [dd2, ss])
       return render(request, 'new/comgoto.html')
    else:

       cursor = connection.cursor()
       cursor.execute("UPDATE new_conference_material SET status_id='3' WHERE id=%s", [ss])
       form = NameForm()
       #return render(request, 'new/Twstper.html', {'form': form})
       return render(request, 'new/Twstper.html', {'form': form})

#Форма для редактирования профиля пользователя
def user_profile(request, pk):
    post = get_object_or_404(User, pk=pk)
    if request.method == "POST":
        form = Prof_user(request.POST, instance=post)
        if form.is_valid():
           form.save()
           return render(request, 'new/goodeditus.html', {'form': form})
        else:
            zinfo = get_object_or_404(User, pk=pk)
            return render(request, 'new/user_profile.html', {'form': form})
    else:
        # взять из таблицы/модели contactform nameconfer  по id
        zinfo = get_object_or_404(User, pk=pk)
        form = Prof_user(initial={'first_name': zinfo.first_name, 'last_name':zinfo.last_name,
                                       'patronymic': zinfo.patronymic, #'data_birth': zinfo.data_birth,
                                       'phone': zinfo.phone, #'address': zinfo.address,
                                       #'pol': zinfo.pol,
                                       #'academemic_degree': zinfo.academemic_degree, 'position': zinfo.position,
                                       #'uchenoe_zvanie': zinfo.uchenoe_zvanie,
                                       #'organization': zinfo.organization, 'country':zinfo.country, #'rinc_author':zinfo.rinc_author,
                                       'security_question':zinfo.security_question, 'check_answer':zinfo.check_answer, #'description':zinfo.description,
                                  # 'username': zinfo.username,
                                  # 'email': zinfo.email, 'password': zinfo.password
                                  })
        # return render(request, 'new/conference_new2.html', {'items': items})
        return render(request, 'new/user_profile.html', {'form': form})

# def file_upload(request):
#   if request.method == 'POST':
#     form = File_doc_rtfForm(request.POST, request.FILES)
#     if form.is_valid():
#
#       form.save()
#       return HttpResponseRedirect('/')
#   else:
#     form = File_doc_rtfForm()
#
#   return render(request, 'new/file_upload.html', {'form': form})

def deletcont(request, pk):
    # PostgreSQL Запрос на обновление статуса в таблице материалов для комнат
    ss = pk
    cursor = connection.cursor()
    cursor.execute("DELETE FROM new_contactform WHERE id =%s;", [ss])
    # PostgreSQL Запрос на обновление статуса в таблице материалов для комнат END
    return render(request, 'new/deletgood.html')

#Страница со списком конференций
def full_list_confer(request):
    conferences = Conference.objects.all()
    return render(request, 'new/full_list_confer.html', {'conferences': conferences})

def spisok_material_conferents(request, pk):
    conference = get_object_or_404(Conference, pk=pk)

    return render(request, 'new/spisok_material_conferents.html', {'conference': conference})
#Удаление идеи и предложения
def udalenie_material(request, pk):

    ss = pk
    matfo = get_object_or_404(Conference_material, id=ss)
   # dd2 = form.cleaned_data['file_obj'].name
    dd2=matfo.file_obj.name
    if '.pdf' in dd2:
       default_storage.delete(matfo.file_obj.name)
    else:
        if '.docx' in dd2:
             dd3=dd2[:-4]
             dd4=dd3+'pdf'
             default_storage.delete(dd4)
             default_storage.delete(matfo.file_obj.name)
        else:
            dd3 = dd2[:-3]
            dd4 = dd3 + 'pdf'
            default_storage.delete(dd4)
            default_storage.delete(matfo.file_obj.name)

    cursor2 = connection.cursor()
    cursor2.execute("DELETE FROM new_comment WHERE post_id =%s;", [ss])

    cursor = connection.cursor()
    cursor.execute("DELETE FROM new_conference_material WHERE id =%s;", [ss])
    dd = matfo.conference.pk
    messages.error(request, 'Материал успешно удален')
    #return render(request, 'new/uspex_udalenie.html')
    return redirect('new.views.spisok_material_conferents', pk=dd)

#Временный механизм удаление идеи и предложения для выбранной комнаты, секции
def sterta(request, pk):
    # PostgreSQL Запрос на обновление статуса в таблице материалов для комнат
    ss = pk

    cursor2 = connection.cursor()
    cursor2.execute("DELETE FROM new_conference_material WHERE conference_id = %s;", [ss])

    cursor = connection.cursor()
    cursor.execute("DELETE FROM new_user_conference WHERE conference_id = %s;", [ss])

    cursor5 = connection.cursor()
    cursor5.execute("DELETE FROM new_comment WHERE conference_id = %s;", [ss])

    cursor3 = connection.cursor()
    cursor3.execute("DELETE FROM new_section WHERE confer_id = %s;", [ss])

    cursor4 = connection.cursor()
    cursor4.execute("DELETE FROM new_conference WHERE id = %s;", [ss])

    # PostgreSQL Запрос на обновление статуса в таблице материалов для комнат END
    return render(request, 'new/confmaterial_stert.html')

#Форма добавления комментария
def add_comment_to_post(request, pk):
    op = get_object_or_404(Conference_material, pk=pk)
    conf=op.conference.pk
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            if User_conference.objects.filter(user=request.user.pk, conference=conf).exists():
                comment = form.save(commit=False)
                comment.op = op
                comment.save()
            else:
                comment = form.save(commit=False)
                comment.op = op
                comment.save()

                us = request.user.pk
                tim = timezone.now()
                cursor11 = connection.cursor()
                cursor11.execute("INSERT INTO new_user_conference (message, published_us_confr, conference_id, status_role_id, status_user_id, user_id) values('', %s, %s, 3, 2, %s)",[tim, conf, us])
           # return render(request, 'new/opisanie_material.html', {'op': op})
            return redirect('new.views.opisanie_material', pk=pk)
    else:
       # form = CommentForm()
        zinfo =  get_object_or_404(Conference_material, pk=pk)
        dd3 = request.user.pk
        cursor2 = connection.cursor()
        cursor2.execute("select id from new_foto_user where user_id=%s;", [dd3])
        row = cursor2.fetchone()
        if row == None:
            form = CommentForm(initial={'post': zinfo.pk, 'author': request.user})
            return render(request, 'new/add_comment_to_post.html', {'form': form})
        else:
            row2 = min(row)
            foto  =  get_object_or_404(Foto_user, pk=row2)
            form = CommentForm(initial={'post': zinfo.pk, 'author':request.user, 'fotourl':foto.pk})
            return render(request, 'new/add_comment_to_post.html', {'form': form})

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('opisanie_material', pk=comment.op.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.op.pk
    comment.delete()
    op = get_object_or_404(Conference_material, pk=post_pk)
    return render(request, 'new/opisanie_material.html', {'op': op})

#Форма для ответа
def otvet_na_coment(request, pk):
   # op = get_object_or_404(Conference_material, pk=pk)
    if request.method == "POST":
        #zinfo2 = get_object_or_404(Comment, pk=pk)
        form = CommentForm(request.POST)
        if form.is_valid():
            op = form.cleaned_data['post']
            zinfo = get_object_or_404(Comment, pk=pk)
            conf =  get_object_or_404(Conference_material, pk=zinfo.post.pk)
            if User_conference.objects.filter(user=request.user.pk, conference=conf.conference.pk).exists():
                comment = form.save(commit=False)
                comment.save()
            else:

                comment = form.save(commit=False)
                comment.save()
                user = request.user.pk
                dd13 = timezone.now()
                conf=conf.conference.pk
                cursor12 = connection.cursor()
                cursor12.execute("INSERT INTO new_user_conference (message, published_us_confr, conference_id, status_role_id, status_user_id, user_id) values('', %s, %s, 3, 2, %s)",[dd13, conf, user])

            zinfo = get_object_or_404(Comment, pk=pk)

            return redirect('new.views.opisanie_material', pk=zinfo.post_id)
           # return render(request, 'new/confmaterial_stert.html')
    else:

        zinfo = get_object_or_404(Comment, pk=pk)

        dd3 = request.user.pk
        cursor2 = connection.cursor()
        cursor2.execute("select id from new_foto_user where user_id=%s;", [dd3])
        row = cursor2.fetchone()
        if row == None:
            form = CommentForm(initial={'post': zinfo.post_id, 'author':request.user, 'parent':zinfo.pk})
            return render(request, 'new/otvet_na_coment.html', {'form': form})
        else:
            row2 = min(row)
            foto = get_object_or_404(Foto_user, pk=row2)
            form = CommentForm(initial={'post': zinfo.post_id, 'author':request.user, 'parent':zinfo.pk, 'fotourl': foto.pk})
            return render(request, 'new/otvet_na_coment.html', {'form': form})

    #     form = CommentForm(initial={'post': zinfo.post_id, 'author':request.user, 'parent':zinfo.pk})
    # return render(request, 'new/otvet_na_coment.html', {'form': form})

def udalen(request, pk):
    # PostgreSQL Запрос на обновление статуса в таблице материалов для комнат
    ss = pk
    zinfo = get_object_or_404(Comment, pk=pk)
    op = get_object_or_404(Conference_material, pk=zinfo.post_id)
    cursor = connection.cursor()
    cursor.execute("DELETE FROM new_comment WHERE parent_id = %s;", [ss])
    cursor2 = connection.cursor()
    cursor2.execute("DELETE FROM new_comment WHERE id = %s;", [ss])
    # PostgreSQL Запрос на обновление статуса в таблице материалов для комнат END
    return render(request, 'new/opisanie_material.html', {'op': op})

def del_com(request, pk):
    # PostgreSQL Запрос на обновление статуса в таблице материалов для комнат
    ss = pk
    zinfo = get_object_or_404(Comment, pk=pk)
    op = get_object_or_404(Conference_material, pk=zinfo.post_id)
    cursor = connection.cursor()
    cursor.execute("DELETE FROM new_comment WHERE parent_id = %s;", [ss])
    cursor2 = connection.cursor()
    cursor2.execute("DELETE FROM new_comment WHERE id = %s;", [pk])
    # PostgreSQL Запрос на обновление статуса в таблице материалов для комнат END
    return render(request, 'new/opisanie_material.html', {'op': op})

#Добавление секции
def section_dob(request, pk):
    sections = Section.objects.filter(confer=pk)
    if request.method == "POST":
        form = SectionForm(request.POST)
        if form.is_valid():
           dd2 = form.cleaned_data['section_name']
           dd3 = form.cleaned_data['confer']
           if Section.objects.filter(section_name=dd2, confer=dd3 ).exists():
               form = SectionForm(initial={'confer': pk})
               messages.error(request, 'Такая секция уже существует! Введите другое название секции.')
               return render(request, 'new/section_dob.html', {'form': form})
           else:
               post = form.save(commit=False)
               post.save()
        conferences = Conference.objects.filter(authorconf=request.user.pk)
        sections = Section.objects.filter(confer=pk)
        return redirect('new.views.spisoc_section', pk=pk)
        #return render(request, 'new/my_conferents.html', {'conferences': conferences})
    else:
        #items = get_object_or_404(auth, id=user_id)
        form = SectionForm(initial={'confer': pk})
        return render(request, 'new/section_dob.html', {'form': form})

#Список секций
def spisoc_section(request, pk):
    sections = Section.objects.filter(confer = pk)

    return render(request, 'new/spisoc_section.html', {'sections': sections})

#Заявка на добавление в конференцию
def uchastie_confer(request, id):
    if request.method == "POST":
       form = NameForm3(request.POST)
       if form.is_valid():
          # if form.cleaned_data['your_name']=="":
          #    dd2 = 'Пользователь не оставил комментарий.'
          # else:
          #     dd2 = form.cleaned_data['your_name']

          dd = form.cleaned_data['confer']
          dd4 = request.user.pk
          dd3 = timezone.now()

          if User_conference.objects.filter(conference=dd, user=dd4).exists():
              messages.error(request, 'Вы уже являетесь участником этой комнат.')
              form = NameForm3(initial={'confer': id, 'user': request.user.pk})
              # return render(request, 'new/Twstper.html', {'form': form})
              return render(request, 'new/uchastie_confer.html', {'form': form})
          else:
             cursor2 = connection.cursor()
             cursor2.execute("INSERT INTO new_user_conference (message, published_us_confr, conference_id, status_role_id, status_user_id, user_id) values('', %s, %s, 3, 2, %s)", [ dd3, dd, dd4])
             conference = get_object_or_404(Conference, pk=id)
      # return render(request, 'new/post_detail_confer.html', {'conference': conference})
       return redirect('new.views.post_detail_confer', pk=id)
    else:

       form = NameForm3(initial={'confer':id, 'user': request.user.pk})
       #return render(request, 'new/Twstper.html', {'form': form})
       return render(request, 'new/uchastie_confer.html', {'form': form})

#Список участников комнаты
def usmyconf(request, pk):
    conference = get_object_or_404(Conference, pk=pk)
    return render(request, 'new/usmyconf.html', {'conference': conference})

def smena_status(request, pk):
    ss=pk
    cursor = connection.cursor()
    cursor.execute("UPDATE new_user_conference SET status_user_id = '2' WHERE id=%s", [ss])
    #cursor3 = connection.cursor()
    #cursor3.execute("select conference_id from new_user_conference where id=%s;", [ss])
    #row = cursor3.fetchone()
    conferences = Conference.objects.filter(authorconf = request.user.pk);
    return render(request, 'new/my_conferents.html', {'conferences': conferences})

def lock_status(request, pk):
    ss=pk
    cursor = connection.cursor()
    cursor.execute("UPDATE new_user_conference SET status_user_id = '3' WHERE id=%s", [ss])
    #cursor3 = connection.cursor()
    #cursor3.execute("select conference_id from new_user_conference where id=%s;", [ss])
    #row = cursor3.fetchone()
    conferences = Conference.objects.filter(authorconf = request.user.pk);
    return render(request, 'new/my_conferents.html', {'conferences': conferences})

def us_conf_full(request, pk):
    conference = get_object_or_404(Conference, pk=pk)
    return render(request, 'new/us_conf_full.html', {'conference': conference})

def zamen_stutus(request, pk):
    ss=pk
    cursor = connection.cursor()
    cursor.execute("UPDATE new_user_conference SET status_user_id = '2' WHERE id=%s", [ss])
    #cursor3 = connection.cursor()
    #cursor3.execute("select conference_id from new_user_conference where id=%s;", [ss])
    #row = cursor3.fetchone()
    conferences = Conference.objects.filter(authorconf = request.user.pk);
    return render(request, 'new/full_list_confer.html', {'conferences': conferences})

def bloc_user(request, pk):
    ss=pk
    cursor = connection.cursor()
    cursor.execute("UPDATE new_user_conference SET status_user_id = '3' WHERE id=%s", [ss])
    #cursor3 = connection.cursor()
    #cursor3.execute("select conference_id from new_user_conference where id=%s;", [ss])
    #row = cursor3.fetchone()
    conferences = Conference.objects.filter(authorconf = request.user.pk);
    return render(request, 'new/full_list_confer.html', {'conferences': conferences})

#Форма для востановления пароля из учетной записи от лица админа сайта
def pass_edit(request, pk):
    post = get_object_or_404(User, pk=pk)
    if request.method == "POST":
        form = Pass(request.POST, instance=post)
        if form.is_valid():
          # dd2 = form.cleaned_data['password']
           #form.password = make_password(dd2, 'pbkdf2_sha256')

           tek_user = form.save(commit=False)
           tek_user.set_password(form.cleaned_data['password'])
           tek_user.save()
           #select id from auth_user where username='Admin';
           # form.save()
           user4 = User.objects.all()
           return render(request, 'new/user_list.html', {'user4': user4})
        # else:
        #     zinfo = get_object_or_404(User, pk=pk)
        #     return render(request, 'new/pass_edit.html', {'form': form})
    else:
        # взять из таблицы/модели contactform nameconfer  по id
        zinfo = get_object_or_404(User, pk=pk)
        form = Pass(initial={'first_name': zinfo.first_name, 'last_name':zinfo.last_name,
                                       'patronymic': zinfo.patronymic, #'data_birth': zinfo.data_birth,
                                       'phone': zinfo.phone, #'address': zinfo.address,
                                       #'pol': zinfo.pol,
                                       #'academemic_degree': zinfo.academemic_degree, 'position': zinfo.position,
                                       #'uchenoe_zvanie': zinfo.uchenoe_zvanie,
                                       #'organization': zinfo.organization, 'country':zinfo.country, #'rinc_author':zinfo.rinc_author,
                                   'username': zinfo.username, 'security_question':zinfo.security_question, 'check_answer':zinfo.check_answer
                                  # 'email': zinfo.email, 'password': zinfo.password
                                  })
        # return render(request, 'new/conference_new2.html', {'items': items})
        return render(request, 'new/pass_edit.html', {'form': form})


def new_pass(request):
    if request.method == "POST":
        form = New_pass(request.POST)
        if form.is_valid():
            dd2 = form.cleaned_data['username']

            if User.objects.filter(username=dd2).exists():
                  cursor3 = connection.cursor()
                  cursor3.execute("select id from auth_user where username=%s;", [dd2])
                  row = cursor3.fetchone()
                  row2 = min(row)

                  zinfo = get_object_or_404(User, pk=row2)
                  # dd = New_pass2(initial={'pk': zinfo.id, 'username': zinfo.username, 'security_question': zinfo.security_question,
                  #                         'password':"asdf12534"})
                  # form = New_pass2(initial={'pk':row, 'username':row2, 'security_question':row3})
                  return redirect('new.views.log_zaregn', pk=zinfo.pk)
                  #return render(request, 'new/log_zaregn.html', {'dd': dd})
                 # HttpResponse(render(request, 'new/log_zaregn.html', {'dd': dd}))
                  # template = loader.get_template("new/log_zaregn.html")
                  # context = {'dd': dd}
                  # return HttpResponse(template.render(context, request))
                  #return render_to_response('new/log_zaregn.html')
            else:
                messages.error(request, 'Такой Логин не зарегистрирован!')
                form = New_pass()
                return render(request, 'new/new_pass.html', {'form': form})
    else:
        form = New_pass()
        return render(request, 'new/new_pass.html', {'form': form})


def log_zaregn(request, pk):
     zinfo = get_object_or_404(User, pk=pk)
     if request.method == "POST":
        dd = Pass(request.POST, instance=zinfo)
        if dd.is_valid():
            dd2 = dd.cleaned_data['check_answer']
            #dd1 = dd.cleaned_data['pk']
            #dd5 = dd.cleaned_data['password']
            #dd8 = dd.set_password(dd5)
            if User.objects.filter(check_answer=dd2, id=pk).exists():
                tek_user = dd.save(commit=False)
                tek_user.set_password(dd.cleaned_data['password'])
                tek_user.save()
                #messages.error(request, 'Пароль изменен. Для входа воспользуйтесь логином и новым паролем.')
                #zinfo = get_object_or_404(User, pk=pk)
                #return HttpResponse('new/finish_pass.html')
                return render(request, 'new/finish_pass.html', {'zinfo': zinfo})
            else:
                messages.error(request, 'Ответ на контрольный вопрос неверный!')
                zinfo = get_object_or_404(User, pk=pk)
                form = Pass(initial={'first_name': zinfo.first_name, 'last_name': zinfo.last_name,
                          'patronymic': zinfo.patronymic, #'data_birth': zinfo.data_birth,
                          'phone': zinfo.phone, 
						  #'address': zinfo.address,
                          #'pol': zinfo.pol,
                          #'academemic_degree': zinfo.academemic_degree, 'position': zinfo.position,
                          #'uchenoe_zvanie': zinfo.uchenoe_zvanie,
                          #'organization': zinfo.organization, 'country': zinfo.country,
                          #'rinc_author': zinfo.rinc_author,
                          'username': zinfo.username, 'security_question': zinfo.security_question,

                          # 'email': zinfo.email, 'password': zinfo.password
                          })
                #return HttpResponseRedirect('new/finish_pass.html')
                #return redirect('new.views.log_zaregn', pk=zinfo.pk)
                return render(request, 'new/log_zaregn.html', {'form': form})
     else:
         zinfo = get_object_or_404(User, pk=pk)

         form = Pass(initial={'first_name': zinfo.first_name, 'last_name': zinfo.last_name,
                          'patronymic': zinfo.patronymic, #'data_birth': zinfo.data_birth,
                          'phone': zinfo.phone, #'address': zinfo.address,
                          #'pol': zinfo.pol,
                          #'academemic_degree': zinfo.academemic_degree, 'position': zinfo.position,
                          #'uchenoe_zvanie': zinfo.uchenoe_zvanie,
                          #'organization': zinfo.organization, 
						  #'country': zinfo.country,
                          #'rinc_author': zinfo.rinc_author,
                          'username': zinfo.username, 'security_question': zinfo.security_question,
                          'check_answer':''
                          # 'email': zinfo.email, 'password': zinfo.password
                          })
     # return render(request, 'new/conference_new2.html', {'items': items})
         return render(request, 'new/log_zaregn.html', {'form': form})

# def finish_pass(request):
#
#     if request.method == "POST":
#         form = Pass(request.POST, instance=post)
#         if form.is_valid():
#           # dd2 = form.cleaned_data['password']
#            #form.password = make_password(dd2, 'pbkdf2_sha256')
#            tek_user = form.save(commit=False)
#            tek_user.set_password(form.cleaned_data['password'])
#            tek_user.save()
#            #select id from auth_user where username='Admin';
#            # form.save()
#            return render(request, 'new/goodeditus.html', {'form': form})
#         else:
#             zinfo = get_object_or_404(User, pk=pk)
#             return render(request, 'new/pass_edit.html', {'form': form})

def otmen_public_material(request, id):
    ss = id
    if request.method == "POST":
       form = NameForm(request.POST)
       if form.is_valid():
          dd2 = form.cleaned_data['your_name']
          cursor2 = connection.cursor()
          cursor2.execute("UPDATE new_conference_material SET message_com = %s WHERE id=%s", [dd2, ss])
       return render(request, 'new/comgoto.html')
    else:

       cursor = connection.cursor()
       cursor.execute("UPDATE new_conference_material SET status_id='3' WHERE id=%s", [ss])
       form = NameForm()
       #return render(request, 'new/Twstper.html', {'form': form})
       return render(request, 'new/otmen_public_material.html', {'form': form})


# Форма для редактирования секции-------------------------------
def redak_secti(request, id):
    post = get_object_or_404(Section, pk=id)
    # items = Conference.objects.all();
    if request.method == "POST":
        form = SectionForm(request.POST, instance=post)
        if form.is_valid():
            # form.published_datematerial = timezone.now();
            dd2 = form.cleaned_data['confer']
            dd3 = id
            dd4 = form.cleaned_data['section_name']
           # dd5 = form.cleaned_data['comentsection']
            if Section.objects.filter(section_name=dd4, confer=dd2).exclude(id=dd3).exists():
                messages.error(request, 'Такая секция уже существует! Введите другое название секции.')
                form = SectionForm(initial={'confer': dd2})
                return render(request, 'new/redak_secti.html', {'form': form})
            else:
                form.save()
                sections = Section.objects.filter(confer=dd2)
                return render(request, 'new/spisoc_section.html', {'sections': sections})
    # return render(request, 'new/spisoc_section.html', {'form': form})
    else:
         matfo = get_object_or_404(Section, id=id)
         form = SectionForm(initial={'confer': matfo.confer, 'section_name': matfo.section_name})
    return render(request, 'new/redak_secti.html', {'form': form})
#------------------------------------------------------------------

#Форма для редактирования организации (один из разделов для фильтрации комнат и идей)-------------------------------
def org_edit(request, id):
    post = get_object_or_404(Organization, pk=id)
    if request.method == "POST":
        form = OrganizationForm(request.POST, instance=post)
        if form.is_valid():
           dd11 = form.cleaned_data['full_name']

           if Organization.objects.filter(full_name=dd11).exclude(id=id).exists():
               messages.error(request, 'Такая организация уже есть в справочнике.')
               form = OrganizationForm()
               return render(request, 'new/org_edit.html', {'form': form})
           else:
               post = form.save(commit=False)
               post.save()
               orgs = Organization.objects.all();
               return render(request, 'new/vseorganization.html', {'orgs': orgs})
    else:
         org = get_object_or_404(Organization, pk=id)
         form = OrganizationForm(initial={'full_name': org.full_name, 'short_name': org.short_name})
		 #form = OrganizationForm(initial={'full_name':org.full_name, 'short_name': org.short_name})
         return render(request, 'new/org_edit.html', {'form': form})
#--------------------------------------------------------------------

# Форма для редактирования должности (для фильтрации)-------------------------------
def posit_edit(request, id):
    post = get_object_or_404(Position, pk=id)
    if request.method == "POST":
        form = PositionForm(request.POST, instance=post)
        if form.is_valid():
            dd11 = form.cleaned_data['full_name']

            if Position.objects.filter(full_name=dd11).exclude(id=id).exists():
                messages.error(request, 'Такая должность уже есть в справочнике.')
                form = PositionForm()
                return render(request, 'new/posit_edit.html', {'form': form})
            else:
                post = form.save(commit=False)
                post.save()
                posits = Position.objects.all();
                return render(request, 'new/positionspisok.html', {'posits': posits})
    else:
        pos = get_object_or_404(Position, pk=id)
        form = PositionForm(initial={'full_name': pos.full_name, 'short_name': pos.short_name})
        # form = OrganizationForm(initial={'full_name':org.full_name, 'short_name': org.short_name})
        return render(request, 'new/posit_edit.html', {'form': form})
 # --------------------------------------------------------------------


def photo_us1(request, pk):
    if request.method == "POST":
        # if request.method == "POST":
            foto = Foto_userForm(request.POST, request.FILES)
            if foto.is_valid():
               # foto.cleaned_data['name'] = foto.cleaned_data['foto']
                post = foto.save(commit=False)
                post.save()

                #foto.save()
                dd=post.pk
                post2 = get_object_or_404(Foto_user, pk=dd)
                dd2=post2.foto.name
                cursor = connection.cursor()
                cursor.execute("UPDATE new_foto_user SET name=%s WHERE id=%s", [dd2, dd])

                return redirect('new.views.user_profile', pk=pk)
    else:
        foto = Foto_userForm(initial={'user': pk})
    return render(request, 'new/photo_us1.html', {'foto': foto})

def ed_us_foto(request, pk):
    post=get_object_or_404(Foto_user, pk=pk)
    if request.method == "POST":
        post = get_object_or_404(Foto_user, pk=pk)
        default_storage.delete(post.foto.name)
        foto = Foto_userForm(request.POST, request.FILES, instance=post)
        if foto.is_valid():
            foto.save()

            post2 = get_object_or_404(Foto_user, pk=pk)
            dd2 = post2.foto.name
            cursor = connection.cursor()
            cursor.execute("UPDATE new_foto_user SET name=%s WHERE id=%s", [dd2, pk])

            return redirect('new.views.user_profile', pk=request.user.pk)
            #return HttpResponseRedirect('new/post_list.html')
    else:
        post = get_object_or_404(Foto_user, pk=pk)
        foto = Foto_userForm(initial={'user': post.user})
        return render(request, 'new/ed_us_foto.html', {'foto': foto})

#Страница подробнее для секций
def step_backward(request, pk):
   # op = get_object_or_404(Conference_material, pk=pk)
    materials = Conference_material.objects.filter(section=pk)
    return render(request, 'new/step_backward.html', {'materials': materials})

#Блокировка пользователя
def lock_us(request, id):
    cursor = connection.cursor()
    cursor.execute("UPDATE auth_user SET is_active=0 WHERE id=%s", [id])
    user4 = User.objects.all()
    return render(request, 'new/user_list.html', {'user4': user4})

#Разблокировать пользователя
def unlock_us(request, id):
    cursor = connection.cursor()
    cursor.execute("UPDATE auth_user SET is_active=True WHERE id=%s", [id])
    user4 = User.objects.all()
    return render(request, 'new/user_list.html', {'user4': user4})


#"Удаление" автором идей и предложений
def otmenpublic(request, id):
    cursor = connection.cursor()
    cursor.execute("UPDATE new_conference_material SET otmenpublic=FALSE WHERE id=%s", [id])
    ff = request.user.pk
    #materials = Conference_material.objects.filter(authormatirial=ff);
    return redirect('new.views.my_material', pk=ff)

#"Востановление" автором идей и предложений
def vostanov(request, id):
    cursor = connection.cursor()
    cursor.execute("UPDATE new_conference_material SET otmenpublic=TRUE WHERE id=%s", [id])
    ff = request.user.pk
    #materials = Conference_material.objects.filter(authormatirial=ff);
    return redirect('new.views.my_material', pk=ff)	
	


#Тест древовидные данные
# def derevo(request):
#     nauks = Branch_science.objects.all().order_by('-id')
#     orgs = Organization.objects.all().order_by('-id')
#     years = Years.objects.all().order_by('-id')
#     confs = Conference.objects.all().order_by('-id')
#     return render(request, 'new/derevo.html', {'nauks': nauks, 'orgs':orgs, 'years':years, 'confs':confs})

def del_sectionfull(request, pk):
    dd3 = pk
    dd = get_object_or_404(Section, pk=pk)

    cursor2 = connection.cursor()
    cursor2.execute("select id from new_conference_material where section_id=%s;", [dd3])
    row = cursor2.fetchone()
    if row == None:
        cursor7 = connection.cursor()
        cursor7.execute("DELETE FROM new_section WHERE id = %s;", [dd3])
        sections = Section.objects.filter(confer=dd.confer)

        return render(request, 'new/spisoc_section.html', {'sections': sections})


    else:
        # messages.error(request, 'Нельзя удалить данную секцию (т.к. к секции прикреплен материал).')
        messages.info(request, 'Нельзя удалить данную секцию (т.к. к секции прикреплен материал).')
        sections = Section.objects.filter(confer=dd.confer)
        return render(request, 'new/spisoc_section.html', {'sections': sections})

