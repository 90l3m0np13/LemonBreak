# 🍋 LemonBreak - Advanced Hash Cracking Tool


Herramienta inteligente para cracking de hashes que genera variantes de contraseña automáticamente.

# 🔥 Features
- Generación automática de variantes (leet speak, mayúsculas, símbolos)
- Soporte para MD5, SHA1, SHA256
- Interfaz interactiva con colores
- No requiere diccionarios externos

# 🚀 Instalación en Kali Linux
## 1. Actualiza el sistema e instala dependencias
```bash
sudo apt update && sudo apt install -y python3 python3-pip git
````
## 2. Clona el repositorio
```bash
git clone https://github.com/90l3m0np13/LemonBreak.git
````
## 3. Entra al directorio del proyecto
```bash
cd LemonBreak
````
## 4. Instala los requisitos de Python
```bash
pip3 install -r requirements.txt
````
## 5. Da permisos de ejecución al script
```bash
chmod +x src/lemonbreak.py
````
## 6. Crea un enlace simbólico para ejecutarlo desde cualquier lugar
```bash
sudo ln -s $(pwd)/src/lemonbreak.py /usr/local/bin/lemonbreak
```
## 7. Abrir la aplicación con python
```bash
python3 ~/LemonBreak.py
````
![imagen](https://github.com/90l3m0np13/LemonBreak/blob/main/docs/App.png)

# 🚨 Requisitos
Kali Linux (o cualquier distro basada en Debian)

Python 3.8+

Conexión a internet para la instalación
