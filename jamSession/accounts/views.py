from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.http import Http404, HttpResponseRedirect
from django.views import generic, View
from django.db.models import Q
from accounts.models import Profile
from . import forms
from .models import User, Profile, ThreadModel, MessageModel
from .forms import ProfileUpdateForm, ThreadForm, MessageForm
from .filters import ProfileFilter

from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.

@login_required
def profile(request):
    if request.method == 'POST':

        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been updated!')

    else:
        form = ProfileUpdateForm(instance=request.user.profile)


    context = {'form': form}
    template_name="accounts/profile.html"

    return render(request, template_name, context)


class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("login")
    template_name = "accounts/signup.html"


class AddEndorsement(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        user = Profile.objects.get(pk=pk)

        is_endorsed = False

        # check all endorsements and if already endorsed, set flag
        for endorsement in user.endorsements.all():
            if endorsement == request.user:
                is_endorsed = True
                break

        # If user hasn't endorsed yet, add endorsement
        if not is_endorsed:
            user.endorsements.add(request.user)

        # If user has endorsed, removed endorsement
        if is_endorsed:
            user.endorsements.remove(request.user)


        # Redirect to the previous page
        next = request.POST.get('next', '/posts/by/{}'.format(user.user))
        return HttpResponseRedirect(next)


class AccountList(generic.ListView):

    model = Profile
    template_name = 'profile_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ProfileFilter(self.request.GET, queryset=self.get_queryset())
        return context
    

class ListThreads(View):
    def get(self, request, *args, **kwargs):
        threads = ThreadModel.objects.filter(Q(user=request.user) | Q(receiver=request.user))

        context = {
            'threads': threads
        }

        return render(request, 'accounts/inbox.html', context)


class CreateThread(View):
    def get(self, request, *args, **kwargs):
        form = ThreadForm()

        context = {
            'form': form
        }

        return render(request, 'accounts/create_thread.html', context)

    def post(self, request, *args, **kwargs):
        form = ThreadForm(request.POST)

        username = request.POST.get('username')

        try:
            receiver = User.objects.get(username=username)
            if ThreadModel.objects.filter(user=request.user, receiver=receiver).exists():
                thread = ThreadModel.objects.filter(user=request.user, receiver=receiver)[0]
                return redirect('accounts:thread', pk=thread.pk)
            elif ThreadModel.objects.filter(user=receiver, receiver=request.user).exists():
                thread = ThreadModel.objects.filter(user=receiver, receiver=request.user)[0]
                return redirect('accounts:thread', pk=thread.pk)

            if form.is_valid():
                thread = ThreadModel(
                    user=request.user,
                    receiver=receiver
                )
                thread.save()

                return redirect('accounts:thread', pk=thread.pk)
        except:
            return redirect('accounts:create-thread')


class CreateThreadFormless(View):

    def post(self, request, pk, *args, **kwargs):
        user = User.objects.get(pk=pk)

        if ThreadModel.objects.filter(user=request.user, receiver=user).exists():
            thread = ThreadModel.objects.filter(user=request.user, receiver=user)[0]
            return redirect('accounts:thread', pk=thread.pk)
        elif ThreadModel.objects.filter(user=request.user, receiver=user).exists():
            thread = ThreadModel.objects.filter(user=user, receiver=request.user)[0]
            return redirect('accounts:thread', pk=thread.pk)

        else:
            thread = ThreadModel(
                user=request.user,
                receiver=user
            )
            thread.save()

            return redirect('accounts:thread', pk=thread.pk)


class ThreadView(View):
    def get(self, request, pk, *args, **kwargs):
        form = MessageForm()
        thread = ThreadModel.objects.get(pk=pk)
        message_list = MessageModel.objects.filter(thread__pk__contains=pk)
        context = {
            'thread': thread,
            'form': form,
            'message_list': message_list
        }

        return render(request, 'accounts/thread.html', context)


class CreateMessage(View):
    def post(self, request, pk, *args, **kwargs):
        thread = ThreadModel.objects.get(pk=pk)
        if thread.receiver == request.user:
            receiver = thread.user
        else:
            receiver = thread.receiver

        message = MessageModel(
            thread=thread,
            sender_user=request.user,
            receiver_user=receiver,
            body=request.POST.get('message')
        )

        message.save()
        return redirect('accounts:thread', pk=pk)