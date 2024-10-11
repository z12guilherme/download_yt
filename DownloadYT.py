import yt_dlp

def baixar_video(url):
    # Definir opções de download
    ydl_opts = {
        'format': 'best',  # Baixa a melhor qualidade disponível
        'outtmpl': '%(title)s.%(ext)s',  # Nome do arquivo de saída
    }

    # Baixar o vídeo
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    url = input("Digite a URL do vídeo que deseja baixar: ")
    baixar_video(url)
