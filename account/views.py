# Create your views here.

from django.shortcuts import render




#
# class HomeView(LoginRequiredMixin, TemplateView):
#     template_name = 'Home.html'
#     login_url = '/'



def homeview(request):
    return render(request, 'home.html')
def welcomeView(request):
    return render(request, 'welcome.html')