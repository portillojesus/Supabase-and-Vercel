
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponseRedirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),  # Incluye las URLs de la app "blog"
    path('', lambda request: HttpResponseRedirect('/blog/')),  # Redirige la raíz a /blog/
]
