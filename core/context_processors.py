from area.models import Area


def area_links(request):
    areas = Area.objects.all().values_list('nombre', flat=True).distinct()
    return dict(areas=areas)
