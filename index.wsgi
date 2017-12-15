#coding: UTF-8
import os

import sae
import web
from service.translateInter import TranslateInterface

urls = (
'/weixin','TranslateInterface'
)

app = web.application(urls, globals()).wsgifunc()
application = sae.create_wsgi_app(app)
