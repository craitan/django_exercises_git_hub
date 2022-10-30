from django.urls import path, include

from mid_exam.car_app.views import add_profile, catalogue_page, create_car, edit_car, details_car, delete_car, create_profile, \
    edit_profile, \
    details_profile, delete_profile

urlpatterns = (
    path('', add_profile, name='index'),
    path('catalog/', catalogue_page, name='catalogue'),
    path('car/', include([
        path('create/', create_car, name='create car'),
        path('<int:pk>/edit/', edit_car, name='edit car'),
        path('<int:pk>/details/', details_car, name='details car'),
        path('<int:pk>/delete/', delete_car, name='delete car'),

    ])),
    path('profile/', include([
        path('create/', create_profile, name='create profile'),
        path('edit/', edit_profile, name='edit profile'),
        path('details/', details_profile, name='details profile'),
        path('delete/', delete_profile, name='delete profile')

    ]))
)
