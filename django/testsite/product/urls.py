# from django.conf.urls import static
# from django.conf import settings

from django.urls import path
from .views import ProductListView, ProductDetailView

urlpatterns = [
    path('', ProductListView.as_view(), name='product_page'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product_detail_page'),
    # path('', product_view, name='product_page'),
]

# if settings.DEBUG:
#     # urlpatterns= urlpatterns + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
#     urlpatterns = urlpatterns + static(settings.STATIC_ROOT, document_root=settings.STATIC_ROOT)
