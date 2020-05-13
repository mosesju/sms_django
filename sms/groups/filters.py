import django_filters
from django_filters import CharFilter

from .models import Group

class GroupFilter(django_filters.FilterSet):
    group_name = CharFilter(field_name='group_name', lookup_expr='icontains')
    class Meta:
        model = Group
        fields = '__all__'
        exclude = ['account', 'description']