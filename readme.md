## Download de Vídeos do YouTube com Python usando Pytube

---

![ShielddoProjeto](https://img.shields.io/badge/Projeto-YoutubeVideoDownload-ff0000.svg?style=for-the-badge)
![ShielddoProjeto](https://img.shields.io/badge/Versão-1.0-34bf49.svg?style=for-the-badge)
![ShielddoProjeto](https://img.shields.io/badge/Linguagem-Python-efdf00.svg?style=for-the-badge)
![ShielddoProjeto](https://img.shields.io/github/last-commit/linehostcloud/YoutubeVideoDownload?style=for-the-badge)

---

#### Introdução:

Este é um pequeno script em Python que permite baixar vídeos do YouTube, bem como playlists, utilizando a biblioteca Pytube. 
O Pytube é uma biblioteca Python simples e eficaz para baixar vídeos do YouTube.

---

#### Instruções de Uso:

1. Certifique-se de ter o Python instalado em seu sistema. Você pode baixar e instalar o Python a partir do site oficial: [Python.org](https://www.python.org/).
2. nstale a biblioteca Pytube. Você pode instalar o Pytube usando pip, o gerenciador de pacotes Python. Execute o seguinte comando no terminal ou prompt de comando:

```python
pip install pytube
```
3. Após fazer a instalação, execulte o seguinte comando:

```python
python app.py
```
4. Executando o script Python. Você será solicitado a inserir a URL do vídeo ou da playlist do YouTube que deseja baixar.
5. Aguarde enquanto o script faz o download do vídeo ou da playlist. 
6. O vídeo será salvo na mesma pasta do script Python.

---

#### Explicação do Código:

- O código começa importando as bibliotecas necessárias, incluindo YouTube e Playlist do Pytube.
- Em seguida, define-se uma função download_video que aceita uma URL do YouTube como entrada.
- Dentro dessa função, o código verifica se a URL fornecida é para uma playlist. Se for uma playlist, itera sobre todos os vídeos na playlist e os baixa individualmente.
- Se a URL não for de uma playlist, o código baixa o vídeo único especificado pela URL.
- O código utiliza a função download() da classe YouTube do Pytube para baixar o vídeo.
- Eventuais erros durante o processo de download são capturados e exibidos.
- Por fim, no bloco `if __name__ == "__main__":`, o código solicita ao usuário que insira a URL do vídeo ou da playlist do YouTube e chama a função download_video com a URL fornecida.

---

#### Observação:

Certifique-se de que o vídeo ou a playlist que você está tentando baixar não esteja protegido por direitos autorais ou sujeito a restrições de uso. O uso deste script é de responsabilidade do usuário.
