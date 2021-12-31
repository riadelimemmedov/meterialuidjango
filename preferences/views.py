from django.shortcuts import render
from django.views.generic import FormView
from .forms import PreferenceModelForm
from django.contrib import messages
from .models import Preference
# Create your views here.

class MyPreference(FormView):
    form_class = PreferenceModelForm
    template_name = 'posts/main.html'

    def get_success_url(self):
        return self.request.path
    
    def form_valid(self,form):
        form.save()
        messages.add_message(self.request,messages.INFO,'Saved Succsessfully')
        return super(MyPreference, self).form_valid(form)
    
    def form_invalid(self, form):
        form.add_error(None,'Ups Something wrong')
        return super(MyPreference, self).form_valid(form)
        
    