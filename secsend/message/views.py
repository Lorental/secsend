import hashlib
import random
from django.shortcuts import render, get_object_or_404
from datetime import datetime
from .models import Message, Log
from .forms import MessageForm

# Create your views here.


def show_index(request):
    try:
        template_name = 'message/index.html'
        form = MessageForm
        context = {'form': form}
        return render(request, template_name, context)
    except Exception as error:
        log = Log()
        log.text = error.__str__()
        log.save()


def save_message(request):
    try:
        messageform = MessageForm(request.POST)
        if messageform.is_valid():
            message = messageform.save(commit=False)
            hashline = str.encode('current' + str(random.randint(0, 4096)) +
                                  datetime.now().strftime('%Y-%m-%d %H:%M:%S.%fZ'))
            message.identificator = hashlib.sha256(hashline).hexdigest()
            message.source_ip = str(request.META['REMOTE_ADDR'])
            message.save()
            if request.is_secure():
                prefix = 'https://'
            else:
                prefix = 'http://'
            message.identificator = (prefix + request.get_host() + "/message/" +
                                     message.identificator)
        context = {'identificator': message.identificator}
        template_name = 'message/link_page.html'
        return render(request, template_name, context)
    except Exception as error:
        log = Log()
        log.text = error.__str__()
        log.save()


def show_message(request, identificator):
    try:
        template_name = 'message/show_message.html'
        # message = Message.objects.get(identficator=identificator)
        message = get_object_or_404(Message, identificator=identificator)
        context = {'message': message}
        message.delete()
        return render(request, template_name, context)
    except Exception as error:
        log = Log()
        log.text = error.__str__()
        log.save()
