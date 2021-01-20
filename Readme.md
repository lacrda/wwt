Simple python game built on Flask

##How it Works

A map is divided in 16 territories, one for each player. Each time the url "/nrounds" is called the game plays a round. A round consists in the game randomly choosing one territory to be the invader and in sequence randomly choosing one of the neighboors to be the target. At the end of the round the owner of the attack territory has one more territory in her possession.
