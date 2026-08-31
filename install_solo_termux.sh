#!/data/data/com.termux/files/usr/bin/bash

pkg update -y
pkg install python -y

python -m venv Convertidor
source Convertidor/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
deactivate

echo 'source Convertidor/bin/activate
python audio_a_texto.py
deactivate' > start.sh

chmod +x start.sh
