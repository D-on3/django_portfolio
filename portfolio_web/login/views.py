from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import LoginForm

from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.conf import settings


class CustomLoginView(LoginView):
    def form_valid(self, form):
        if settings.RECAPTCHA_SECRET_KEY:
            # Verify reCAPTCHA if the secret key is provided
            from django_recaptcha import verify as recaptcha_verify

            recaptcha_response = self.request.POST.get('g-recaptcha-response')
            recaptcha_result = recaptcha_verify(recaptcha_response)

            if not recaptcha_result['success']:
                messages.error(self.request,
                               'Invalid reCAPTCHA. Please try again.')
                return self.form_invalid(form)

        return super().form_valid(form)


def logout_view(request):
    logout(request)
    return render(request, 'registration/logout.html')