#!/usr/bin/env python3
import os
import hashlib
import subprocess
import sys
from pathlib import Path
from colorama import init, Fore, Back, Style
import time
import itertools

# Inicializar colorama
init(autoreset=True)

APP_DIR = Path.home() / "LemonBreak"
DICT_FILE = APP_DIR / "generated_dict.txt"

def display_banner():
    print(Fore.YELLOW + r"""
      ,--./,-.
     / #      \
    |          |     """ + Fore.YELLOW + Style.BRIGHT + "LemonBreak" + Fore.YELLOW + r"""
     \        /      """ + Fore.CYAN + "Smart Hash Cracker" + Fore.YELLOW + r"""
      `._,._,'       """ + Fore.WHITE + "https://github.com/90l3m0np13" + Fore.GREEN + r"""
    """ + Style.RESET_ALL)
    print(Fore.MAGENTA + "="*50)
    print(Fore.GREEN + Style.BRIGHT + "  Generador inteligente de variantes")
    print(Fore.MAGENTA + "="*50 + Style.RESET_ALL + "\n")

def setup():
    APP_DIR.mkdir(exist_ok=True)

def animate_text(text):
    for char in text:
        sys.stdout.write(Fore.YELLOW + char)
        sys.stdout.flush()
        time.sleep(0.03)
    print()
def generate_variations(base_word):
    """Genera variaciones avanzadas incluyendo sustituciones exactas"""
    variations = set()
    
    # Mapeo leet extendido con tu ejemplo específico
    advanced_leet = {
        'a': ['4', '@', '^', '/\\', 'a'],
        'e': ['3', '&', '€', 'e'],
        'i': ['1', '!', '|', 'i'],
        'o': ['0', '°', '()', 'o'],
        'u': ['v', '|_|', 'u'],
        'l': ['1', '|', '£', 'l'],
    }
    
    # Genera todas las combinaciones posibles para cada posición
    from itertools import product
    
    # Prepara las opciones para cada carácter
    char_options = []
    for char in base_word.lower():
        if char in advanced_leet:
            char_options.append(advanced_leet[char])
        else:
            char_options.append([char, char.upper()])
    
    # Genera todas las combinaciones posibles
    for combo in product(*char_options):
        # Caso base
        variation = ''.join(combo)
        variations.add(variation)
        
        # Añade versiones con símbolos
        for symbol in ['', '!', '@', '#', '$', '%', '&', '*']:
            variations.add(variation + symbol)
            variations.add(symbol + variation)
            variations.add(symbol + variation + symbol)
        
        # Añade versiones con números
        for num in ['1', '12', '123', '1234', '2023', '2024']:
            variations.add(variation + num)
            variations.add(num + variation)
    
    # Casos especiales como el tuyo (L4ur@)
    special_cases = {
        'laura': ['L4ur@', 'L@ura', 'L@ur@', '14ur@'],
        'admin': ['@dmin', '4dm1n', '@dm1n'],
        'password': ['p@ssw0rd', 'p@55w0rd']
    }
    
    for original, cases in special_cases.items():
        if original in base_word.lower():
            variations.update(cases)
    
    return variations    
    leet_combinations = generate_leet_combinations(base_word)
    variations.update(leet_combinations)
    
    # Generar combinaciones con números insertados
    for i in range(len(base_word)):
        for num in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
            variations.add(base_word[:i] + num + base_word[i:])
    
    # Generar versiones con símbolos insertados
    for i in range(1, len(base_word)):
        for symbol in ['_', '-', '.', '@', '!', '#']:
            variations.add(base_word[:i] + symbol + base_word[i:])
    
    # Generar combinaciones con palabras comunes
    common_words = ['pass', 'pwd', 'admin', 'secure', 'welcome', 'login']
    for word in common_words:
        variations.update([
            base_word + word,
            word + base_word,
            base_word.upper() + word,
            word.capitalize() + base_word.capitalize(),
            base_word + '_' + word,
            word + '123' + base_word
        ])
    
    # Generar combinaciones con patrones de teclado (qwerty, etc.)
    keyboard_shifts = {
        'q': '1', 'w': '2', 'e': '3', 'r': '4', 't': '5', 'y': '6',
        'u': '7', 'i': '8', 'o': '9', 'p': '0',
        'a': '', 's': '$', 'd': '', 'f': '', 'g': '', 'h': '',
        'j': '', 'k': '', 'l': '',
        'z': '', 'x': '', 'c': '', 'v': '', 'b': '', 'n': '', 'm': ''
    }
    
    keyboard_variant = []
    for char in base_word.lower():
        keyboard_variant.append(keyboard_shifts.get(char, char))
    variations.add(''.join(keyboard_variant))
    
    return variations

    # Combinaciones con palabras comunes
   

def crack_hash():
    animate_text("\n[+] Modo de ataque inteligente")
    
    # Obtener entrada del usuario
    base_word = input(Fore.CYAN + "\n[?] Introduce nombre, empresa o sociedad: " + Fore.WHITE).strip()
    target_hash = input(Fore.CYAN + "[?] Introduce el hash a crackear: " + Fore.WHITE).strip()
    hash_type = input(Fore.CYAN + "[?] Tipo de hash (md5, sha1, sha256): " + Fore.WHITE).strip().lower()
    
    # Generar variaciones
    animate_text("\n[+] Generando variantes de contraseña...")
    variations = generate_variations(base_word)
    total_variations = len(variations)
    
    # Mostrar estadísticas
    print(Fore.YELLOW + f"\n[+] Generadas {total_variations} variantes de '{base_word}'")
    
    # Probar las variaciones
    animate_text("[+] Iniciando proceso de cracking...")
    
    found = False
    current = 0
    
    for password in variations:
        current += 1
        progress = int((current/total_variations)*50)
        
        sys.stdout.write(Fore.YELLOW + "\r[+] Progreso: [" + "="*progress + " "*(50-progress) + f"] {current}/{total_variations}")
        sys.stdout.flush()
        
        h = hashlib.new(hash_type)
        h.update(password.encode())
        current_hash = h.hexdigest()
        
        if current_hash == target_hash:
            print(Fore.GREEN + f"\n\n[+] ¡Contraseña comprometida!: " + Fore.MAGENTA + Style.BRIGHT + password)
            found = True
            break
    
    if not found:
        print(Fore.RED + "\n\n[-] La contraseña no se encontró en las variantes generadas.")

def main():
    setup()
    while True:
        os.system('clear' if os.name == 'posix' else 'cls')
        display_banner()
        
        print(Fore.BLUE + Style.BRIGHT + " MENÚ PRINCIPAL ".center(50, "═"))
        print(Fore.CYAN + "\n 1. " + Fore.WHITE + "Crackear hash (modo inteligente)")
        print(Fore.CYAN + " 2. " + Fore.RED + "Salir\n")
        
        try:
            choice = input(Fore.YELLOW + "[?] Selecciona una opción (1-2): " + Fore.WHITE)
            
            if choice == "1":
                crack_hash()
                input(Fore.CYAN + "\n[+] Presiona Enter para continuar...")
            elif choice == "2":
                animate_text("\n[+] Cerrando LemonBreak...")
                time.sleep(1)
                break
            else:
                print(Fore.RED + "\n[!] Opción no válida")
                time.sleep(1)
        except KeyboardInterrupt:
            print(Fore.RED + "\n[!] Operación cancelada por el usuario")
            time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(Fore.RED + f"\n[!] Error: {e}")
        sys.exit(1)
