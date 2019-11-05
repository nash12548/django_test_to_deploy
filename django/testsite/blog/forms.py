from django import forms
from .models import BlogPage


class ContactForms(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your name'
            }))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your email',
            }))
    contact = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'your massage',
            }))

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not '@gmail.com' in email:
            raise forms.ValidationError('Email most @gmail.com')
        return email


class BlogForm(forms.Form):
    title = forms.CharField(max_length=300)
    slug = forms.SlugField()
    text = forms.CharField(widget=forms.Textarea)


class BlogModelForm(forms.ModelForm):
    class Meta:
        model = BlogPage
        fields = ['title', 'slug', 'text']

    def clean_title(self):
        title = self.cleaned_data.get('title')
        instance = self.instance
        qs = BlogPage.objects.filter(title__iexact=title)
        # print(qs,'////',instance)
        if instance is not None:
            qs = qs.exclude(pk=instance.pk)
            # print('|||',qs,'|||')
        if qs.exists():
            raise forms.ValidationError('This title is exists please choose another one')
        return title
