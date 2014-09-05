__author__ = 'inozemcev'
from django.utils.http import is_safe_url
from django.utils.translation import check_for_language
from django import http
from django.conf import settings

from django.views.generic import TemplateView, RedirectView
from django.core.urlresolvers import reverse



def set_language(request, lang_code):
    """
    Redirect to a given url while setting the chosen language in the
    session or cookie. The url and the language code need to be
    specified in the request parameters.

    Since this view changes how the user will see the rest of the site, it must
    only be accessed as a POST request. If called as a GET request, it will
    redirect to the page in the request (the 'next' parameter) without changing
    any state.
    """
    next = '/'
    response = http.HttpResponseRedirect(next)

    if int(lang_code) == 1:
        lang_code = 'en'
    elif int(lang_code) == 2:
        lang_code = 'ru'
    else:
        lang_code = 'ru'

    if lang_code and check_for_language(lang_code):

       request.session['django_language'] = lang_code

    return response

def get_media_url (request, category_slug, year_id, mounth_id, img):

    response = http.HttpResponseRedirect('/media/products/images/%s/%s/%s' % (year_id, mounth_id, img))
    return response

def temp (request, category_slug, pk, year, mouth, img):
    response = http.HttpResponseRedirect('/media/images/products/%s/%s/%s' % (year, mouth, img))
    return response
