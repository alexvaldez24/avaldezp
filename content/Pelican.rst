==================================================================
Construir un Blog a través del Generador Estático de Sitio PELICAN
==================================================================

:date: 2015-10-21 10:00
:tags: pelican, web
:slug: Inicio

Pelican es un poderoso **generador estático de sitios de Python**. El diseño de como se ve y la disposición de los elementos
de este sitio fueron basados en la página de `Christine <http://chdoig.github.io/create-pelican-blog.html>`_.
Para el diseño y el tema se utilizo Twitter Bootstrap, y para escribir las publicaciones usamos **reStructuredText**, luego Pelican 
se encarga de compilar el contenido en una salida de html apropiada para el blog.

Me gusta la  idea de crear un sitio web estático. Algunas de las ventajas son:

- No se requiere una base de datos... plaintext es facil de editar, hacer backup y mover de un lado a otro.
- plaintext te permite utilizar un editor.. yo estoy usando nano, pero puedes usar vim,gedit,emacs,etc
- Barato y facil de publicar practicamente donde uno desee.. una opción: `Github <https://github.com>`_.
- Seguridad.Evitamos los problemas de seguridad teniendo el software instalado en el host web.
- Obsolencia.No hay que preocuparse sobre los updates y mantenimiento del software del lado del servidor.

La tradicional desventaja de usar páginas estáticas para un blog ha sido la ausencia de elementos dinámicos-comentarios de usuarios-
pero Javascript para cosas como Twitter widget le proveen actualizaciones en tiempo real .

Es asi como construi mi blog usando Pelican .

**1 INSTALACIÓN**.

Instale primero Pelican y algunas herramientas adicionales para crear un entorno virtual usando 
`virtualenv <http://www.circuidipity.com/python2-and-python3.html>`_ y `pip <https://pypi.python.org/pypi/pip>`_. 
Esto me permite crear una area de trabajo específica para mi blog y un usuario separado de mi instalacion de python por defecto.
Con el virtualenv instalado y usando mi blog como ejemplo: :: 

$ cd /home/alex/.virtualenvs/	                                                                                                     
$ virtualenv ~/.virtualenvs/pelican                                                                                            
$ source ~/.virtualenvs/pelican/bin/activate                                                                                         
$ cd pelican                                                                                                                           
$ (pelican)alex@alex-Satellite-P745D:~/.virtualenvs/pelican$ pip install pelican                                                   

Luego cree un directorio para almacenar el contenido de mi blog y ejecutar pelican-quickstart para crear el diseño y la configuración  del sitio por defecto. El tema y el diseño del sitio por defecto al final fue modificado porque utilize el tema y el plugins de 
`Christine <http://chdoig.github.io/create-pelican-blog.html>`_

::

  $ (pelican)alex@alex-Satellite-P745D:~/.virtualenvs/pelican$ mkdir alex
  $ (pelican)alex@alex-Satellite-P745D:~/.virtualenvs/pelican$ cd alex
  $ (pelican)alex@alex-Satellite-P745D:~/.virtualenvs/pelican/alex$ pelican quickstart
  Welcome to pelican-quickstart v3.3.0.

  This script will help you create a new Pelican-based website.

  Please answer the following questions so this script can generate the files
  needed by Pelican.
  > Where do you want to create your new web site? [.]
  > What will be the title of this web site? Alex@nderV.
  > Who will be the author of this web site? Alexander Valdez
  > What will be the default language of this web site? [en]
  > Do you want to specify a URL prefix? e.g., http://example.com   (Y/n) n
  > Do you want to enable article pagination? (Y/n) n
  > Do you want to generate a Fabfile/Makefile to automate generation and publishing? (Y/n)
  > Do you want an auto-reload & simpleHTTP script to assist with theme and site development? (Y/n)
  > Do you want to upload your website using FTP? (y/N)
  > Do you want to upload your website using SSH? (y/N)
  > Do you want to upload your website using Dropbox? (y/N)
  > Do you want to upload your website using S3? (y/N)
  > Do you want to upload your website using Rackspace Cloud Files? (y/N)
  Done. Your new project is available at /home/dwa/circuidipity

Esta es la disposición de archivos generada por pelican-quickstart:

::

  $ tree
  ├── content
  ├── develop_server.sh
  ├── fabfile.py
  ├── Makefile
  ├── output
  ├── pelicanconf.py
  └── publishconf.py
  2 directories, 5 files .
  

**2 PRIMER POST**.

Los post o anotaciones van en la carpeta content y además yo he creado una carpeta images y pages como subdirectorio dentro del folder content
para colocar imagenes y otras opciones como about y contact.

::

  $ mkdir content/{images,pages}

Dentro de content creo el primer post llamando hola_mundo.rst using **reStructuredText**:

::
   
   Hello   World
   
   :date: 2015-10-01 10:30
   :tags: pelican , web
   :slug: hello
   My *first* post using `Pelican <http://docs.getpelican.com/en/3.3.0/getting_started.html>`_!

Items como :date :tags :slug son metada que puede ser usaada en la salida generada de HTML. Estos elementos y otros son incluidos
en Pelican y los usuarios pueden crear sus propios elementos en `templates <http://docs.getpelican.com/en/3.1.1/themes.html#theming-pelican>`_.

Finalmente guardamos el archivo y probamos el nuevo blog ejecutando el servidor desarrollado en Pelican. Esto tomará todos los archivos
*.rst  y generará  los archivos HTML en **output** y se prodrá visualizar en el browser http://localhost:8000:

(pelican)alex@alex-Satellite-P745D:~/.virtualenvs/pelican/alex$ make devserver 

El servidor se ejecutará en backgroud y se actualizara en caso hubiera una actualización de contenido para la vista. Para detener el 
servidor debemos ejecutar el comando  ./develop_server.sh stop.

**3 AJUSTES**.

Ejecutando pelican-quickstart creamos 2 archivos de configuracion: pelicanconf.py  y publishconf.py
Las configuraciones primarias se encuentra en pelicanconf.py.  Los ajustes pueden ser usados como variables en posts, páginas y templates. 
Esta es como luce mi configuracion:D....  Algunos de los ajustes como AUTHOR y SITENAME fueron generados automaticamente por Pelican y 
otros como ABOUT_ME los hice yo.

::

  #!/usr/bin/env python
  # -*- coding: utf-8 -*- #
  from __future__ import unicode_literals

  AUTHOR = u'Alexander Valdez Portocarrero'
  SITENAME = u'Alex@nderV.'
  SITEURL = ''

  PATH = 'content'

  TIMEZONE = 'Europe/Paris'

  DEFAULT_LANG = u'en'

  DEFAULT_DATA_FORMAT= '%A %d %B %Y'

  #Static paths will be copied without parsing thero
  STATIC_PATHS= ['images','extra']
  ABOUT_ME = "Whatever you want to say about yourself"
  STATIC_PATHS = ['images']
  PROFILE_PICTURE = "bananaprofilepicture.png"

  HEADER_IMAGE = "alexheaderimage.png"
  GITHUB_ICON= "github-icon"


  #Shift the installed location of a file
  EXTRA_PATH_METADA={ 
  'extra/CNAME':{'path','CNAME'},
  }	

  #Extract post date from filename
  FILENAME_METADA= '(?P<date>\d{4}-\d{2}-\d{2})'

  #Sole author and don't  use categories... dis
  AUTHOR_SAVE_AS= False
  AUTHORS_SAVE_AS=False
  CATEGORY_SAVE_AS=False
  CATEGORIES_SAVE_AS=False

  # Feed generation is usually not desired when developing
  FEED_ALL_ATOM = None
  CATEGORY_FEED_ATOM = None
  TRANSLATION_FEED_ATOM = None
  AUTHOR_FEED_ATOM = None
  AUTHOR_FEED_RSS = None

  #URL settings
  #Uncomment following line if you want documente-relative URLSs when developing
  RELATIVE_URLS = True
  ARTICLE_URL='{slug}.html'
  PAGE_URL ='{slug}.html'
  PAGE_SAVE_AS='{slug}.html'
  TAG_URL='tag-{slug}.html' 
  TAGE_SAVE_AS='tag-{slug}.html'
  TAGS_URL='tags.html'
  TAGS_SAVE_AS='tags.html'
  ARCHIVES_URL='archives.html'
  ARCHIVES_SAVE_AS='archives.html'

  #Contact
  EMAIL_ADDR= 'alex.valdezp22 at gmail dot com'

  #Plugins
  PLUGIN_PATH='/home/alex/pelican_plugins/pelican-plugins'
  PLUGINS=['neighbors']

  #Theme
  #THEME='/home/alex/pelican_themes/pelican-themes/pelican-bootstrap3'
  THEME='/home/alex/pelican_themes/pelican-bootstrap3-lovers'
  BOOTSTRAP_THEME='lovers'

  WHOAMI_URL='/home/alex/Pictures/pelican_images/whoami.jpg'
  GREETING= 'Howdy!'
  #LICENCE_NAME='BY-NC-SA'
  #LICENCE_URL='http://creativecommons.org/licenses/by-nc-sa/3.0/deed.en_US'
  #LICENCE_URL_IMG='http://i.creativecommons.org/l/by-nc-sa/3.0/80x15.png'
  JINJA_EXTENSIONS=['jinja2.ext.loopcontrols']

  #Social
  TWITTER_URL='https://twitter.com/alexvaldez900'
  GITTHUB_URL='https://github.com/alexvaldez24'

  #Tag cloud
  TAG_CLOUD_STEPS = 4

  # Blogroll
  LINKS = (('Pelican', 'http://getpelican.com/'),
  ('Python.org', 'http://python.org/'),
  ('Jinja2', 'http://jinja.pocoo.org/'),
  ('You can modify those links in your config file', '#'),)

  # Social widget
  #SOCIAL = (('You can add links in your config file', '#'),
  #          ('Another social link', '#'),)
  # Social settings
  SOCIAL = (('github', 'https://github.com/alexvaldez24'),
  ('twitter', 'https://twitter.com/alexvaldez900'),)

  DEFAULT_PAGINATION = False

  # Uncomment following line if you want document-relative URLs when developing
  #RELATIVE_URLS = True

El segundo archivo de configuración se llama publishconf.py , este contiene ajustes de prioridad para publicar el cotenido:

:: 

  #!/usr/bin/env python
  # -*- coding: utf-8 -*- #
  from __future__ import unicode_literals

  # This file is only used if you use `make publish` or
  # explicitly specify it as your config file.

  import os
  import sys
  sys.path.append(os.curdir)
  from pelicanconf import *

  SITEURL = 'http://www.avaldezp.com'
  RELATIVE_URLS = False

  FEED_ALL_ATOM = 'feed.xml'
  CATEGORY_FEED_ATOM = None
  TRANSLATION_FEED_ATOM=None
  Feed_Max_ITEMS= 25

  DELETE_OUTPUT_DIRECTORY = True

  # Following items are often useful when publishing

  #DISQUS_SITENAME = ""
  #GOOGLE_ANALYTICS = ""  

**4 PLUGINS**.

Plugins estan disponibles para ampliar la funcionalidad de Pelican. He usado el plugin llamado
`neighbors <https://github.com/getpelican/pelican-plugins/tree/master/neighbors>`_ que hace sencillo añadir
links y ordenar artículos nuevos y antiguos en relacion con la página actual.

Para habilitar plugins en pelicanconf.py:

::

  PLUGIN_PATH='/home/alex/pelican_plugins/pelican-plugins'
  PLUGINS=['neighbors']

**5 THEMES**.

Pelican incluye un tema por defecto que nos permite empezar y tambien hay una colección de 
`temas creados por los usuarios <https://github.com/getpelican/pelican-themes>`_  yo he utilizado el tema  
llamado `Pelican-bootstrap3-lovers <https://github.com/chdoig/pelican-bootstrap3-lovers>`_.

Para usar un tema se debe setear la ubicación de el contenido en pelicanconf.py: 

::

  THEME='/home/alex/pelican_themes/pelican-bootstrap3-lovers'
  BOOTSTRAP_THEME='lovers'

**6 PUBLISH**.

Cuando estemos listos para generar y publicar :

::

  (pelican)alex@alex-Satellite-P745D:~/.virtualenvs/pelican/alex$ make publish

Todo el contenido del blog esta situado en **output** listo para ser subido a un servicio de hosting. Como todo el contenido es estático
hay muchas opciones disponibles.  Yo uso de manera gratuita  github como ven 
`Alex@nderVP <http://alexvaldez24.github.io/avaldezp/>`_.


My *first* post using `Pelican <http://docs.getpelican.com/en/3.3.0/getting_started.html>`_ 
Buena Suerte!

