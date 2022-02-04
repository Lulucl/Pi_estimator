# Pi_estimator

Cette application permet d'estimer pi avec spark et numpy

Travail en binome : CONTAL Lucie et LE QUENTREC Jade

n = 100000
spark :
temps d execution = 0.09695306301116943
valeurs de pi = 3.1406656
ecart % Math.pi = 0.029509032265326775
numpy :
temps d execution = 0.025617461204528808
valeurs de pi = 3.14123
ecart % Math.pi = 0.01154362228911298

n = 1000000
spark :
temps d execution = 0.18919002056121825
valeurs de pi = 3.14186384
ecart % Math.pi = 0.008632131536756767
numpy :
temps d execution = 0.21743435859680177
valeurs de pi = 3.14174412
ecart % Math.pi = 0.004821325579355914

Plus n est grand, plus le temps d execution augmente et plus le pourcentage d erreur est faible. 

Nous avons, pour nos deux cas tests, calculer la moyenne sur 100 executions car, d un test a l autre, avec les memes parametres, les resultats pouvaient etre tres different.

Pour lancer le programme, placez vous dans le dossier src et executez spark-submit main.py. Les resulats sont sauvegardes dans le dossier OUTPUT. Ils sont aussi affiches dans le terminal.