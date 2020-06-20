from django.conf.urls import url
from . import views
from django.conf.urls import include, url


urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
	url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
	url(r'^testpage/', views.test_list, name='test_list'),
    #url(r'^contact/$', views.contact, name='contact'),
    url(r'^contacts_list/$', views.contacts_list, name='contacts_list'),
    url(r'^contact_ditails/(?P<pk>[0-9]+)/$', views.contact_ditails, name='contact_ditails'),
    url(r'^contact', views.contact_new, name='contact_new'),
    url(r'^conferents_list/$', views.conferents_list, name='conferents_list'),
    url(r'^conferences/(?P<pk>[0-9]+)/$', views.post_detail_confer, name='post_detail_confer'),
    url(r'^edit_conferences/(?P<id>[0-9]+)/$', views.edit_conferences, name='edit_conferences'),
    url(r'^my_conferents/(?P<pk>[0-9]+)/$', views.my_conferents, name='my_conferents'),
    url(r'^conference_new2/(?P<id>[A-Za-zА-Яа-яЁё0-9\s]+)/$', views.conference_new2, name='conference_new2'),
    url(r'^material_new/(?P<id>[A-Za-zА-Яа-яЁё0-9\s]+)/$', views.material_new, name='material_new'),
    url(r'^opisanie_material/(?P<pk>[0-9]+)/$', views.opisanie_material, name='opisanie_material'),
    url(r'^ditailsmaterial/(?P<pk>[0-9]+)/$', views.ditailsmaterial, name='ditailsmaterial'),
    url(r'^my_material/(?P<pk>[A-Za-zА-Яа-яЁё0-9\s]+)/$', views.my_material, name='my_material'),
    url(r'^my_contact/(?P<pk>[A-Za-zА-Яа-яЁё0-9\s]+)/$', views.my_contact, name='my_contact'),
    url(r'^edit_material_my_conferents/(?P<pk>[A-Za-zА-Яа-яЁё0-9\s]+)/$', views.edit_material_my_conferents, name='edit_material_my_conferents'),
    url(r'^edit_material/(?P<id>[0-9]+)/$', views.edit_material, name='edit_material'),
   # url(r'^conference_new/(?P<contact_nameconfer>[A-Za-zА-Яа-яЁё\s]+)/$', views.conference_new, name='conference_new'),
    url(r'^accounts/profile/', views.post_list, name='post_list'),
    url(r'^position_dob', views.position_dob, name='position_dob'),
    url(r'^organization_dob', views.organization_dob, name='organization_dob'),
    url(r'^reference', views.reference, name='reference'),
    url(r'^user_list/', views.user_list, name='user_list'),
    url(r'^detail_user/(?P<pk>[0-9]+)/$', views.detail_user, name='detail_user'),
    url(r'^Twstper/(?P<id>[0-9]+)/$', views.Twstper, name='Twstper'),
    url(r'^conttwstper/(?P<id>[0-9]+)/$', views.conttwstper, name='conttwstper'),
    url(r'^user_profile/(?P<pk>[0-9]+)/$', views.user_profile, name='user_profile'),
    url(r'^deletcont/(?P<pk>[0-9]+)/$', views.deletcont, name='deletcont'),
    url(r'^sterta/(?P<pk>[0-9]+)/$', views.sterta, name='sterta'),
    url(r'^udalen/(?P<pk>[0-9]+)/$', views.udalen, name='udalen'),
    url(r'^udalenie_material/(?P<pk>[0-9]+)/$', views.udalenie_material, name='udalenie_material'),
    url(r'^full_list_confer', views.full_list_confer, name='full_list_confer'),
    url(r'^spisok_material_conferents/(?P<pk>[0-9]+)/$', views.spisok_material_conferents, name='spisok_material_conferents'),
    url(r'^opisanie_material/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^opisanie_material/(?P<pk>[0-9]+)/otvet_na_coment/$', views.otvet_na_coment, name='otvet_na_coment'),
    #url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
    url(r'^comment_remove/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
    url(r'^section_dob/(?P<pk>[0-9]+)/$', views.section_dob, name='section_dob'),
    url(r'^spisoc_section/(?P<pk>[0-9]+)/$', views.spisoc_section, name='spisoc_section'),

    url(r'^vseorganization/', views.vseorganization, name='vseorganization'),
    url(r'^positionspisok/', views.positionspisok, name='positionspisok'),
    url(r'^uchastie_confer/(?P<id>[0-9]+)/$', views.uchastie_confer, name='uchastie_confer'),
    url(r'^usmyconf/(?P<pk>[0-9]+)/$', views.usmyconf, name='usmyconf'),
    url(r'^smena_status/(?P<pk>[0-9]+)/$', views.smena_status, name='smena_status'),
    url(r'^lock_status/(?P<pk>[0-9]+)/$', views.lock_status, name='lock_status'),
    url(r'^us_conf_full/(?P<pk>[0-9]+)/$', views.us_conf_full, name='us_conf_full'),
    url(r'^zamen_stutus/(?P<pk>[0-9]+)/$', views.zamen_stutus, name='zamen_stutus'),
    url(r'^bloc_user/(?P<pk>[0-9]+)/$', views.bloc_user, name='bloc_user'),
    url(r'^pass_edit/(?P<pk>[0-9]+)/$', views.pass_edit, name='pass_edit'),
    url(r'^new_pass/$', views.new_pass, name='new_pass'),
    url(r'^log_zaregn/(?P<pk>[0-9]+)/$', views.log_zaregn, name='log_zaregn'),
    #url(r'^log_zaregn/$', views.log_zaregn, name='log_zaregn'),
    #url(r'^finish_pass/', views.finish_pass, name='finish_pass'),
    url(r'^otmen_public_material/(?P<id>[0-9]+)/$', views.otmen_public_material, name='otmen_public_material'),
    url(r'^redak_secti/(?P<id>[0-9]+)/$', views.redak_secti, name='redak_secti'),
    url(r'^org_edit/(?P<id>[0-9]+)/$', views.org_edit, name='org_edit'),
    url(r'^posit_edit/(?P<id>[0-9]+)/$', views.posit_edit, name='posit_edit'),
    url(r'^photo_us1/(?P<pk>[0-9]+)/$', views.photo_us1, name='photo_us1'),
    url(r'^ed_us_foto/(?P<pk>[0-9]+)/$', views.ed_us_foto, name='ed_us_foto'),
    url(r'^step_backward/(?P<pk>[0-9]+)/$', views.step_backward, name='step_backward'),
    url(r'^lock_us/(?P<id>[0-9]+)/$', views.lock_us, name='lock_us'),
    url(r'^unlock_us/(?P<id>[0-9]+)/$', views.unlock_us, name='unlock_us'),
    url(r'^otmenpublic/(?P<id>[0-9]+)/$', views.otmenpublic, name='otmenpublic'),
    # url(r'^derevo/$', views.derevo, name='derevo'),
    url(r'^del_sectionfull/(?P<pk>[0-9]+)/$', views.del_sectionfull, name='del_sectionfull'),
	url(r'^vostanov/(?P<id>[0-9]+)/$', views.vostanov, name='vostanov'),
]
