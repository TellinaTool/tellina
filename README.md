# Tellina

Tellina uses natural language processing (NLP) to translate an English sentence, such as "Find text file in the current folder", into a bash command, such as `find . -name "*.txt"`.

You can try it now at http://tellina.rocks .
Or, you can install it locally; this document tells you how.

### Install Tensorflow:

Tellina uses Tensorflow r0.12. (We are upgrading to r1.1 soon!) 

Follow the instructions on the [Tensorflow website](https://www.tensorflow.org/versions/r0.12/get_started/os_setup.html). The simplest way is to install using [`pip3`](https://www.tensorflow.org/versions/r0.12/get_started/os_setup.html#pip-installation).

### Install other dependencies:

```
pip3 install -r requirements.txt
```

### Set up tellina_learning_module submodule:

```
git submodule update --init --remote
git submodule foreach git pull origin master
```
To update the tellina_learning_module in the future, run:
```
make git
```

### Set up databases:

```
make db
```

### Run webapp:

```
make run
```
Visit http://127.0.0.1:8000 in your browser.
