import hashlib
import random

from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime

from message.models import Log, Message
from .serializers import MessageSerializer, LinkSerializer
# Create your views here.


@api_view(['GET', 'POST'])
def save_message(request):
    try:
        if request.method == 'POST':
            message = MessageSerializer(data=request.data)
            if message.is_valid():
                hashline = str.encode('current' +
                                      str(random.randint(0, 4096)) +
                                      datetime.now().strftime('%Y-%m-%d %H:%M:%S.%fZ'))
                identificator = hashlib.sha256(hashline).hexdigest()
                source_ip = str(request.META['REMOTE_ADDR'])
                log = Log()
                log.text = request.__str__()
                log.save()
                message.save(identificator=identificator, source_ip=source_ip)
                if request.is_secure():
                    prefix = 'https://'
                else:
                    prefix = 'http://'
                link = (prefix + request.get_host() +
                        "/message/" + identificator)
                message.save(identificator=identificator, source_ip=source_ip,
                             link=link)
                resplink = message.save()
                respmessage = LinkSerializer(resplink)
                return Response(respmessage.data)
    except Exception as error:
        log = Log()
        log.text = error.__str__()
        log.save()
