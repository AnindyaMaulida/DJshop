from django.urls import path
from main.views import create_product_flutter, show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id 
from main.views import register
from main.views import login_user #sesuaikan dengan nama fungsi yang dibuat
from main.views import delete_product
from main.views import logout_user, add_amount, reduce_amount, delete_product, edit_product, delete_product, pricelist, get_product_json, add_product_ajax



app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'), 
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
    path('register/', register, name='register'), 
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('add-amount/<int:product_id>/', add_amount, name='add_amount'),  # New URL for adding amount
    path('reduce-amount/<int:product_id>/', reduce_amount, name='reduce_amount'), 
    path('edit-product/<int:id>', edit_product, name='edit_product'),
    path('delete/<int:id>', delete_product, name='delete_product'), # sesuaikan dengan nama fungsi yang dibuat
    path('pricelist.html', pricelist, name='pricelist_html'),
    # path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('get-product/', get_product_json, name='get_product_json'),
    path('create-product-ajax/', add_product_ajax, name='add_product_ajax'),
    path('create-flutter/', create_product_flutter, name='create_product_flutter'),

]