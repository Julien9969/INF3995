## Prérequis
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [rocker](https://github.com/osrf/rocker)
- [nvm v20.12.2](https://nodejs.org/en/blog/release/v20.12.2)

## Installation (Linux)

1. Cloner le projet avec les **submodules**
```bash
git clone --recurse-submodules git@gitlab.com:polytechnique-montr-al/inf3995/20241/equipe-102/INF3995-102.git
```

2. Se placer dans le répertoire du projet
```bash
cd INF3995-102
```
Ces 3 dossiers devraient être présent:
- `INF3995-Backend`
- `INF3995-Frontend`
- `INF3995-Robot`


3. Lancer le serveur et le client par docker-compose
```bash
docker compose up
```

4. Se placer dans le répertoire INF3995-Robot
```bash
cd INF3995-Robot
```

5. Build et démarrer de docker de simulation
```bash
docker build -t "rosignbase" ./simulation
```

```bash
rocker --x11 --device=/dev/dri --volume $(pwd):/root/INF3995-Robot --port 22900:22900 --port 22901:22901 --port 22902:22902 --port 22910-22921:22910-22921 --image-name=rosign --name=simulation-ign rosignbase 
```

6. Une fois dans le shell de la simulation, executer le script suivant:
```bash
./deploy-simulation.sh
```

7. Démarrer la simulation dans gazebo

Appuyer sur le bouton play orange en bas à gauche dans gazebo pour démarrer la simulation


## Utilisation

- Acceder au site web à l'adresse **[http://localhost:4200](http://localhost:4200)**

- Visualiser la simulation dans Gazebo

## Tests
1. Test unitaires Backend

Ouvrir un nouveau terminal et executer la commande suivante:

```bash
docker exec -it backend-container bash -c "cd /src/app/ros_nodes/src/backend_server && pytest --ignore=./test --cov-report term-missing --cov=backend_server backend_server/"
```

2. Test unitaires Frontend

Ouvrir un nouveau terminal et executer la commande suivante:

```bash
docker exec -it frontend-angular bash -c "cd /src/app && npm run coverage-gitlab"
```



3. Ouvrir un shell dans la simulation

```bash
docker exec -it simulation-ign bash 
```


➡️ Pour pull sur le repo main: `git pull --recurse-submodules git@gitlab.com:polytechnique-montr-al/inf3995/20241/equipe-102/INF3995-102.git puis possiblement `cd` dans les submodules qui ont été mis à jour et faire git switch main`