# OpenCV Image Manipulation - T.C.C

## Descrição
Este projeto contém um conjunto de funções Python para manipulação de imagens usando a biblioteca OpenCV.

## Instalação

Siga estas etapas para configurar e executar o projeto localmente.

### Pré-requisitos

Certifique-se de ter os seguintes requisitos instalados em sua máquina:

- [Python >= 3.12.2](https://www.python.org/) (você pode verificar a versão com `python --version`)

### Clone o Repositório

```bash
git clone https://github.com/deivomaciel/Worshop-T.C.C.git
```

### Instale o OpenCV

```bash
pip install opencv-python
```

## Funções Disponíveis

### Ler imagem

Lê uma imagem e retorna sua representação como uma matriz de pixels.

Parâmetros:
 - image_path (str): O caminho da imagem a ser lida.

Retorna a matriz de pixels da imagem.

```python
def ler_imagem(image_path):
    imagem = cv2.imread(image_path)
    return imagem
```

### Exibir imagem

Exibe uma imagem em uma janela na tela e aguarda até que uma tecla seja pressionada.

Parâmetros:
 - imagem: A matriz de pixels da imagem a ser exibida.
 - titulo (str): O título da janela que exibe a imagem. Default é 'Imagem'.

```python
def exibir_imagem(imagem, titulo='Imagem'):
    cv2.imshow(titulo, imagem)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
```

### Salvar imagem

Salva uma imagem em um arquivo.

Parâmetros
- nome_imagem (str): O nome do arquivo para salvar a imagem. A extensão do arquivo deve ser incluída
- imagem_editada: A matriz de pixels da imagem a ser salva.

```python
def salvar_imagem(nome_imagem, imagem_editada):
    cv2.imwrite(nome_imagem, imagem_editada)
```

### Redimensionar imagem

Redimensiona uma imagem para uma nova largura e altura.

Parâmetros: 
 - imagem: A matriz de pixels da imagem a ser redimensionada.
 - largura (int): A largura desejada para a imagem redimensionada.
 - altura (int): A altura desejada para a imagem redimensionada.

Retorna a matriz de pixels da imagem redimensionada.

```python
def redimensionar_imagem(imagem, largura, altura):
    nova_imagem = cv2.resize(imagem, (largura, altura))
    return nova_imagem
```

### Aplicar filtro

Aplica um filtro de suavização a uma imagem.

Parâmetros: 
 - imagem: A matriz de pixels da imagem a ser suavizada.

Retorna a matriz de pixels da imagem suavizada.

```python
def aplicar_filtro(imagem):
    imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    imagem_suavizada = cv2.GaussianBlur(imagem_cinza, (5, 5), 0)
    return imagem_suavizada
```

### Corrigir brilho

Corrige o brilho de uma imagem se for muito escuro.

Parâmetros: 
 - imagem: A matriz de pixels da imagem a ser corrigida.

Retorna a matriz de pixels da imagem corrigida.

```python
def corrigir_brilho(imagem):
    image_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    brilho = cv2.mean(image_cinza)[0]
    limiar_de_brilho = 100
    limiar_de_contraste = 1.5

    if brilho > limiar_de_brilho:
        return imagem
    else:
        fator_de_correcao = limiar_de_brilho - brilho
        return cv2.convertScaleAbs(imagem, alpha=limiar_de_contraste, beta=fator_de_correcao)
```
