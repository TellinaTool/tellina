# This Makefile wraps commands used to set up the learning module and 
# start the Tellina server.

git: 
	# Update learning submodule
	git submodule update --remote

run: 
	# Set up data files in the learning module
	tar xf tellina_learning_module/data/bash/vocab.tar.xz tellina_learning_module/data/bash/
	# Run server
	python3 manage runserver 0.0.0.0:8000    

clean: 
	# Destroy database and migrations	 
	rm -rf db.sqlite3 tellina/migrations 