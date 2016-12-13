"""pharma_aid URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^super/', admin.site.urls),

    url(r'^backend/', include('backend.urls', namespace='backend')),

    url(r'^', include('catalog.urls', namespace='catalog')),

    url(r'^cart/', include('cart.urls', namespace='cart')),

    url(r'^order/', include('order.urls', namespace='order')),

    url(r'^my_account/', include('act.urls', namespace='my_account')),

    url(r'^pages/', include('django.contrib.flatpages.urls')),

    url(r'^accounts/', include('allauth.urls')),

    url(r'^misc/', include('misc.urls', namespace='misc')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
