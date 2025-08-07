# Importa todos os módulos da biblioteca moviepy
from moviepy import *

# Importa a biblioteca Path para manipulação de diretórios e caminhos
from pathlib import Path

# Carrega o vídeo original a partir do caminho fornecido
# O prefixo 'r' indica que é uma raw string (evita problemas com barras invertidas)
Video = VideoFileClip(r"C:\Users\guilh\Documents\VScode\Trabalhos\Algoritimo TTK\Movie\Arquivo Exemplo - Link do zap Rei dos demonios\videoplayback.mp4")

# Recorta o vídeo, pegando apenas o trecho entre os segundos 60 e 120
Clip = Video.subclipped(60, 120)

# Define o caminho da pasta onde o novo vídeo será salvo
destination_folder = Path(r"C:\Users\guilh\Documents\VScode\Trabalhos\Algoritimo TTK\Movie\Arquivo Exemplo - Link do zap Rei dos demonios\MovieClip")

# Cria a pasta de destino, incluindo todas as subpastas necessárias, caso não existam
destination_folder.mkdir(parents=True, exist_ok=True)

# Define o caminho completo onde o vídeo cortado será salvo
output_path = destination_folder / "clip.mp4"

# Salva o novo vídeo no caminho especificado, usando o codec de vídeo 'libx264' e de áudio 'aac'
Clip.write_videofile(str(output_path), codec="libx264", audio_codec="aac")
