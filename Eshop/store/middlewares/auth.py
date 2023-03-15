from django.shortcuts import redirect

def auth_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        print(request.session.get('customer'))
        returnUrl = request.META['PATH_INFO']                   #Return Url function
        print(request.META['PATH_INFO'])
        if not request.session.get('customer'):
           return redirect(f'login?return_url={returnUrl}')   #If customer login or not

        response = get_response(request)
        return response

    return middleware