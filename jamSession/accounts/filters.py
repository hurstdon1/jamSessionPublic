import django_filters
from pyzipcode import ZipCodeDatabase
from django.db.models import Q

import operator


from .models import *

class ProfileFilter(django_filters.FilterSet):

    location_zip = django_filters.NumberFilter(label='location zip', method="filter_by_distance")

    class Meta:
        model = Profile

        fields = ['instruments', 'singer', 'music_production_experience', 'experience_level', 'location_zip']

    def filter_by_distance(self, queryset, location_zip, value):

        zcdb = ZipCodeDatabase()

        nearby_zips = []

        if location_zip is not None:

            for z in zcdb.get_zipcodes_around_radius(int(value), 25):
                nearby_zips.append(z.zip)
            
            query = Q()

            for z in nearby_zips:
                query = query | Q(location_zip=z)

            return queryset.filter(query)
