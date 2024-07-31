import os
import requests
import subprocess
import time

# Variables
FORGE_VERSION = "1.20.1-47.3.0"
FORGE_URL = f"https://maven.minecraftforge.net/net/minecraftforge/forge/{FORGE_VERSION}/forge-{FORGE_VERSION}-installer.jar"
FORGE_INSTALLER = f"forge-{FORGE_VERSION}-installer.jar"
SERVER_JAR = f"forge-{FORGE_VERSION}.jar"

# Función para descargar un archivo
def download_file(url, filename):
    print(f"Descargando {filename}...")
    response = requests.get(url, stream=True)
    response.raise_for_status()
    
    with open(filename, 'wb') as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)
    print(f"{filename} descargado con éxito.")

# Función para ejecutar el instalador de Forge
def run_forge_installer():
    print("Ejecutando el instalador de Forge...")
    # Ejecutar el instalador de Forge
    subprocess.run([
        "java", "-jar", FORGE_INSTALLER, "--installServer"
    ], check=True)
    print("Instalación de Forge completada.")

# Crear archivo eula.txt
def create_eula_file():
    print("Aceptando el EULA...")
    with open("eula.txt", 'w') as file:
        file.write("eula=true\n")
    print("EULA aceptada.")

# Iniciar el servidor de Minecraft
def start_server():
    print("Iniciando el servidor...")
    subprocess.run([
        "java", "-Xmx2G", "-Xms1G", "-jar", SERVER_JAR, "nogui"
    ], check=True)

if __name__ == "__main__":
    # Descargar el instalador de Forge
    download_file(FORGE_URL, FORGE_INSTALLER)

    # Ejecutar el instalador de Forge
    run_forge_installer()

    # Crear el archivo eula.txt
    create_eula_file()

    # Iniciar el servidor de Minecraft
    start_server()
