from django.urls import path,include
from . import views 

 
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers


router = routers.DefaultRouter()
router.register("products",views.ProductsViewSet)
router.register("categpries",views.CategoryViewSet)
router.register("carts",views.CartViewSet)

cart_router=routers.NestedDefaultRouter(router,"carts",lookup="cart")
cart_router.register("items",views.CartItemViewSet,basename="cart-items")
# urlpatterns = router.urls 


urlpatterns = [
    path('', include(router.urls)),
    path('',include(cart_router.urls))
    # path('products',views.api_products ),
    # path('product/<str:pk>',views.api_product),
    # path('categories',views.api_categories ),
    # path('category/<str:pk>',views.api_category),
]