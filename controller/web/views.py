"""
View classes for presenting Deis web pages.
"""

from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from axes.decorators import get_ip_address_from_request
from axes.utils import reset

from api.models import App
from deis import __version__

from .forms import MathCaptchaForm


@login_required
def account(request):
    """Return the user's account web page."""
    return render(request, 'web/account.html', {
        'page': 'account',
    })


@login_required
def dashboard(request):
    """Return the user's dashboard web page."""
    apps = App.objects.filter(owner=request.user)
    return render(request, 'web/dashboard.html', {
        'page': 'dashboard',
        'apps': apps,
        'version': __version__,
    })


@login_required
def apps(request):
    """Return the user's apps web page."""
    apps = App.objects.filter(owner=request.user)
    return render(request, 'web/apps.html', {
        'page': 'apps',
        'apps': apps,
    })


@login_required
def support(request):
    """Return the support ticket system home page."""
    return render(request, 'web/support.html', {
        'page': 'support',
    })


def locked_out(request):
    """Force a captcha when a user is locked out."""
    if request.POST:
        form = MathCaptchaForm(request.POST)
        if form.is_valid():
            ip = get_ip_address_from_request(request)
            reset(ip=ip)
            return HttpResponseRedirect(reverse("admin:index"))
    else:
        form = MathCaptchaForm()

    return render_to_response('web/locked_out.html', dict(form=form), context_instance=RequestContext(request))
