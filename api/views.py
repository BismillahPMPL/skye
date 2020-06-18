# Python library
import re

# Django library
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

# Line bot library
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

# Load local env
from dotenv import load_dotenv
load_dotenv()

# Local libs
from .helper import parse_message
from .controller import controller

# Create your views here.
def status(request):
    return JsonResponse(
        { 'is_running': True },
        content_type = 'json',
        status = 200,
    )

from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

def images_test(request):
    # collect html
    html = urlopen(Request(url='https://animenewsplus.net/2020/06/perbedaan-ova-ona-pv-dan-cm/', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'})).read() 
    # print(html)

    # convert to soup
    soup = BeautifulSoup(html, 'html.parser')
    image_tags = soup.select("img")
    urls = []
    for image_tag in image_tags:
        try:
            url = image_tag['src']
            urls.append(url)
        except KeyError as e:
            pass

    return JsonResponse({
         "type": "image",
         "image_urls": urls,
    })


# Line bot setup
bot = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(settings.LINE_CHANNEL_SECRET)

@csrf_exempt
def api(request):
    if request.method == "POST":
        # get X-Line-Signature header value
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        global domain
        domain = request.META['HTTP_HOST']
        
        # get request body as text
        body = request.body.decode('utf-8')
        # handle webhook body
        try:
            handler.handle(body, signature)
        except InvalidSignatureError:
            return HttpResponseBadRequest()
        return HttpResponse()
    else:
        return HttpResponseBadRequest()

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    data = parse_message(event.message)
    
    if not data["is_valid"]: return
    
    message = controller(data["command"], data["options"])

    bot.reply_message(
        event.reply_token,
        message,
    )