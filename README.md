# Tellina

### Install Tensorflow:

```
Follow the official instruction on installing with `pip3`

https://www.tensorflow.org/versions/r0.11/get_started/os_setup.html#pip-installation
```

### Install other dependencies:

```
pip3 install -r requirements.txt
```

### Set up commandline-helper submodule:

```
git submodule update --remote
git submodule foreach git pull origin master
```

### Run webapp:

```
export PYTHONPATH=`pwd`

python3 manage.py runserver
```
Visit http://127.0.0.1:8000 in your browser.
