FROM ubuntu:18.04

RUN apt-get update

RUN apt-get install -y wget && rm -rf /var/lib/apt/lits/*

RUN wget --quiet http://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh \
	&& bash Miniconda3-latest-Linux-x86_64.sh -b -p /miniconda \
	&& rm Miniconda3-latest-Linux-x86_64.sh

ENV PATH=/miniconda/bin:${PATH}


RUN conda update -y conda \
	&& conda install -c anaconda -y python=3.6 \
	&& conda install -c conda-forge rdkit \
	&& conda install -c conda-forge keras \
	&& conda install -c conda-forge h5py=2.10.0 \
	&& conda install -c conda-forge flask \
	&& conda install -c conda-forge glob2 \
	&& conda install -c conda-forge hdf5 \
	&& conda install -c anaconda requests \
	&& conda install tensorflow=2.0


ADD app_demo /web_app/

WORKDIR web_app