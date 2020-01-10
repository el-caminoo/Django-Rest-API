from django.conf.urls import url
from .views import VisitorView, VisitorCreate, VisitorUpdate

urlpatterns = [
    url(r'^get/$', VisitorView.as_view()),
    url(r'^create/$', VisitorCreate.as_view()),
    url(r'^validate/(?P<pk>[-\w]+)/$', VisitorUpdate.as_view())
]