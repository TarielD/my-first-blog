from django.http import HttpResponse


def cors_middleware(get_response):
    def middleware(request):
        response: HttpResponse = get_response(request)
        response["Access-Control-Allow-Origin"] = "*"
        return response

    return middleware
