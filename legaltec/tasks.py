# Create your tasks here
from __future__ import absolute_import, unicode_literals
import requests
from celery import shared_task

#from demoapp.models import Widget
import textract
import re
from .models import *
import spacy


nlp = spacy.load("es_core_news_sm")


@shared_task
def add(x, y):
    return x + y

@shared_task
def c_clasifica(self,_, poliza):

    #return clasifica(self,_,poliza)
    return print(type(poliza))


def c_questions(contexto='', pregunta=''):
    #url = 'http://127.0.0.1:5555/model' #
    url = 'http://10.128.0.12:5555/model'
    data = {}
    data['context_raw']=[contexto]
    data['question_raw']=[pregunta]
    t = ''
    try:
        r = requests.post(url, json=data)
        t = r.text
        t=t.replace('[','')
        t=t.replace(']','')
        t=t.replace('"','')
        t=t.split(',')
        

    except: 
        print('Engine is down')

    return t

@shared_task
def procesa(polizas):
    print(type(polizas))
    for pol in polizas:
        a = polizas[pol]
        preguntas = a['quest']
        text = textract.process(a['path'])
        text=text.decode("utf-8")
        text1 = re.sub('\r?\n', ' ', text)
        paginas=text1.split("\f")
        texto = 'INICIO:\n'
        for preg in preguntas:
            for pag in paginas:
                #a = model_qa([pag], [preg.pregunta])
                a = c_questions(pag, preg)
                if a != None:
                    if len(a[0]) > 0:
                        doc=nlp(pag)
                        frase = a[0]
                        for oraciones in doc.sents:
                            val = oraciones.text.find(frase)
                            if val>0:
                                #print( type(oraciones.text),a[0][0])
                                texto = texto +' PREGUNTA: '+ preg+'\n' +' - SEGMENTO: '+a[0] +'\nEXTRACTO: '+oraciones.text +  '\n\n'
        objeto = lead.objects.get(pk=pol)
        objeto.extracto = texto
        print(texto)
        objeto.estado = True
        objeto.save()