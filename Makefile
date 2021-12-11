init: apt_install pyenv pip_install

pyenv:
	python3 -m venv env

apt_install:
	apt update && apt install -y python3-pip python3-dev build-essential RPi.GPIO

pip_install:
	export CFLAGS="-fcommon"
	. ./env/bin/activate
	pip3 install -r requirements.txt

run:
	python3 main.py
