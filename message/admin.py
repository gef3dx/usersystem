from django.contrib import admin

from message.models import ThreadModel, MessageModel

admin.site.register(ThreadModel)
admin.site.register(MessageModel)

