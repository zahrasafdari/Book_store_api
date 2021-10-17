from django.urls import path
from tp_book.views import GetAllData, GetFavData, UpdateFavData, PostModelData, PostData, SearchData, DeleteData, \
    allApi, SetData

urlpatterns = [
    path('get-all-data/', GetAllData.as_view()),
    path('all-data/', allApi),
    path('get-fav-data/', GetFavData.as_view()),
    path('update-fav-data/<int:pk>/', UpdateFavData.as_view()),
    path('post-data/', PostData.as_view()),
    path('post-model/', PostModelData.as_view()),
    path('set-data/', SetData),
    path('search/', SearchData.as_view()),
    path('delete/<int:pk>', DeleteData.as_view()),
]
