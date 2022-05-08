from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from courses.models import Course
from .forms import ContactForm
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User
from teachers.models import Teacher


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['courses'] = Course.objects.filter(available=True).order_by('-date')[:2]
        contex['total_course'] = Course.objects.filter(available=True).count()
        contex['total_students'] = User.objects.count()
        contex['total_teachers'] = Teacher.objects.count()
        return contex


class AboutView(TemplateView):
    template_name = 'about.html'


class ContactView(SuccessMessageMixin, FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact')
    success_message = 'WE received your request'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

# def courses(request):
#     return render(request, 'courses.html')
