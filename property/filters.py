from urllib import parse


class Filters():

    def validate_filters(params):
        year_qs   = parse.parse_qs(params).get('year')
        city_qs   = parse.parse_qs(params).get('city')
        status_qs = parse.parse_qs(params).get('status')
        
        if year_qs is not None:
            year_qs   = year_qs[0]
                   
        if city_qs is not None:
            city_qs   = city_qs[0]
        
        if status_qs is not None:
            status_qs = status_qs[0]

        return year_qs,city_qs,status_qs