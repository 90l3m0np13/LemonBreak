# 🍋 LemonBreak - Advanced Hash Cracking Tool
![image](https://github.com/90l3m0np13/LemonBreak/blob/main/docs/Portada.jpeg)

# 🔍 ¿Qué es LemonBreak?
LemonBreak es una herramienta especializada en ataques de diccionario inteligente para descifrar hashes de contraseñas. A diferencia de los métodos tradicionales, genera variantes personalizadas basadas en nombres de personas, empresas o sociedades, aumentando exponencialmente las probabilidades de éxito.
# 🧠 Funcionamiento técnico

## 1. Entrada del usuario
Recibe:

Un hash (MD5, SHA1, SHA256, etc.).

Un nombre base (ej: "Julian", "EmpresaXYZ").

## 2. Generación de variantes
Aplica transformaciones lingüísticas y patrones comunes:

Ejemplo para "Julian":
```bash
Variantes = ["Julian", "julian", "JULIAN", "Jul1an", "Jul!an", "Julian2023", "Juli4n", "Julian#"]
````
## Algoritmos utilizados:

-  Leet speak: Sustitución de letras por números/símbolos (a → @, e → 3).

-  Capitalización: Variantes con mayúsculas/minúsculas.

-  Sufijos comunes: Añade números (123), símbolos (!, #) o años (2023).

-  Inserción de caracteres: Introduce símbolos dentro del nombre (Jul_ian).

## 3. Ataque al hash

-  Para cada variante generada:

    -  Calcula su hash (usando el mismo algoritmo que el hash objetivo).

    -  Compara con el hash proporcionado.

    -  Si coinciden, descifra la contraseña.

DIAGRAMA

    A[Hash Objetivo] --> B(Generar variantes)
    B --> C[Calcular hash de "Julian"]
    B --> D[Calcular hash de "Jul1an"]
    B --> E[...]
    C --> F{¿Coincide?}
    D --> F
    E --> F
    F -->|Sí| G[Contraseña encontrada]
    F -->|No| B

# 🎯 Casos de uso típicos

Pentesting ético: Auditorías de seguridad para validar la fortaleza de contraseñas.

Recuperación de acceso: Recuperar contraseñas olvidadas (cuando se conoce información base).

Concienciación: Demostrar cómo combinaciones simples son vulnerables.

# ⚠️ Consideraciones éticas

Uso legal: Solo emplea LemonBreak en sistemas con autorización explícita.

Limitaciones:

Efectividad depende de la calidad del nombre base proporcionado.

No es eficaz contra contraseñas completamente aleatorias.

# 📚 Ejemplo técnico

Hash a descifrar:
```bash
7b3e54970689eeb089e9f949a350198e  (MD5 de "4lv@ro2025")
````
Entrada de LemonBreak:

Nombre base: "Alvaro"

Variantes generadas incluyen: "@lvaro", "4lvar0", "Alv@ro2025", "@lvaro2025"

Resultado: Descubre que "4lv@ro2025" era la contraseña original.

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

# 🌟 ¿Por qué usar LemonBreak?

Eficiencia: Ahorra tiempo generando variantes contextuales (vs. diccionarios genéricos).

Precisión: Optimizado para contraseñas basadas en información personal/empresarial.

Customizable: Puedes ampliar las reglas de generación en el código.

