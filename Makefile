# This Makefile wraps commands used to set up the learning module and 
# start the Tellina server.

run: git submodule update --remote
    
    # Set up data files in the learning module
    tar xf tellina_learning_module/data/bash/vocab.tar.xz tellina_learning_module/data/bash/
    # Run server
    python3 manage runserver 0.0.0.0:8000    

# Destroy database and migrations
clean:  rm -rf db.sqlite3 tellina/migrations 
