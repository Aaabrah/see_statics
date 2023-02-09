from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView, View
from .models import ProductModel


class MainView(TemplateView):
    template_name = 'index.html'


class SearchView(ListView):
    template_name = 'index.html'
    model = ProductModel
    # paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = ProductModel.objects.filter(sku__isnull=False)
        return context

    def get_queryset(self):
        qs = ProductModel.objects.filter(sku__isnull=False)
        q = self.request.GET.get('q')
        if q:
            print('123123')
            qs = get_object_or_404(ProductModel, sku=q)

        return qs

