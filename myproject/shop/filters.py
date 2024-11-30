from django_filters import FilterSet
from .models import *

class CatalogFilter(FilterSet):
    model = Catalog
    fields = {
        'catalogImage' ['exact']
    }