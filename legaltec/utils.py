from deeppavlov import build_model, configs
import textract
import re
import spacy
import requests
from .models import *
nlp = spacy.load("es_core_news_sm")


#model_qa = build_model(configs.squad.squad_bert,  download=False)

def questions(contexto='', pregunta=''):
    url = 'http://127.0.0.1:5555/model'
    data = {}
    data['context_raw']=[contexto]
    data['question_raw']=[pregunta]
    try:
        r = requests.post(url, json=data)
        t = r.text
        t=t.replace('[','')
        t=t.replace(']','')
        t=t.replace('"','')
        t=t.split(',')
        return t

    except: 
        print('Engine is down')

def clasifica(self,_,  poliza='POLIZA ALLIANZ.pdf',):
    #preguntas = Preguntas.objects.all()
    #pregunta = "puede designar?"
    for pol in poliza:
        #text = textract.process(pol.poliza.path, method='pdfminer')
        #print(pol.aseguradora)
        preguntas = Preguntas.objects.filter(aseguradora=pol.aseguradora)
        text = textract.process(pol.poliza.path)
        text=text.decode("utf-8")
        text1 = re.sub('\r?\n', ' ', text)
        paginas=text1.split("\f")
        texto = 'INICIO:\n'
        for preg in preguntas:
            for pag in paginas:
                #a = model_qa([pag], [preg.pregunta])
                a = questions(pag, preg.pregunta)

                if len(a[0]) > 0:
                    doc=nlp(pag)
                    frase = a[0]
                    for oraciones in doc.sents:
                        val = oraciones.text.find(frase)
                        if val>0:
                            #print( type(oraciones.text),a[0][0])
                            texto = texto +' PREGUNTA: '+ preg.pregunta+'\n' +' - SEGMENTO: '+a[0] +'\nEXTRACTO: '+oraciones.text +  '\n\n'
        pol.extracto = texto
        print(texto)
        pol.estado = True
        pol.save()


'''
def clasifica(self,_,  poliza='POLIZA ALLIANZ.pdf',):
    preguntas = Preguntas.objects.all()
    for pol in poliza:
        #print( '\npoliza', pol.poliza.path)
        #print(dir(pol))
        pol.extracto= 'Este el el texo que siempre quise escribir sobre un teclado de un computador nuevo'
        print(pol.extracto, type(pol.extracto))
        pol.estado = True
        #pol.save()
        for preg in preguntas:
            print(preg.pregunta, type(preg.pregunta), )


'''


