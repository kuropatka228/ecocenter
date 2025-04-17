from .models import SiteSetting

def site_settings(request):
    settings = SiteSetting.objects.first()
    return {'settings': settings}