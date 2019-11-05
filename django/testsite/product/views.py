from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView
from .models import Product


class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = 'product/product_list.html'
    # def get_queryset(self, *args, **kwargs):
    #     request =self.request
    #     return Product.objects.all()

    # def get_context_data(self, *args, **kwargs):
    #     context = super(ProductView, self).get_context_data(*args, **kwargs)
    #     context['a'] = Product.objects.all()
    #     return context


# def product_view(request):
#     render(request, 'product/product_list.html', {})


class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = 'product/product_detail.html'
    # def get_queryset(self, *args, **kwargs):
    #     request =self.request
    #     return Product.objects.all()


    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        context['obj'] = Product.objects.all()
        # context['ob'] = Product.objects.all().filter(image=True)
        # print(context)
        return context
