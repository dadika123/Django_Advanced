from django.urls import path
from django.views.decorators.cache import cache_page
import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.products, name='index'),
    path('category/<int:category_id>/', cache_page(3600)(mainapp.products), name='category'),
    path('page/<int:page_num>/', mainapp.products, name='page'),
]
