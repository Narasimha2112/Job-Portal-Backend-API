import django_filters
from .models import Job

class JobFilter(django_filters.FilterSet):
    min_salary = django_filters.CharFilter(method='filter_salary_min')
    
    class Meta:
        model = Job
        fields = ['location']
    
    def filter_salary_min(self, queryset, name, value):
        return queryset.filter(salary_range__icontains=value)