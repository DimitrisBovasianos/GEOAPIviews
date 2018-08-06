from django.contrib.gis.geoip import GeoIP


def home(request):
        address = request.META['HTTP_X_FORWARDED_FOR']
        ip = address.split(',')[-1].strip()
        g = GeoIP()
        country = g.country(ip)
        for key,value in country.items():
            if key == "country_code":
                country_code = value
        continent = coun_code(country_code)
        if continent == 'america':
            if request.user_agent.is_touch_capable:
                return render(request,'mobileUS.html')
            else:
                return render(request,'homeUS.html')
        else:
            if request.user_agent.is_touch_capable:
                return render(request,'mobilehome.html')
            else:
                return render(request,'home.html')

def coun_code(code):
    world_dict=[
    ('continent',['countries codes'...]
    for continent,country in world_dict:
        if code in country:
            return continent
