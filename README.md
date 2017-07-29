# Tellina

Tellina uses natural language processing (NLP) to translate an English sentence, such as "Find text file in the current folder", into a bash command, such as `find . -name "*.txt"`.

You can try it now at http://tellina.rocks .
Or, you can install it locally; this document tells you how.

### Install Tensorflow:

Tellina uses Tensorflow (>=r1.0).

Follow the instructions on the [Tensorflow website](https://www.tensorflow.org/get_started/get_started). The simplest way is to install using [`pip3`](https://www.tensorflow.org/install/).

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

To experiment with the translation model locally, make sure to set following control variables correctly.

### Control variables:

```
WEBSITE_DEVELOP (website/views.py) 

  - True (default), start the web server without importing the Tensorflow translation module (fast start)
  - False, start the web server and translate new queries (5-10 secs delay during start)
```
Visit http://127.0.0.1:8000 in your browser.
