"""
Backwards-compatible URLconf for existing django-registration
installs; this allows the standard ``include('registration.urls')`` to
continue working, but that usage is deprecated and will be removed in
a future release.  For new installs, use
``include('registration.backends.model_activation.urls')``.

"""

import warnings
from django.conf.urls import include, url
from registration.forms import RegistrationFormUniqueEmail

from registration.backends.model_activation import urls as model_urls


warnings.warn(
    "include('registration.urls') is deprecated; use "
    "include('registration.backends.model_activation.urls') instead.",
    DeprecationWarning
)


urlpatterns = model_urls.urlpatterns



#urlpatterns = [
#url(r'^register/$', 'registration.views.register', {'form': RegistrationFormUniqueEmail}, name='registration_register'),
#url('', include('registration.urls')),
#]