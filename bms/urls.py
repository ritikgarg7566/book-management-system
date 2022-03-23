from django.urls import path
from bms import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
        path("front",views.front),
        path("signup",views.signup),
        path("signin",views.signin),
        path("addsign",views.addsignupdetails),
        path("login",views.signinrequest),
        path("add_book",views.addbook),
        path("add2_book",views.book),
        path("search2_book",views.searching),
        path("edit_book",views.edit),
        path("editbook",views.edit_save),
        path("delete_book",views.delete),
        path("signout2",views.signout),


]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
