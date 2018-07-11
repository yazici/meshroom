ARG CUDA_TAG=9.2-devel
FROM alicevision:$CUDA_TAG
LABEL maintainer="AliceVision Team alicevision@googlegroups.com"

# use CUDA_TAG to select the image version to use
# see https://hub.docker.com/r/nvidia/cuda/
#
# For example, to create a ubuntu 16.04 with cuda 8.0 for development, use
# export CUDA_TAG=8.0-devel
# docker build --build-arg CUDA_TAG=$CUDA_TAG --tag meshroom:$CUDA_TAG .
#
# then execute with nvidia docker (https://github.com/nvidia/nvidia-docker/wiki/Installation-(version-2.0))
# docker run -it --runtime=nvidia meshroom:$CUDA_TAG

RUN apt-get clean && apt-get update && apt-get install -y --no-install-recommends python3-dev python3-pip python3-setuptools python3-wheel \
      && rm -rf /var/lib/apt/lists/*

RUN pip3 install --upgrade pip

COPY . /opt/meshroom
WORKDIR /opt/meshroom

# this is not necessary if GUI is not used
# RUN pip install -r requirements.txt -r dev_requirements.txt

# install psutil, normally not necessary if requirements.txt is used.
RUN pip3 install psutil

env PYTHONPATH=/opt/meshroom/bin:$PYTHONPATH
