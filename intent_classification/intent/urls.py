from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import IntentView


urlpatterns = [
    path('predict/', IntentView.as_view()),
    # path('all/', TravelView.as_view()),
    # path('<int:id>/', TravelView.as_view()),
    # path('upload/', FileUploadView.as_view(), name="file-upload"),
    # path('view/(?P<destination>\w{0,50})/$', TravelView.as_view()),
    # path('view/(?P<distance>\w{0,50})/$', TravelView.as_view()),
    # path('view/(?P<budget>\w{0,50})/$', TravelView.as_view()),
    # path('view/(?P<mode>\w{0,50})/$', TravelView.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)