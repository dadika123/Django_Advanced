from django.urls import path

from basketapp.views import basket_add, basket_edit, basket_delete

app_name = "basketapp"

urlpatterns = [
    path('basket-add/<int:product_id>/', basket_add, name='basket_add'),
    path('basket-remove/<int:id>/', basket_delete, name='basket_delete'),
    path('edit/<int:id>/<int:quantity>/', basket_edit, name='basket_edit'),
]
