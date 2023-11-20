# machine-learning
Machine Learning Python notebooks

## How to start a Docker JupyterLab
We will use JupyterLab in most of our videos. We start JupyterLab using Docker. Here is the command:

```bash
docker run -p 9999:8888 --name jupyterlab -e JUPYTER_TOKEN=docker -it jupyter/datascience-notebook:latest
```
Here is an explanation of the parameters:
- `-p 9999:8888`: is the mapping port in this format `<host port>:<container port>`. This image exposes the JupyterLab in `8888`, with this parameter you can map this port to one available in your machine
- `--name jupyterlab`: is the name of your container
- `-e JUPYTER_TOKEN=docker`: is the token you will enter when starting the JupyterLab
- ` -it`: interactive terminal
- `jupyter/datascience-notebook:latest`: the name of the Docker image

Please, notice you will lose your notebooks once you stop and delete the Docker container. In order to persist your notebooks you can create a volume:
```bash
docker run -p 9999:8888 --name jupyterlab -v <your working directory>:/home/jovyan/work -e JUPYTER_TOKEN=docker -it jupyter/datascience-notebook:latest
```
