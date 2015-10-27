==================================================================
Host de un BLOG en una Página de GitHub
==================================================================

:date: 2015-10-23 10:59
:tags: python, web
:slug: Segundo

`La página de GitHub <http://pages.github.com>`_ es un servicio gratis de web hosting para proyectos compuestos de archivos estáticos.
Combina **Páginas del repositorio** con **la version de control de git** y un **generador estático de sitios** como **Pelican**   que nos permite tener un conjunto increible de herramientas para construir un sitio web.

**Entonces..!**

**1 INSTALACIÓN DE GIT**.

Instalar el paquete de git y escribir las configuraciones globales para nombre  usuario. 
::

  $ sudo apt-get install git git-doc
  $ git config --global user.name "USERNAME"
  $ git config --global user.email USERNAME.EMAIL@example.com
  $ git config --global core.edito EDITOR 

**2 CREACION DEL REPOSITORIO GIT**.

Dentro de mi carpeta llamada alex  donde creamos el blog, creo 2 archivos llamados: **.gitignore** y  **readme.rst**.
El archivo **.gitignore** se encarga de ignorar que archivos o directorios no seran considerados en el track de la version de control.
Por ejemplo, yo no quiero almacenar en el track: 

::

  *.pid 
  *.pyc 
  output/ 

Crearemos un archivo README.rst que le permitira a GitHub conocer de que se trata el proyecto. En mi caso luce asi: 

::

  www dot avaldezp dot com
  "======================="
  
  This repository holds my blog which you can visit at www.avaldezp.com.

  It is compiled by `Pelican <http://docs.getpelican.com/>`_ and hosted on `GitHub Pages <http://pages.github.com/>`_.

Ahora , podemos crear el repositorio local, añadimos los archivos y lo que queremos almacenar en el track y ejecutamos el primer commit:

::

  $ git init
  $ git add README.rst
  $ git add .gitignore
  $ git add Makefile
  $ git add content/
  $ git add pelicanconf.py
  $ git add publishconf.py
  $ git status
  $ git commit -a -m "Primer commit"
  $ git log


**3 TEST DEL SITIO**

La página de usuario de GitHub mostrará todo el contenido en la rama master. Yo prefiero trabajar en una nueva rama con mis archivos y almacenar solo el output hacia la rama master. Creamos primero una nueva rama de trabajo llamada **source**. 

:: 

  $(pelican)alex@alex-Satellite-P745D:~/.virtualenvs/pelican/alex$ git checkout  -b source

Antes de publicar una forma de testear podemos tester el sitio en el host local con los comandos:

::

  $(pelican)alex@alex-Satellite-P745D:~/.virtualenvs/pelican/alex$ make html
  $(pelican)alex@alex-Satellite-P745D:~/.virtualenvs/pelican/alex$ make serve

Trataermos de visualizarlo en  en localhost:8000 desde un navegador web. Si todo esta bien :D ya estamos listos!.
Como todo resulto bien en el test, tengo mi folder output y quiero guardar todo lo que tengo hasta el momento. Usando Git hago un commit de todos mis cambios locales. Esta es una buena practica para tener una version de control de nuestro trabajo, para hacer esto solo usamos 2 comandos. Primero, añadimos los archivos y despues hacemos el commit.

:: 

  $ git add .
  $ git commit -m "Segundo Commit"

**4 PUBLICACIÓN DEL BLOG EN GITHUB**

Recordando que nos encontramos en una rama llamada  "**source** ,necesitamos copiar los archivos necesarios hacia la rama master para tenerla en nuestra Página de Usuario de GitHub. Para hacer esto podemos empujar directameente el folder llamado output  al folder master, pero yo prefiero usar un script que me ayuda a hacer este tarea. El script que hago mención y que uso se llama ghp-import. Este script exporta el contenido del folder output hacia la 
"gh-pages" rama. Entonces creo una rama  llamada "gh-pages", corro el script , y luego empujro el contenido de la gh-pages hacia mi rama master.
Estos pasos son mostrados acontinuacion en la linea de comandos.

Si no tienes instalado ghp-import, lo puedes obtener simplemente con:

::

  $(pelican)alex@alex-Satellite-P745D:~/.virtualenvs/pelican/alex$ pip install ghp-import

Creamos la rama gh-pages y corremos el script ghp-import.

::

  $(pelican)alex@alex-Satellite-P745D:~/.virtualenvs/pelican/alex$ git branch gh-pages
  $(pelican)alex@alex-Satellite-P745D:~/.virtualenvs/pelican/alex$ ghp-import output
  $(pelican)alex@alex-Satellite-P745D:~/.virtualenvs/pelican/alex$ git checkout master
  $(pelican)alex@alex-Satellite-P745D:~/.virtualenvs/pelican/alex$ git merge gh-pags
  $(pelican)alex@alex-Satellite-P745D:~/.virtualenvs/pelican/alex$ git push --all

Visualizemos ahora nuestra página de Usuario en GitHub y esperemos pacientemente, nuestro sitio se mostrará pronto. Hemos subido todo la rama al repositorio de Git, pero tu solo puedes subir la rama master y la rama source. No necesitaremos nunca la rama gh-pages.

En el post, el nombre de usuario que estoy usando es alexvaldez24, entonces para ver la  página estática de nuestro blog buscamos el sitio 
`alexvaldez24.github.io/avaldezp/ <http://alexvaldez24.github.io/avaldezp/>`_



My *second* post using `Pelican <http://docs.getpelican.com/en/3.3.0/getting_started.html>`_ 
Buena Suerte!

