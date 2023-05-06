# mejorar o agregar

para mejorar el desarrollo debes conocer python y conocer virtual-env

se recomienda usar virtualenv para desarrollar el bot "se debe usar python3 no python2" pip o pip3 install virtualenv 

``` bash
# windows
python -m venv venv

# linux y mac
python3 -m venv venv
```

para activar vitrualenv:
 * windows: .\venv\scripts\activate.bat
 * linux y mac: source ./venv/bin/activate

## install python module:
luego de activar el virtualenv lo siguiente es ejecutar lo siguiente. 
### opcion 1
>pip install -r requirements.txt

### opcion 2
>pip3 install -r requirements.txt

## compilar app
``` bash
pyinstaller --onefile app.py -n=stack-supreme
```