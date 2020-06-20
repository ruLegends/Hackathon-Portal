from django import forms
from .models import Post
from .models import ContactForm
from .models import Conference
from .models import Conference_material
from .models import Position
from .models import Organization
from ckeditor.fields import RichTextField
from .models import Trebovania_public
from django.utils.safestring import mark_safe
from .models import Status_contact
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.forms import UserCreationForm
from .models import Comment
from .models import Section
from .models import Foto_user




class EventSplitDateTime(forms.SplitDateTimeWidget):
    def __init__(self, attrs=None):
        widgets = [forms.TextInput(attrs={'class': 'vDateField'}),
                   forms.TextInput(attrs={'class': 'vTimeField'})]
        # Note that we're calling MultiWidget, not SplitDateTimeWidget, because
        # we want to define widgets.
        forms.MultiWidget.__init__(self, widgets, attrs)

    def format_output(self, rendered_widgets):
        return mark_safe(u'%s<br />%s' % (rendered_widgets[0], rendered_widgets[1]))

class PostForm(forms.ModelForm):

        class Meta:
            model = Post
            fields = ('title', 'text',)


class ContactFormForm(forms.ModelForm):

         class Meta:
            model = ContactForm
            fields = (
                     # 'fam',
                     # 'name',
                     # 'otch',
                     # 'email',
                     # 'telfon',
                      'org',
                      'branch_science',
                      'nameconfer',
                      'date_launch_s',
                      'date_launch_po',
                      'srok_podacha',
                      'srok_prin_resh_itog',
                      'message',
                      'trebovania',
                      'sostav_orgkomitet',
                      'status',
                      'published_contact',
                      )


class ConferenceForm(forms.ModelForm):
       # filter_horizontal = ('titleconf', 'org', 'branch_science', 'textconf',)
        class Meta:
            model = Conference
            fields = ('authorconf',
                      'org',
                      'published_dateconf',
                      'date_launch_s',
                      'date_launch_po',
                      'srok_podacha',
                      'srok_prin_resh_itog',
                      'branch_science',
                      'titleconf',
                      'textconf',
                      'trebovania',
                      'sostav_orgkomitet',
                      'otmenpublic',
                     )



class Conference_materialForm(forms.ModelForm):

        def __init__(self, id, *args, **kwargs):
        #       id=kwargs.pop('id', None)
               super(Conference_materialForm, self).__init__(*args, **kwargs)
        # #     # if self.instance.conference:
        # #     #    #dd = (self.instance.conference.pk)
        # #
               self.fields['section'].queryset = Section.objects.filter(confer = id)

        class Meta:
            model=Conference_material
            fields=('branch_science',
                    'conference',
                    'titlematirial',
                    'authormatirial',
                    'authormatirial2',
                    'textmaterial',
                    'org',
                    'published_datematerial',
                    'file_obj',
                    'message_com',
                    'status',
                    'section',
                    'otmenpublic',
                    'annotation_rus',
                    'annotation_usa',
                    'keywords_rus',
                    'keywords_usa',
            )





class PositionForm(forms.ModelForm):

       class Meta:
           model=Position
           fields=(
               'full_name',
               'short_name'
           )

class OrganizationForm(forms.ModelForm):

       class Meta:
           model=Organization
           fields=(
               'full_name',
               'short_name'
           )

class NameForm(forms.Form):
    your_name = forms.CharField(widget=forms.Textarea, max_length=1000)

class NameForm2(forms.Form):
    your_name = forms.CharField(widget=forms.Textarea, max_length=1000)

class NameForm3(forms.Form):
    # your_name = forms.CharField(widget=forms.Textarea, max_length=1000)
    confer = forms.CharField(max_length=1000)
    user = forms.CharField(max_length=1000)

class Prof_user(forms.ModelForm):
    class Meta:
        model= User
        fields = (
           # 'username'
           # 'password',
            #'password2',
           # 'email',
            'last_name',
            'first_name',
            'patronymic',
            #'pol',
            #'data_birth',
            #'country',
            #'address',
           # 'organization',
            #'profession',
            'phone',
            #'organization',
            #'position',
            #'academemic_degree',
            #'uchenoe_zvanie',
            #'description',
            #'rinc_author',
            'security_question',
            'check_answer',

        )


class Pass(forms.ModelForm):
    class Meta:

        model = User
        fields = (
           'username',
            'password',
            #'password2',
           'last_name',
           'first_name',
           'patronymic',
           #'pol',
           #'data_birth',
           #'country',
           #'address',
           #'organization',
           #'profession',
           'phone',
           #'organization',
           #'position',
           #'academemic_degree',
           #'uchenoe_zvanie',
           #'description',
           #'rinc_author',
           'security_question',
           'check_answer',


        )
        widgets = {
            'password': forms.PasswordInput(),
        }



class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('parent', 'post','author', 'text', 'fotourl')

class CommentForm2(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('parent', 'post','author', 'text', 'fotourl')

class SectionForm(forms.ModelForm):

    class Meta:
        model = Section
        fields = ('section_name', 'confer',)


class New_pass(forms.Form):
    username = forms.CharField(max_length=300)
    # password = forms.CharField(max_length=30, widget=forms.PasswordInput)
    # password2 = forms.CharField(max_length=30, widget=forms.PasswordInput)
    # security_question = forms.CharField(max_length=500)
    # check_answer = forms.CharField(max_length=500)

class New_pass2(forms.Form):
     pk =  forms.CharField(max_length=10)
     username = forms.CharField(max_length=300)
     password = forms.CharField(max_length=30)
     password2 = forms.CharField(max_length=30, widget=forms.PasswordInput)
     security_question = forms.CharField(max_length=500)
     check_answer = forms.CharField(max_length=500)
     test = forms.CharField(max_length=500)


    # class Meta:
    #
    #     fields = (
    #        'username'
    #        'password',
    #        'password2',
    #
    #         'security_question',
    #         'check_answer',
    #
    #     )


class Conference_materialForm2(forms.ModelForm):

    class Meta:
        model = Conference_material
        fields = ('branch_science',
                  'conference',
                  'titlematirial',
                  'authormatirial',
                  'authormatirial2',
                  'textmaterial',
                  'org',
                  'published_datematerial',
                  'file_obj',
                  'message_com',
                  'status',
                  'section',
                  )


class Foto_userForm(forms.ModelForm):

    class Meta:
        model = Foto_user
        fields = ('user',
                  'foto',

                  )


