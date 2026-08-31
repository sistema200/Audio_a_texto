#!/bin/bash
sudo apt install python3.13-venv
python3 -m venv Convertidor
source Convertidor/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
deactivate
echo """source Convertidor/bin/activate
python3 audio_a_texto.py
deactivate"""> start.sh
chmod +x start.sh
#rm -rf install.sh
