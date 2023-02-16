from django.urls import path, include
from rest_framework.routers import DefaultRouter

from applications.product.views import ProductItemFileViewSet, ProductItemViewSet, ProductViewSet, ArchiveApiView

router = DefaultRouter()

router.register('archive', ArchiveApiView)
router.register('course_item', ProductItemViewSet)
router.register('course_item_file', ProductItemFileViewSet)
router.register('', ProductViewSet)

urlpatterns = [
    path('favourites/', ProductViewSet.as_view({'get': 'get_favourites'})),
    path('<int:pk>/favourite/', ProductViewSet.as_view({'post':'favourite'})),
    path('<int:pk>/rating/', ProductViewSet.as_view({'post': 'rating'})),
    path('<int:pk>/like/', ProductViewSet.as_view({'post': 'like'})),
    path('<int:pk>/comment/', ProductViewSet.as_view({'post': 'add_comment'})),
    path('comment/<int:pk>/', ProductViewSet.as_view({'delete': 'delete_comment', 'put': 'update_comment'})),
    path('comment/<int:pk>/like/', ProductViewSet.as_view({'post':'like_comment'})),
    path('', include(router.urls)),  
]