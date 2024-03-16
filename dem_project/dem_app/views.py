from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import UserForm, ProfileForm
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.models import User
from dem_app.models import Profile

# Create your views here.
def home(request):
    context = {}
    return render(request, 'dem_app/home.html', context)

def profile(request):
    return 

from django.contrib import messages

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'dem_app/profile.html'
    # def get(self, request, username):
    #     # Your logic to fetch user profile based on the username
    #     return render(request, 'profile.html', {'username': username})
    
class ProfileUpdateView(LoginRequiredMixin, TemplateView):
    user_form = UserForm
    profile_form = ProfileForm
    template_name = 'dem_app/profile-update.html'

    def post(self, request):

        post_data = request.POST or None
        file_data = request.FILES or None

        user_form = UserForm(post_data, instance=request.user)
        profile_form = ProfileForm(post_data, file_data, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.error(request, 'Your profile is updated successfully!')
            return HttpResponseRedirect(reverse_lazy('profile'))

        context = self.get_context_data(
                                        user_form=user_form,
                                        profile_form=profile_form
                                    )

        return self.render_to_response(context)     

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)