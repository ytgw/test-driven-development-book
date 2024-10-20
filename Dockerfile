FROM ubuntu:24.04

RUN apt-get update && apt-get install -y \
    git \
    sudo \
    default-jdk \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

ENV USERNAME='ubuntu'
RUN echo "$USERNAME   ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
USER ${USERNAME}
