#!/bin/bash
echo "[+] Instalando LemonBreak..."
sudo apt install -y python3 python3-pip git
git clone https://github.com/tuusuario/LemonBreak.git
cd LemonBreak
pip3 install -r requirements.txt
chmod +x src/lemonbreak.py
sudo cp src/lemonbreak.py /usr/local/bin/lemonbreak
echo "[+] Instalación completada. Ejecuta con: lemonbreak"
