import mechanize
from lxml import html
import re
from timeit import default_timer as timer
import unicodedata
#from .rut import rut

def get_datos(entrada, formulario):
    may = '18.168.143'
    rut=entrada.split('-')
    if (revisa(entrada) and formulario==0) or (rut[0]== may and formulario==1):
        persona = {
                'nombre': 'Sepulveda Avila Mayra Victoria',
                'run': '18.168.143-8',
                'sex': 'MUJ',
                'dir': 'Seminario 999',
                'dist': 'Providencia'
                }
    else:
        inicio = timer()
        brwsr = mechanize.Browser()
        brwsr.set_handle_robots(False)
        brwsr.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
        brwsr.open('https://www.nombrerutyfirma.com/')

        brwsr.select_form(nr = formulario)
        #brwsr['term'] = 'vicente sepulveda avila'
        #brwsr['term'] = '8.828.535-2'
        brwsr['term'] = entrada
        response = brwsr.submit()
        info = response.read()
        page = info.decode("utf-8")
        tree = html.fromstring(page)
        a=tree.xpath('//div[@class="container"]')
        persona = {}
        inx = {27:'nombre',29:'run',31:'sex',33:'dir',35:'dist'}
        for i,ii in enumerate(a[0].itertext()):
            cl = re.sub('\t+','', ii )
            cl = re.sub('\n+','', cl )
            if i in inx.keys():
                persona[inx[i]]=cl
                #print(i, type(cl),len(cl),cl)
        print("\n datos:",persona, entrada)
        print(timer()-inicio)
    return persona, entrada

# lista = rut.genera_rut(cantidad=10, inicio=8828530, csv=False)

# for i in lista:
#     r= "{:,}".format(int(i.split("-")[0]))
#     r= r.replace(",",".") + "-0"
#     print(r)
#     get_datos(r)
#get_datos('8.828.535-0')


def revisa(nombre):
    val = False
    normal = unicodedata.normalize('NFKD', nombre.lower()).encode('ASCII', 'ignore').decode("utf-8")
    lista=normal.split(' ')
    match = ['mayra', 'sepulveda', 'avila']
    if match[0] in lista and match[1] in lista and match[2] in lista:
        val = True
    return val



