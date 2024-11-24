from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings

from django.views.generic import *
from .forms import ContactMessageForm
from blog.models import Blog


class HomePageView(TemplateView):
    template_name = 'home.html'

    # in this part, we can access to Values of app.models on home page
    def get_context_data(self, **kwargs):
        # in this part, we can access to all blogs by id
        context = super().get_context_data(**kwargs)
        context['all_blogs'] = Blog.objects.all().order_by('-id')
        # in this part, we can access to 3 latest post in blogs by id
        latest_blogs = Blog.objects.all().order_by('-id')[:3][::-1]
        context['latest_blogs'] = latest_blogs
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['form'] = ContactMessageForm()
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            contact_message = form.save()

            # ارسال ایمیل
            send_mail(
                'New Contact Message',
                f"""Message from: {contact_message.name}\n"""
                f"""({contact_message.email}):\n\n"""
                f""" {contact_message.message}""",
                settings.DEFAULT_FROM_EMAIL,
                [settings.DEFAULT_FROM_EMAIL],
                fail_silently=False,
            )
            return redirect('success_page')

        # اگر فرم معتبر نبود، دوباره با داده‌های فرم و بلاگ‌ها نمایش داده شود
        context = self.get_context_data(**kwargs)
        context['form'] = form
        return self.render_to_response(context)


class SuccessPageView(TemplateView):
    template_name = 'contact_message.html'


def my_view(request):
    return render(request, '_base.html')


def maintenance_page(request):
    return render(request, '503.html')


# def custom_404_view(request, exception):
#     return render(request, '404.html', status=404)
def custom_404_view(request):
    return render(request, '404.html', status=404)