from django.conf.urls import url

from pets import views

urlpatterns = [
    url(r"^cats/(?P<pk>\d+)/$", views.CatDetailView.as_view()),
    url(r"^dogs/(?P<pk>\w+)/$", views.DogDetailView.as_view()),

]