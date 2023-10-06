from django.shortcuts import render
from django.views.generic import FormView
from .models import Customer
from django.views.generic.edit import CreateView
from django.views.generic.base import View
from django.http import HttpResponse
from django.urls import reverse_lazy


class CustomerView(CreateView):
    model = Customer
    fields = []
    template_name ='basket/customer_form.html'
    success_url = reverse_lazy('about-view')

    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        return super(CustomerView, self).form_valid(form)

class AboutView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello!')
