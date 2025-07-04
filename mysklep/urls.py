"""
URL configuration for mysklep project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.apps import apps
from django.contrib import admin
from django.urls import include,path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.sitemaps import views
#from django.contrib.sitemaps.views import sitemap

from apps.sitemaps import base_sitemaps

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),

    # The Django admin is not officially supported; expect breakage.
    # Nonetheless, it's often useful for debugging.

    path('admin/', admin.site.urls),
    path('catalogue/galeria/', include('galeria.urls')),
    path('catalogue/contact/', include('contact.urls')),
    
    path('', include(apps.get_app_config('oscar').urls[0])), 
    
     #path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="django.contrib.sitemaps.views.sitemap",)
 
    # include a basic sitemap
    path('sitemap.xml', views.index,
        {'sitemaps': base_sitemaps}),
    path('sitemap-<slug:section>.xml', views.sitemap,
        {'sitemaps': base_sitemaps},
        name='django.contrib.sitemaps.views.sitemap')
]#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
   #  import debug_toolbar
    
     # Server statics and uploaded media
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
     # Allow error pages to be tested
     # urlpatterns += [
     #     path('403', handler403, {'exception': Exception()}),
     #     path('404', handler404, {'exception': Exception()}),
     #     path('500', handler500),
     #     path('__debug__/', include(debug_toolbar.urls)),
     #     ]
