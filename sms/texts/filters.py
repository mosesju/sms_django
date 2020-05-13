import django_filters

from .models import Text

class TextFilter(django_filters.FilterSet):
    class Meta:
        model = Text
        fields = '__all__'