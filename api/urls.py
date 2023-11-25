from django.urls import path, include

urlpatterns = [
    path('submissions/', include('submissions.urls')),
    path('problems/', include('problems.urls')),
    path('compilers/', include('compilers.urls'))
]
