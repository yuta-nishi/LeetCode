FROM python:3.10

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update -qq && \
    apt-get install -y \
    curl libopencv-dev lsof git sudo tmux tree vim wget htop && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /var/cache/apk/*

WORKDIR /workdir
