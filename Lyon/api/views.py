from django_filters import rest_framework as filters
from rest_framework import viewsets
from api.serializer import UserSerializer
from .models import User


# FilterSetを継承したフィルタセット(設定クラス)を作る
class UserFilter(filters.FilterSet):
    # フィルタの定義
    name = filters.CharFilter(field_name="name")


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # フィルタセットの指定
    filter_class = UserFilter
