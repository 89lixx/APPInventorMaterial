# -*- coding: utf-8 -*-
import sae
import web
import json
urls = (
    '/', 'Hello',
    '/storeavalue', 'StoreAValue',
    '/getvalue', 'GetValue'
    )
class Hello:
    def GET(self):
        return "Its Webservice for TinyWebDB, please call it through storeavalue or getvalue"

class StoreAValue:
    def GET(self):
        return "ok"
    def POST(self):
        data = web.input()
        aitag = data.tag
        aivalue = data.value
        db = web.database(
                          dbn='mysql',host=sae.const.MYSQL_HOST, 
                          port=int(sae.const.MYSQL_PORT),
                          user=sae.const.MYSQL_USER, 
                          pw=sae.const.MYSQL_PASS,
                          db=sae.const.MYSQL_DB,
                          charset='utf8')
        results = db.select('test',where="tag='"+aitag+"'")
        if len(results)==0:
            db.insert('test',tag=aitag,value=aivalue)
        else:
            db.update('test',where="tag='"+aitag+"'",value=aivalue)
        result = ["STORED",aitag,aivalue]
        return json.dumps(result)
    
class GetValue:
    def GET(self):
        return "ok"
    def POST(self):
        data = web.input()
        aitag = data.tag
        db = web.database(
                          dbn='mysql',host=sae.const.MYSQL_HOST, 
                          port=int(sae.const.MYSQL_PORT),
                          user=sae.const.MYSQL_USER, 
                          pw=sae.const.MYSQL_PASS,
                          db=sae.const.MYSQL_DB,
                          charset='utf8')
        results = db.select('test',where="tag='"+aitag+"'")
        if len(results)==0:
            aivalue-None
        else:
            for a in results:
                aivalue=a.value
                result = ["VALUE",aitag,aivalue]
                return json.dumps(result)

app = web.application(urls, globals()).wsgifunc()
application = sae.create_wsgi_app(app)

