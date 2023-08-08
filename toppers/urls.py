from django.urls import path
# from .views import BirdAddView, BirdListView

from . import views
app_name='toppers'

urlpatterns = [
path('', views.index, name='index'),

]
