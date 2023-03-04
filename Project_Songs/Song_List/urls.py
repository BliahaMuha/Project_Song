from django.urls import path, include
from rest_framework import routers, permissions
from .views import ArtistViewSet, AlbumViewSet, SongViewSet, AlbumListByArtistAPIView, ArtistListByArtistAPIView, \
    SongListByArtistAPIView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = routers.DefaultRouter()
router.register(r'artists', ArtistViewSet)
router.register(r'albums', AlbumViewSet)
router.register(r'songs', SongViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="Music Catalog API",
        default_version='v1',
        description="API for managing music catalog",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@musiccatalog.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('', include(router.urls)),
    path('songs/<str:artist_name>/', SongListByArtistAPIView.as_view(), name='song_list_by_artist'),
    path('albums/<int:id>/', AlbumListByArtistAPIView.as_view(), name='album-list-by-artist'),
    path('artists/<int:id>/', ArtistListByArtistAPIView.as_view(), name='artist_list_by_artist'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]