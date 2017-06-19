from django.conf.urls import url , include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from registration.forms import RegistrationFormUniqueEmail
from registration.backends.default.views import RegistrationView
from rest_framework.urlpatterns import format_suffix_patterns
from attendanceMgnt import views


admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
 	url(r'^users/', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),

    url(r'^', include('attendanceMgnt.urls')),
    url(r'^accounts/register/$',RegistrationView.as_view(form_class=RegistrationFormUniqueEmail),
        name='registration_register'),
    url(r'^accounts/', include('registration.backends.default.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = format_suffix_patterns(urlpatterns)