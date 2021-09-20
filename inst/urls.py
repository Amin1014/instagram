from django.conf.urls import include
from django.urls import path,re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django_registration.backends.one_step.views import RegistrationView

urlpatterns=[
    # path('', views.login_redirect, name='login_redirect'),
    # path('accounts/register/', RegistrationView.as_view(success_url='/'),name='django_registration_register'),
    # path('accounts/',include('django_registration.backends.one_step.urls')),

    path('',views.index, name='index'),
    path('',views.profile,name = 'profile'),
    path('',views.timeline,name = 'timeline'),
    re_path('pic/', views.single_pic, name='single_pic'),
    re_path('comment/', views.comment, name='comment'),
    path('profile/', views.profile, name='profile'),
    re_path('single_pic/', views.single_pic, name='single_pic'),
    path('send/', views.send, name='send'),
    path('search/', views.search_results, name='search_results'),
    path('upload/profile', views.upload_profile, name='upload_profile'),
]

if settings.DEBUG:
	urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 