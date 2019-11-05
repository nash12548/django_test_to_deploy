from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import ContactForms
from django.contrib.auth import authenticate
from .models import BlogPage
from .forms import BlogForm, BlogModelForm
from django.contrib.admin.views.decorators import staff_member_required


# from django.http import HttpResponse


# Create your views here.

def home_page(request):
    context = {
        'title': 'Home page',
        'text': 'Hello',
    }
    if request.user.is_authenticated:
        context['vip'] = 'Your is a VIP member'

    return render(request, 'blog/index.html', context)


def about_page(request):
    context = {
        'title': 'About page',
        'text': '',
    }

    return render(request, 'blog/index.html', context)


def contact_page(request):
    contact_form = ContactForms(request.POST or None)
    context = {
        'title': 'Contact page',
        'text': 'hi',
        'forms': contact_form

    }
    # print('====================================================')
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    print('====================================================')
    if request.method == 'POST':
        pass
        # print(request.POST)
        # print(request.POST.get('name'))
        # print(request.POST.get('email'))
        # print(request.POST.get('contact'))
    return render(request, 'blog/contact.html', context)


def blog_list_view(request):
    queryset = BlogPage.objects.all()
    template_name = 'blog/list.html'
    context = {
        'title': 'List Page',
        'queryset': queryset,
        'range': range(2)

    }
    return render(request, template_name, context)


@staff_member_required
def blog_create_view(request):
    form = BlogModelForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        form = BlogModelForm()
    template_name = 'blog/create.html'
    context = {
        'title': 'Create Page',
        'form': form,
    }
    return render(request, template_name, context)


@staff_member_required
def blog_update_view(request, slug):
    queryset = get_object_or_404(BlogPage, slug=slug)
    form = BlogModelForm(request.POST or None, instance=queryset)
    if form.is_valid():
        form.save()
        return redirect('../')
    template_name = 'blog/update.html'
    context = {
        'title': f'update {queryset.title}',
        'form': form,
        'queryset': queryset,
    }
    return render(request, template_name, context)


@staff_member_required
def blog_delete_view(request, slug):
    queryset = get_object_or_404(BlogPage, slug=slug)
    if request.method == 'POST':
        queryset.delete()
        return redirect('../../')
    template_name = 'blog/delete.html'
    context = {
        'title': 'Delete Page',
        'queryset': queryset,
    }
    return render(request, template_name, context)


def blog_detail_view(request, slug):
    queryset = get_object_or_404(BlogPage, slug=slug)
    template_name = 'blog/detail.html'
    context = {
        'title': 'Detail Page',
        'queryset': queryset,
    }
    return render(request, template_name, context)

def test_page(request):
    template_name = 'blog/test.html'
    return render(request, template_name ,{})

def test2_page(request):
    template_name = 'blog/test2.html'
    return render(request, template_name ,{})

