from django.shortcuts import render, redirect
from .models import ThreadModel, MessageModel
from django.db.models import Q
from users.models import CustomUser as User
from .forms import ThreadForm, MessageForm

def ListThread(request):
    if request.user.is_authenticated:
        thread = ThreadModel.objects.filter(Q(user=request.user) | Q(receiver = request.user))
        context = {
            'threads': thread
        }
        return render(request, 'message/inbox.html', context)
    else:
        return redirect('home')

def CreateThread(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = ThreadForm(request.POST)
            username = request.POST.get('username')

            try:
                receiver = User.objects.get(username=username)
                if ThreadModel.objects.filter(user=request.user, receiver=receiver).exists():
                    thread = ThreadModel.objects.filter(user=request.user, receiver=receiver)[0]
                    return redirect('thread', pk=thread.pk)
                elif ThreadModel.objects.filter(user=receiver, receiver=request.user).exists():
                    thread = ThreadModel.objects.filter(user=receiver, receiver=request.user)[0]
                    return redirect('thread', pk=thread.pk)

                if form.is_valid():
                    thread = ThreadModel(
                        user=request.user,
                        receiver=receiver
                    )
                    thread.save()

                    return redirect('thread', pk=thread.pk)
            except:
                return redirect('create-thread')
        else:
            form = ThreadForm()

            context = {
                'form': form
            }

            return render(request, 'message/create_thread.html', context)
    else:
        return redirect('home')

def ThreadView(request, pk):
    if request.user.is_authenticated:
        form = MessageForm()
        thread = ThreadModel.objects.get(pk=pk)
        message_list = MessageModel.objects.filter(thread__pk__contains=pk)
        context = {
            'thread': thread,
            'form': form,
            'message_list': message_list
        }
        return render(request, 'message/thread.html', context)
    else:
        return redirect('home')

def CreateMessage(request, pk):
    if request.user.is_authenticated:
        if request.method == "POST":
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
            return redirect('thread', pk=pk)
    else:
        return redirect('home')


