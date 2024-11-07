from django.urls import path
from . import views


urlpatterns=[
        path('',views.shop_login),
        path('shop_logout',views.shop_logout),
        # ------------shop------------
        path('shop_home',views.shop_home),
        path('add_plants',views.add_plants),
        path('edit_plants/<pid>',views.edit_plants),
        path('delete_plants/<pid>',views.delete_plants),

        # --------------user----------------

]