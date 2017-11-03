# Create your views here.
import uuid

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.utils.encoding import force_text, force_bytes
from django.utils.html import strip_tags
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.views.generic import FormView, RedirectView
from django.core.mail import EmailMessage, EmailMultiAlternatives
from forms.forms import SignUpForm, EditProfileForm


class LoginView(FormView):
    success_url = '/home/'
    form_class = AuthenticationForm
    template_name = 'home.html'

    def dispatch(self, request, *args, **kwargs):
        request.session.set_test_cookie()
        return super(LoginView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(LoginView, self).form_valid(form)


def account_activation_sent(request):
    return render(request, 'account_activation_sent.html')


def account_activation_invalid(request):
    return render(request, 'account_activation_invalid.html')


def welcomeView(request):
    return render(request, 'welcome.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            print("HEY")
            form.save()
            firstname = form.cleaned_data.get('first_name')
            email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            sendMail(user, request.build_absolute_uri('/activation/' + str(uuid.uuid4)))

            return redirect('account:welcome')
        else:
            return render(request, 'signup.html', {'form': form})
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def sendMail(new_user, activation_link):
    subject = "Activation Key"
    from_email = 'webelopertest@gmail.com'
    to = new_user.email
    context = {'new_user': new_user, 'url': activation_link}
    html_message = render_to_string('account_activation_email.html', context)
    text_content = strip_tags(html_message)
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_message, "text/html")
    msg.send()


# def signup(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.is_active = False
#             user.save()
#             current_site = get_current_site(request)
#             message = render_to_string('account_activation_email.html', {
#                 'user': user,
#                 'domain': current_site.domain,
#                 'uid': urlsafe_base64_encode(force_bytes(user.pk)),
#                 'token': account_activation_token.make_token(user),
#             })
#             mail_subject = 'Activate your blog account.'
#             to_email = form.cleaned_data.get('email')
#             email = EmailMessage(mail_subject, message, to=[to_email])
#             email.send()
#             return HttpResponse('Please confirm your email address to complete the registration')
#
#     else:
#         form = SignUpForm()
#
#     return render(request, 'signup.html', {'form': form})




class LoginView(FormView):
    success_url = '/home/'
    form_class = AuthenticationForm
    template_name = 'login.html'

    def dispatch(self, request, *args, **kwargs):
        request.session.set_test_cookie()
        return super(LoginView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())

        return super(LoginView, self).form_valid(form)


class LogoutView(RedirectView):
    url = '/'

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)


def profileView(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'profile.html', {'user': user,
                                            })


# def editProfile(request):
#     return render(request, 'editprofile.html')


def editProfile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            raw_password2 = form.cleaned_data.get('password2')
            print(raw_password)
            print(raw_password2)
            current_user = User.objects.get(username=username)
            current_user.first_name = first_name
            current_user.email = email
            if raw_password == raw_password2 and raw_password:
                current_user.set_password(raw_password)
            current_user.save()
            login(request, current_user)
            return redirect('cafe:home')
        else:
            return render(request, 'editprofile.html', {'form': form})
    else:
        form = EditProfileForm()
    return render(request, 'editprofile.html', {'form': form})
