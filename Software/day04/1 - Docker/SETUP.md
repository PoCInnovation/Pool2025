# Setup - [Docker]

Let's install [Docker](https://docs.docker.com/engine/install/fedora/)
engine with his CLI and [docker compose](https://docs.docker.com/compose/install/linux).

## Install [Docker]

> ⚠️ The following steps are made for fedora (your default dump). <br>
> If you use another OS, please, follow this [documentation](https://docs.docker.com/engine/install/)

#### Clean up

Let's start by removing old unused dependencies

```shell
sudo dnf remove docker                   \
                docker-client            \
                docker-client-latest     \
                docker-common            \
                docker-latest            \
                docker-latest-logrotate  \
                docker-logrotate         \
                docker-selinux           \
                docker-engine-selinux    \
                docker-engine
```

#### Installation

We can now install docker engine and the compose plugin:

```shell
# Add docker repository to your package manager
sudo dnf -y install dnf-plugins-core
sudo dnf config-manager --add-repo https://download.docker.com/linux/fedora/docker-ce.repo

# Install Docker
sudo dnf install docker-ce docker-ce-cli containerd.io

# Install docker compose
sudo dnf install docker-compose-plugin

### Start Docker

After installing all the dependencies, start docker engine:

```shell
# Start docker service
sudo systemctl start docker

# Optional: Automatically start it when on computer start
sudo systemctl enable docker
```

The last thing to do for a seamless experience is to [enable the use of Docker without a root user](https://docs.docker.com/engine/install/linux-postinstall/#manage-docker-as-a-non-root-user): 

```shell
# Add current user to docker group to use docker CLI without sudo
sudo groupadd docker
sudo usermod -aG docker $USER

# Logout from your user session or restart your computer
```

#### Troubleshooting

If you are on Fedora 31+, you will certainly meet this issue:

```shell
docker: Error response from daemon: cgroups: cannot found cgroup mount destination: unknown.
```

If that happens, read this [issue](https://github.com/docker/for-linux/issues/219)
and try the fixes in it.

> If you still struggle, don't hesitate to ask the staff to help you 😄

## Check your installation

You can verify that everything goes well by running a [`hello-world`](https://hub.docker.com/_/hello-world)
container.

You should have the following output:

```shell
docker run hello-world
# Unable to find image 'hello-world:latest' locally
# latest: Pulling from library/hello-world
# 2db29710123e: Pull complete 
# Digest: sha256:18a657d0cc1c7d0678a3fbea8b7eb4918bba25968d3e1b0adebfa71caddbc346
# Status: Downloaded newer image for hello-world:latest
# 
# Hello from Docker!
# This message shows that your installation appears to be working correctly.
# 
# To generate this message, Docker took the following steps:
#  1. The Docker client contacted the Docker daemon.
#  2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
#     (amd64)
#  3. The Docker daemon created a new container from that image which runs the
#     executable that produces the output you are currently reading.
#  4. The Docker daemon streamed that output to the Docker client, which sent it
#     to your terminal.
# 
# To try something more ambitious, you can run an Ubuntu container with:
#  $ docker run -it ubuntu bash
# 
# Share images, automate workflows, and more with a free Docker ID:
#  https://hub.docker.com/
# 
# For more examples and ideas, visit:
#  https://docs.docker.com/get-started/
```


## Back to the workshop

[Jump !](./README.md)