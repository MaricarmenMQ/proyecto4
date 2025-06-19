from django.shortcuts import render
from django.http import HttpResponse
from . import data 

def Hola(request):
    return HttpResponse("Hola mundo...!")
def datos_personales(request):
    html = '''
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Mis Datos Personales - Maricarmen</title>
        <link rel="stylesheet" type="text/css" href="/static/css/estilos.css">
    </head>
    <body>
        <div class="contenedor">
            <div class="encabezado-seccion">
                <img src="/static/imagenes/imagenc.jpg" alt="imagenc" class="imagenc-img">
                <h1>''' + data.DATOS_PERSONALES['titulo'] + '''</h1>
            <div class="descripcion-seccion">
            <h2> '''+ data.DATOS_PERSONALES['descripcion'] +'''</h2>
            </div>
            <div class="info-personal">
    '''
    for etiqueta, valor in data.INFO_ITEMS:
        html += f'''
                <div class="dato">
                    <span class="etiqueta">{etiqueta}:</span>
                    <span class="valor">{valor}</span>
                </div>
        '''
    html += '''
            </div>
            
            <div class="botones-navegacion">
                <a href="/datos" class="boton">Datos</a>
                <a href="/preferencias" class="boton">Preferencias</a>
                <a href="/gustos" class="boton">Gustos</a>
                <a href="/habilidades" class="boton">Habilidades</a>
                <a href="/familia" class="boton">Familia</a>
            </div>
        </div>
        
    </body>
    </html>
    '''
    return HttpResponse(html)

def preferencias(request):
    html = '''
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Mis Preferencias - Maricarmen</title>
        <link rel="stylesheet" type="text/css" href="/static/css/estilos.css">
    </head>
    <body>
        <div class="contenedor">
            <h1>Mis Preferencias</h1>
            
            <div class="seccion">
                <div class="titulo-seccion">Géneros Musicales</div>
                <ul class="lista">
    '''
    for genero in data.GENEROS_MUSICALES:
        html += f'<li class="item">{genero}</li>'
    html += """
                </ul>
            </div>
            <div class="seccion">
                <div class="titulo-seccion">Artistas Favoritos</div>
                <ul class="lista">
    """
    for artista in data.ARTISTAS_FAVORITOS:
        html += f'<li class="item">{artista}</li>'
    html += '''
                </ul>
            </div>
            <div class="seccion">
                <div class="titulo-seccion">Canciones que me gustan</div>
                <ul class="lista">
    '''
    for cancion in data.CANCIONES_FAVORITAS:
        html += f'<li class="item">{cancion}</li>'
    html += '''
                </ul>
            </div>
            <div class="seccion">
                <div class="titulo-seccion">Películas y Series</div>
                <ul class="lista">
    '''
    for titulo in data.PELICULAS_SERIES:
        html += f'<li class="item">{titulo}</li>'
    html += '''
                </ul>
            </div>
            <div class="botones-navegacion">
                <a href="/datos" class="boton">Datos</a>
                <a href="/preferencias" class="boton">Preferencias</a>
                <a href="/gustos" class="boton">Gustos</a>
                <a href="/habilidades" class="boton">Habilidades</a>
                <a href="/familia" class="boton">Familia</a>
            </div>
        </div>
    </body>
    </html>
    '''
    return HttpResponse(html)

def gustos(request):
    html = '''
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Mis Gustos - Maricarmen</title>
        <link rel="stylesheet" type="text/css" href="/static/css/estilos.css">
    </head>
    <body>
        <div class="contenedor">
            <h1>Mis Gustos e Intereses</h1>
    '''
    for categoria, items in data.MIS_GUSTOS.items():
        if categoria == 'pasatiempos':
            titulo = 'Cosas que me gusta hacer'
        elif categoria == 'comida_favorita':
            titulo = 'Mi comida favorita'
        elif categoria == 'mascotas':
            titulo = 'Mis mascotas'
        else:
            titulo = categoria.title()
        html += f'''
            <div class="seccion">
                <div class="titulo-seccion">{titulo}</div>
                <ul class="lista">
        '''
        for item in items:
            html += f'<li class="item">{item}</li>'
        html += '''
                </ul>
            </div>
        '''
    
    html += '''
            <div class="botones-navegacion">
                <a href="/datos" class="boton">Datos</a>
                <a href="/preferencias" class="boton">Preferencias</a>
                <a href="/gustos" class="boton">Gustos</a>
                <a href="/habilidades" class="boton">Habilidades</a>
                <a href="/familia" class="boton">Familia</a>
            </div>
        </div>
    </body>
    </html>
    '''
    return HttpResponse(html)

def habilidades(request):
    html = '''
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Mis Habilidades - Maricarmen</title>
        <link rel="stylesheet" type="text/css" href="/static/css/estilos.css">
    </head>
    <body>
        <div class="contenedor">
            <h1>Mis Habilidades y Aptitudes</h1>
    '''
    for categoria, lista_habilidades in data.HABILIDADES.items():
        if categoria == 'idiomas':
            titulo = 'Idiomas que manejo'
        elif categoria == 'tecnicas':
            titulo = 'Habilidades técnicas'
        elif categoria == 'personales':
            titulo = 'Cualidades personales'
        else:
            titulo = categoria.title()        
        html += f'''
            <div class="seccion">
                <div class="titulo-seccion">{titulo}</div>
                <ul class="lista">
 '''
        for habilidad in lista_habilidades:
            html += f'<li class="item">{habilidad}</li>'
        html += '''
                </ul>
            </div>
        '''
    html += '''
            <div class="botones-navegacion">
                <a href="/datos" class="boton">Datos</a>
                <a href="/preferencias" class="boton">Preferencias</a>
                <a href="/gustos" class="boton">Gustos</a>
                <a href="/habilidades" class="boton">Habilidades</a>
                <a href="/familia" class="boton">Familia</a>
            </div>
        </div>
    </body>
    </html>
    '''
    return HttpResponse(html)

def familia(request):
    html = '''
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Mi Familia - Maricarmen</title>
        <link rel="stylesheet" type="text/css" href="/static/css/estilos.css">
    </head>
    <body>
        <div class="contenedor">
            <h1>Mi Entorno Social y Familia</h1>
    '''
    for grupo, personas in data.ENTORNO_SOCIAL.items():
        if grupo == 'padres':
            titulo = 'Mis padres'
        elif grupo == 'hermanos':
            titulo = 'Mis hermanos'
        elif grupo == 'sobrinos':
            titulo = 'Mis sobrinos'
        elif grupo == 'amigos':
            titulo = 'Mis amigos cercanos'
        else:
            titulo = grupo.title()
        html += f'''
            <div class="seccion">
                <div class="titulo-seccion">{titulo}</div>
                <ul class="lista">
        '''
        for persona in personas:
            html += f'<li class="item">{persona}</li>'
        html += '''
                </ul>
            </div>
        '''
    html += '''
            <div class="botones-navegacion">
                <a href="/datos" class="boton">Datos</a>
                <a href="/preferencias" class="boton">Preferencias</a>
                <a href="/gustos" class="boton">Gustos</a>
                <a href="/habilidades" class="boton">Habilidades</a>
                <a href="/familia" class="boton">Familia</a>
            </div>
        </div>
    </body>
    </html>
    '''
    return HttpResponse(html)