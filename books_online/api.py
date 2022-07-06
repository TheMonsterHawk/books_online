from rest_framework.routers import DefaultRouter 
from users.views import UserViewSet 
from pub_auth.views import PublisherViewSet, AuthorViewSet

router = DefaultRouter() 
router.register('users', UserViewSet) 
router.register('publisher', PublisherViewSet) 
router.register('author', AuthorViewSet) 
