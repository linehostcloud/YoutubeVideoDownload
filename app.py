from pytube import YouTube, Playlist


def download_video(url, output_path=None):
    try:
        print("Downloading video...")
        # Verifica se a URL fornecida é uma playlist do YouTube
        if 'playlist' in url.lower():
            # Se for uma playlist, cria um objeto Playlist do pytube
            playlist = Playlist(url)
            # Itera sobre todos os URLs dos vídeos na playlist
            for video in playlist.video_urls:
                # Cria um objeto YouTube para cada vídeo na playlist
                yt = YouTube(video)
                # Seleciona a melhor resolução disponível para o vídeo
                video_stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by(
                    'resolution').desc().first()
                # Define o caminho de saída do vídeo (nome do arquivo)
                if output_path is None:
                    output_path = video_stream.default_filename
                # Realiza o download do vídeo
                video_stream.download(output_path)
            print("Download da playlist concluído!")
        else:
            # Se não for uma playlist, cria um objeto YouTube para o vídeo único
            yt = YouTube(url)
            # Seleciona a melhor resolução disponível para o vídeo
            video_stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by(
                'resolution').desc().first()
            # Define o caminho de saída do vídeo (nome do arquivo)
            if output_path is None:
                output_path = video_stream.default_filename
            # Realiza o download do vídeo
            video_stream.download(output_path)
            print("Download do vídeo concluído!")
    except Exception as e:
        # Captura e exibe qualquer erro que ocorrer durante o download
        print("Ocorreu um erro durante o download:", e)


if __name__ == "__main__":
    # Solicita ao usuário que insira a URL do vídeo ou da playlist
    video_url = input("Digite a URL do vídeo ou da playlist do YouTube: ")
    # Chama a função de download de vídeo, passando a URL fornecida como argumento
    download_video(video_url)
