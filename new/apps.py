from django.apps import AppConfig


class NewConfig(AppConfig):
    name = 'new' # Здесь указываем исходное имя приложения
    verbose_name = 'Конференции, материалы, справочники, заявки'  # А здесь, имя которое необходимо отобразить в админке
