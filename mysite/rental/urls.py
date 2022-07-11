from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    


from .import views
app_name = 'rental'
urlpatterns = [
    path('', views.index, name='index'),
    path('list/',views.alllist,name='alllist'),
    path('detail/<int:id>',views.detail,name='detail'),
    path('deleteroom/<int:id>',views.deleteroom,name='deleteroom'),
    path('myroom/',views.showroom,name='showroom'),
    path('login/',views.login,name='login'),
    path('about/',views.about,name='about'),
    path('loggedIn',views.cust_login1,name="cust_login1"),
    path('register/',views.register,name='register'),
    path('addRoom/',views.addroom,name='addroom'),
    path('contact/',views.contact,name='contact'),
    path('loggedOut', views.logout, name="logout"),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)