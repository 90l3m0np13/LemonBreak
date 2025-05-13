# 🍋 LemonBreak - Advanced Hash Cracking Tool

![Lemon Logo](assets/lemon_logo.png)

Herramienta inteligente para cracking de hashes que genera variantes de contraseña automáticamente.

## 🔥 Features
- Generación automática de variantes (leet speak, mayúsculas, símbolos)
- Soporte para MD5, SHA1, SHA256
- Interfaz interactiva con colores
- No requiere diccionarios externos

## 🚀 Instalación en Kali Linux
```bash
sudo apt update && sudo apt install -y python3 python3-pip git
git clone https://github.com/tuusuario/LemonBreak.git
cd LemonBreak
pip3 install -r requirements.txt
chmod +x src/lemonbreak.py
sudo ln -s $(pwd)/src/lemonbreak.py /usr/local/bin/lemonbreak
```

## 💻 Uso básico
```bash
lemonbreak
```
