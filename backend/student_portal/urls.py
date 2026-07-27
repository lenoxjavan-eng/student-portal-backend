from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions


class CookieTokenObtainView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        from django.contrib.auth import authenticate
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, username=email, password=password)
        if not user:
            return Response({'detail': 'Invalid credentials'}, status=400)
        refresh = RefreshToken.for_user(user)
        response = Response({'access': str(refresh.access_token)})
        response.set_cookie(
            'refresh_token', str(refresh),
            httponly=True,
            samesite='Lax',
            secure=not settings.DEBUG,
            max_age=7 * 24 * 3600
        )
        return response


class CookieTokenRefreshView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        refresh_token = request.COOKIES.get('refresh_token')
        if not refresh_token:
            return Response({'detail': 'No refresh token'}, status=401)
        try:
            refresh = RefreshToken(refresh_token)
            return Response({'access': str(refresh.access_token)})
        except Exception:
            return Response({'detail': 'Invalid or expired token'}, status=401)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('accounts.urls')),
    path('api/applications/', include('applications.urls')),
    path('api/programs/', include('programs.urls')),
    path('api/documents/', include('documents.urls')),
    path('api/notifications/', include('notifications.urls')),
    path('api/token/', CookieTokenObtainView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', CookieTokenRefreshView.as_view(), name='token_refresh'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
