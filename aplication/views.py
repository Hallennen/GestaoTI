from django.shortcuts import render
from django.views.generic import UpdateView, ListView
from .models import Folga

# Create your views here.
class EditSolicitacao(ListView):
    model = Folga
    template_name = 'editsolicitacao.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['folgas'] = Folga.objects.filter(status_folga='PENDENTE').values()
        return context

