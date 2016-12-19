# Tellina

### Install Tensorflow:

Follow the instructions on the [official website](https://www.tensorflow.org/versions/r0.9/get_started/os_setup.html). The simplest way is to install using [`pip3`](https://www.tensorflow.org/versions/r0.11/get_started/os_setup.html#pip-installation).

### Install other dependencies:

```
pip3 install -r requirements.txt
```

### Set up commandline-helper submodule:

```
git submodule update --remote
git submodule foreach git pull origin master

cd commandline-helper/data/bash
tar -xzvf vocab.tar.xz && rm vocab.tar.xz
```

### Set up databases

```
python manage.py makemigrations
python manage.py migrate
```

### Run webapp:

```
export PYTHONPATH=`pwd`

python3 manage.py runserver
```
Visit http://127.0.0.1:8000 in your browser.
