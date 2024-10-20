FROM ubuntu:24.04

RUN apt-get update && apt-get install -y \
    git \
    sudo \
    default-jdk \
    # gradleをインストールするためのsdkmanのインストールに必要
    curl zip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

ENV USERNAME='ubuntu'
RUN echo "$USERNAME   ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
USER ${USERNAME}

# gradleをインストールするためのsdkmanのインストール
RUN curl -s "https://get.sdkman.io" | bash

# gradleのインストール
RUN /bin/bash -c "source ${HOME}/.sdkman/bin/sdkman-init.sh && sdk install gradle 8.10.2"

# gitのタブ補完
RUN echo 'source /usr/share/bash-completion/completions/git' >> ~/.bashrc
