# Audio_a_texto
Convierta audio .wav a texto plano sin costo alguno totalmente gratis 

## Instalación

Clona este repositorio:

```bash
git clone https://github.com/sistema200/Audio_a_texto.git
```
Entra a la carpeta: 
```bash
cd Audio_a_texto
```
Ejecuta el instalador En linux:
```bash
bash ./install.sh
```
En Termux:
```bash
bash ./install_solo_termux.sh
```
Ejecuta el Programa:
```bash
./start.sh
```
> [!WARNING]
> **Solo funciona con archivos de audio WAV.**
>
> Puedes usar FFmpeg para convertir un archivo a WAV:
> 
> En linux:
> ```bash 
> sudo apt install ffmpeg -y
> ```
> En termux
> ```bash 
> pkg install ffmpeg -y
> ```
> Luego:
> ```bash
> ffmpeg -i audio.mp3 audio.wav
> ```


