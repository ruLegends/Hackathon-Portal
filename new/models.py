from django.db import models
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField
from pytils import translit
from django.utils.crypto import random


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

		
		
class Test23(models.Model):
    user_id = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=15, blank=True, null=True)
    class Meta:
       managed = False
       db_table = 'test23'

#Модель для конференции
class Conference(models.Model):
    authorconf = models.ForeignKey('auth.User', verbose_name=u"Организатор конференции")
    org = models.ForeignKey('new.Organization', verbose_name=u"Организация", blank=True, null=True, related_name='children')
    branch_science = models.ForeignKey('new.Branch_science', verbose_name=u'Отрасль науки', related_name='children')
    titleconf = models.CharField(max_length=200, verbose_name=u"Тема конференции")
    textconf = RichTextUploadingField(verbose_name=u"Текст", blank=True, default='')
    trebovania = models.ForeignKey('new.Trebovania_public', verbose_name=u'Требования к публикации', blank=True, null=True)
    date_launch_s = models.CharField(verbose_name=u"Время проведения конференции с", max_length=10)
    date_launch_po = models.CharField(verbose_name=u"по", max_length=10)
    srok_podacha = models.CharField(verbose_name=u"Срок подачи статей и докладов", max_length=10)
    srok_prin_resh_itog = models.CharField(verbose_name=u"Срок принятия решений по итогам конференции", max_length=10)
    sostav_orgkomitet = RichTextUploadingField(verbose_name=u"Текст", blank=True, default='')
    #section = models.ForeignKey('new.Section', verbose_name=u"Секция")
    otmenpublic = models.BooleanField(verbose_name=u"Снять с публикации")

    year1 = models.ForeignKey('new.Years', verbose_name=u'Год1', related_name='children2', blank=True, null=True)
    year2 = models.ForeignKey('new.Years', verbose_name=u'Год2', related_name='children3', blank=True, null=True)

    created_dateconf = models.DateTimeField(
            default=timezone.now)
    published_dateconf = models.DateTimeField(
            blank=True, null=True, verbose_name=u"Дата создания конференции")

    class Meta:
        verbose_name = u'Конференцию'
        verbose_name_plural = u'Конференции'

    def publish(self):
        self.published_dateconf = timezone.now()
        self.save()

    def __str__(self):
        return self.titleconf

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>

    dd222=random.random()
    dd=instance.titlematirial
    if '.pdf' in filename:
        return 'media/conf/conf_{0}/{1}.pdf'.format(instance.conference.id, translit.slugify(dd))
       # return 'media/conf/conf_{0}/{1}.pdf'.format(instance.conference.id, dd222)
    else:
        return 'media/conf/conf_{0}/{1}.docx'.format(instance.conference.id, translit.slugify(dd))
       # return 'media/conf/conf_{0}/{1}.docx'.format(instance.conference.id, dd222)

class Conference_material(models.Model):
    conference = models.ForeignKey('new.Conference', verbose_name=u"Материал для конференции")
    branch_science = models.ForeignKey('new.Branch_science', verbose_name=u'Отрасль науки')
    org = models.ForeignKey('new.Organization', verbose_name=u"Организация", blank=True, null=True, related_name='tt')
    titlematirial = models.CharField(max_length=140, verbose_name=u"Заголовок")
    authormatirial = models.ForeignKey('auth.User', verbose_name=u"Создатель материала")
    authormatirial2 = models.CharField(max_length=340, verbose_name=u"Автор материала")
    textmaterial = RichTextUploadingField(verbose_name=u"Текст", blank=True, default='')
    message_com = models.TextField(verbose_name=u"Комментарий администратора", max_length=1300, blank=True)
    status = models.ForeignKey('new.Status_contact', verbose_name=u'Статус материала')
    section = models.ForeignKey('new.Section', verbose_name=u'Секция', blank=True, null=True, related_name='children')
    file_obj = models.FileField(verbose_name=u'Файл для материала', upload_to=user_directory_path, blank=True, max_length=2500)
    otmenpublic = models.BooleanField(verbose_name=u"Снять с публикации")

    annotation_rus = models.TextField(verbose_name=u"Аннотация (Rus)", blank=True, null=True)
    annotation_usa = models.TextField(verbose_name=u"Аннотация (Eng)", blank=True, null=True)
    keywords_rus = models.TextField(verbose_name=u"Ключевые слова (Rus)", blank=True, null=True)
    keywords_usa = models.TextField(verbose_name=u"Ключевые слова (Eng)", blank=True, null=True)

    created_datematerial = models.DateTimeField(
            default=timezone.now)
    published_datematerial = models.DateTimeField(
            blank=True, null=True, verbose_name=u"Дата публикации")

    class Meta:
        verbose_name = u'Материал для конференции'
        verbose_name_plural = u'Материалы для конференций'

    def publish(self):
        self.published_datematerial = timezone.now()
        self.save()

    def __str__(self):
        return self.titlematirial



class ContactForm(models.Model):
    login_user = models.ForeignKey('auth.User', verbose_name=u"Имя пользователя")
   # fam = models.CharField(verbose_name=u"Фамилия", max_length=300)
   # name = models.CharField(verbose_name=u"Имя", max_length=300)
   # otch = models.CharField(verbose_name=u"Отчество", max_length=300)
   # email = models.EmailField(verbose_name=u"Почта", max_length=300)
   # telfon = models.CharField(verbose_name=u"Номер телефона", max_length=300)
    # datasoz=forms.DateField.auto_now_add(label='Дата обращения')
    org = models.ForeignKey('new.Organization', verbose_name=u"Организация", blank=True, null=True)
    branch_science = models.ForeignKey('new.Branch_science', verbose_name=u'Отрасль науки')
    nameconfer = models.CharField(verbose_name=u"Тема конференции", max_length=300)
    date_launch_s = models.CharField(verbose_name=u"Время проведения конференции с", max_length=10, blank=True)
    date_launch_po = models.CharField(verbose_name=u"по", max_length=10, blank=True)
    srok_podacha = models.CharField(verbose_name=u"Срок подачи статей и докладов", max_length=10, blank=True)
    srok_prin_resh_itog = models.CharField(verbose_name=u"Срок принятия решений по итогам конференции", max_length=10, blank=True)
    message = RichTextUploadingField(verbose_name=u"Описание конференции и требования к публикации", blank=True, default='')
    trebovania = models.ForeignKey('new.Trebovania_public', verbose_name=u'Требования к публикации', blank=True, null=True)
    sostav_orgkomitet = RichTextUploadingField(verbose_name=u"Текст", blank=True, default='')
    status = models.ForeignKey('new.Status_contact', verbose_name=u'Статус заявки')
    message_com = models.TextField(verbose_name=u"Комментарий администратора", max_length=1300, blank=True, null=True)
    published_contact = models.DateTimeField(
        blank=True, null=True, verbose_name=u"Дата отправки заявки")

    class Meta:
        verbose_name = u'Заявка на создание конференции'
        verbose_name_plural = u'Заявки на создание конференций'

    def publish(self):
        self.published_contact = timezone.now()
        self.save()

    def __str__(self):
        return self.nameconfer

class Pol(models.Model):
    namepole = models.CharField(max_length=200, verbose_name=u"Пол")
    def __str__(self):
        return self.namepole

class Academic_degree(models.Model):
    full_name = models.CharField(max_length=300, verbose_name=u"Полное название")
    short_name = models.CharField(max_length=200, verbose_name=u"Сокращенное название")

    class Meta:
        verbose_name = u'Ученую степень'
        verbose_name_plural = u'Ученые степени'
    def __str__(self):
        return self.short_name

class Position(models.Model):
    full_name = models.CharField(max_length=300, verbose_name=u"Полное название")
    short_name = models.CharField(max_length=200, verbose_name=u"Сокращенное название")

    class Meta:
        verbose_name = u'Должность'
        verbose_name_plural = u'Должности'
    def __str__(self):
        return self.short_name

class Uchenoe_zvanie(models.Model):
    full_name = models.CharField(max_length=300, verbose_name=u"Полное название")
    short_name = models.CharField(max_length=200, verbose_name=u"Сокращенное название")

    class Meta:
        verbose_name = u'Ученое звание'
        verbose_name_plural = u'Ученые звания'
    def __str__(self):
        return self.short_name

class Organization(models.Model):
    full_name = models.CharField(max_length=300, verbose_name=u"Полное название")
    short_name = models.CharField(max_length=200, verbose_name=u"Сокращенное название")

    class Meta:
        verbose_name = u'Организацию'
        verbose_name_plural = u'Организации'
    def __str__(self):
        return self.short_name

class Countrys(models.Model):
    country = models.CharField(max_length=300, verbose_name=u"Страна")
    class Meta:
        verbose_name = u'Страну'
        verbose_name_plural = u'Страны'
    def __str__(self):
        return self.country


class Branch_science(models.Model):
    science = models.CharField(max_length=1300, verbose_name=u"Наука")
    class Meta:
        verbose_name = u'Отрасль науки'
        verbose_name_plural = u'Отрасли наук'

    def __str__(self):
        return self.science

class Trebovania_public(models.Model):
    trebovania = models.CharField(max_length=1000, verbose_name=u'Требования к публикации')
    class Meta:
        verbose_name = u'Требование к публикации'
        verbose_name_plural = u'Требования к публикации'

    def __str__(self):
        return self.trebovania

class Section(models.Model):
    section_name = models.CharField(max_length=300, verbose_name=u"Секция")
    comentsection = models.CharField(max_length=300, verbose_name=u"Подробнее", blank=True, null=True)
    confer = models.ForeignKey('new.Conference', verbose_name=u"Конференция", related_name='children')

    class Meta:
        verbose_name = u'Секцию'
        verbose_name_plural = u'Секции'

    def __str__(self):
        return self.section_name

class Status_contact(models.Model):
    status_contact = models.CharField(max_length=300, verbose_name=u"Статус")

    class Meta:
        verbose_name = u'Статус'
        verbose_name_plural = u'Статусы'

    def __str__(self):
        return self.status_contact


# class File_doc_rtf(models.Model):
#     file_obj = models.FileField(upload_to = user_directory_path)

class Comment(models.Model):
    post = models.ForeignKey('new.Conference_material', related_name='comments')
    parent = models.ForeignKey('new.Comment', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    #parent2 = models.ForeignKey('new.Comment', blank=True, null=True, related_name='children2', on_delete=models.CASCADE)
    author = models.ForeignKey('auth.User', verbose_name=u"Имя пользователя")
    text = models.TextField(verbose_name=u"Комментарий", max_length=1300)
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)
    fotourl = models.ForeignKey('new.Foto_user', verbose_name=u'Фото',  blank=True, null=True)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)


class Status_user(models.Model):
    name = models.CharField(max_length=300, verbose_name=u"Статус_user")

    class Meta:
        verbose_name = u'Статус_user'
        verbose_name_plural = u'Статусы_user'

    def __str__(self):
        return self.name

class Status_role(models.Model):
    name = models.CharField(max_length=300, verbose_name=u"Статус_admin")

    class Meta:
        verbose_name = u'Статус_admin'
        verbose_name_plural = u'Статусы_admin'

    def __str__(self):
        return self.name


class User_conference(models.Model):
    conference = models.ForeignKey('new.Conference', verbose_name=u"Конференция", related_name='children2')
    user = models.ForeignKey('auth.User', verbose_name=u"Пользователь", related_name='uchconf')
    message = models.TextField(verbose_name=u"Описание конференции", max_length=1300, blank=True, null=True)
    status_user = models.ForeignKey('new.Status_user', verbose_name=u"Статус пользователя")
    status_role = models.ForeignKey('new.Status_role', verbose_name=u"Роли конференции")
    published_us_confr = models.DateTimeField(
        blank=True, null=True, verbose_name=u"Дата отправки запроса на добавление в конференцию")

    def publish(self):
        self.published_us_confr = timezone.now()
        self.save()

    def __str__(self):
        return self.message

def user_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    dd = instance.user.pk
    if '.png' in filename:
        return 'media/user/{0}.png'.format(dd)
       # return 'media/conf/conf_{0}/{1}.pdf'.format(instance.conference.id, dd222)
    else:
        return 'media/user/{0}.jpg'.format(dd)
       # return 'media/conf/conf_{0}/{1}.docx'.format(instance.conference.id, dd222)

class Foto_user(models.Model):
    user = models.ForeignKey('auth.User', blank=True, null=True, related_name='fotos')
    foto = models.FileField(verbose_name=u'Файл для материала', upload_to=user_path, blank=True, max_length=2500)
    name = models.CharField(max_length=300,  blank=True, null=True)

    class Meta:
        verbose_name = u'Фото'
        verbose_name_plural = u'Фото'

    def __str__(self):
        return self.name


class Years(models.Model):
    year = models.CharField(max_length=10, verbose_name=u"Год")

    class Meta:
        verbose_name = u'Год'
        verbose_name_plural = u'Годы'

    def __str__(self):
        return self.year


