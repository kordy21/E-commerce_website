from django.urls import path,include
from . import views 

 
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("products",views.ProductsViewSet)
router.register("categpries",views.CategoryViewSet)


# urlpatterns = router.urls 


urlpatterns = [
    path('', include(router.urls))
    # path('products',views.api_products ),
    # path('product/<str:pk>',views.api_product),
    # path('categories',views.api_categories ),
    # path('category/<str:pk>',views.api_category),
]