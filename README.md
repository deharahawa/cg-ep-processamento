[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-v2.0%20adopted-ff69b4.svg)](code_of_conduct.md)

# Exercício Programa de Computação Gráfica

### Esse programa deve ter os seguintes requisitos:
- Detecção facial
- Algoritmo Gaussian Blur
- Aplicação do blur na região de interesse
- Detecção de blur seu uso de IA
  - Remoção do fundo (para foco na região teve a aplicação
    do blur, de fato)
  - Convolução calculando a variância do Laplaciano
  
#### Como usar a detecção de blur:
``` python roi_blur_detection.py -i <caminho da(s) imagem(s)> -t <limite (padrao 100)> ```
  - Basicamente o script pode receber 2 parâmetros: -i e -t, mas por enquanto só precisa
  informar o -i com o caminho para a pasta com as imagens de rostos anonimizados. 

---
### This program must have these requierments:
```English Below```
- Facial detection
- Gaussian blur algorithm
- Blur application in the region of interest
- Blur detection without AI
  - Remove background
  - Convolution calculating the Laplacian var

