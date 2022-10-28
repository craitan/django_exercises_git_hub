from django.urls import path, include

from games_app.web.views import index, dashboard, create_profile, edit_profile, details_profile, delete_profile, \
    create_game, edit_game, details_game, delete_game

urlpatterns = (
    path('', index, name='index'),
    path('dashboard/', dashboard, name='dashboard'),
    path('game/', include([
        path('create/', create_game, name='create game'),
        path('edit/<int:pk>/', edit_game, name='edit game'),
        path('details/<int:pk>/', details_game, name='details game'),
        path('delete/<int:pk>/', delete_game, name='delete game'),

    ])),
    path('profile/', include([
        path('create/', create_profile, name='create profile'),
        path('edit/', edit_profile, name='edit profile'),
        path('details/', details_profile, name='details profile'),
        path('delete/', delete_profile, name='delete profile'),
    ]))
)
