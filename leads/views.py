from django.shortcuts import render, reverse, redirect
from django.views import generic
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from .twitter import *

from .forms import UserModelForm
from .models import User, Contact


class LandingPageView(generic.TemplateView):
    template_name = 'home_page.html'


class UserCreateView(generic.CreateView):
    template_name = 'user-create.html'
    form_class = UserModelForm

    def form_valid(self, form):
        user = form.save()
        user.set_password(user.password)
        user.twitter_list = create_list(user)
        user.save()

        # user = authenticate(username=user.username, password=user.password)
        return super(UserCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('home-page')
        # return reverse('home')


class ContactListView(generic.ListView):
    template_name = 'contact-list.html'
    queryset = Contact.objects

    def get_queryset(self, *args, **kwargs):
        qs = super(ContactListView, self).get_queryset(*args, **kwargs)
        qs = qs.filter(user=self.request.user)
        return qs

# class ContactView(generic.DetailView):
#     template_name = 'contact.html'
#     queryset = Contact.objects


class CreateContactView(generic.CreateView):
    template_name = 'contact-create.html'
    model = Contact
    fields = ['name',
              'title',
              'company',
              'phone',
              'email',
              'website',
              'telegram',
              'twitter_personal',
              'twitter_brand',
              'linkedin',
              'birthday',
              'address',
              'status',
              'relationship',
              'notes'
              ]

    def form_valid(self, form):
        form.instance.user = self.request.user
        contact = form.save()
        add_to_list(self.request.user, contact)

        return super(CreateContactView, self).form_valid(form)
        # return redirect(reverse('contact-list'))

    def get_success_url(self):
        return reverse('contact-list')


class ContactDeleteView(generic.DeleteView):
    template_name = 'contact-delete.html'
    model = Contact

    # def form_valid(self, form):
    #     return super(ContactDeleteView, self).form_valid(form)

    def get_success_url(self):
        remove_extra(self.request.user, self.object)
        return reverse('contact-list')


class ContactView(generic.edit.UpdateView):
    template_name = 'contact.html'
    model = Contact
    fields = ['name',
              'title',
              'company',
              'phone',
              'email',
              'website',
              'telegram',
              'twitter_personal',
              'twitter_brand',
              'linkedin',
              'birthday',
              'address',
              'status',
              'relationship',
              'notes'
              ]

    def form_valid(self, form):
        contact = form.save()
        remove_extra(self.request.user)
        add_to_list(self.request.user, contact)

        return super(ContactView, self).form_valid(form)

    def get_success_url(self):
        return reverse('contact-info', kwargs={'pk': self.object.id})
