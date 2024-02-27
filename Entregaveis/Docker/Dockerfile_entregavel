FROM ubuntu:20.04

# Instalação do tmux e htop
RUN apt-get update && \
    apt-get install -y tmux htop && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /dir1/dir2/dir3

CMD ["tmux"]
