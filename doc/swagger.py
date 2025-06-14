from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
   openapi.Info(
    title="Django Restful API",
    default_version='v1',
    description="Description",
    terms_of_service="https://www.google.com/policies/terms/",
    contact=openapi.Contact(email="xuanthuydam.06072000@gmail.com"),
    license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)