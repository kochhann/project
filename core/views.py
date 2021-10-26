from django.urls import reverse_lazy
from django.views.generic import FormView
from .models import Service, Employee
from .forms import ContactForm
from django.contrib import messages


class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContactForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['services'] = Service.objects.all()
        context['employees'] = Employee.objects.all()
        return context

    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, 'Email enviado com sucesso')
        return super(IndexView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Email não enviado. Tente novamente mais tarde.')
        return super(IndexView, self).form_valid(form, *args, **kwargs)
