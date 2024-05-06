# OpenCV Image Manipulation - T.C.C

## Descrição
Este projeto contém um conjunto de funções Python para manipulação de imagens usando a biblioteca OpenCV.

## Instalação

Siga estas etapas para configurar e executar o projeto localmente.

### Pré-requisitos

Certifique-se de ter os seguintes requisitos instalados em sua máquina:

- [Python >= 3.12.2](https://www.python.org/) (você pode verificar a versão com `python --version`)

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

## Código completo

```python
import cv2

def ler_imagem(image_path):
    imagem = cv2.imread(image_path)
    return imagem
    

def exibir_imagem(imagem, titulo='Imagem'):
    cv2.imshow(titulo, imagem)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def salvar_imagem(nome_imagem, imagem_editada):
    cv2.imwrite(nome_imagem, imagem_editada)


def redimensionar_imagem(imagem, largura, altura):
    nova_imagem = cv2.resize(imagem, (largura, altura))
    return nova_imagem


def aplicar_filtro(imagem):
    imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    imagem_suavizada = cv2.GaussianBlur(imagem_cinza, (5, 5), 0)
    return imagem_suavizada


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

## Exemplos de uso

### Exibir uma imagem

```python
imagem = ler_imagem('./Assets/dog.jpg')
exibir_imagem(imagem)
```

### Redimencionar uma imagem 
```python
imagem = ler_imagem('./Assets/dog.jpg')
imagem_redimencionada = redimensionar_imagem(imagem, 200, 200)
exibir_imagem(imagem_redimencionada)
```

<table>
  <tr style="border: none;">
    <td>
     <h3>Imagem original</h3>
     <img src="https://github.com/deivomaciel/Worshop-T.C.C/assets/31144383/74ac8008-40bc-472e-b855-12a172f75303" alt="Imagem 1">
    </td>
    <td>
     <h3>Imagem original</h3>
     <img src="https://github.com/deivomaciel/Worshop-T.C.C/assets/31144383/6daf2e36-ecb1-420e-9c8a-967ab9643dde" alt="Imagem 2">
    </td>
  </tr>
</table>


### Aplicar filtro a uma imagem

```python
imagem = ler_imagem('./Assets/dog.jpg')
imagem_com_filtro = aplicar_filtro(imagem)
exibir_imagem(imagem_com_filtro)
```

<table>
  <tr style="border: none;">
    <td>
     <h3>Imagem original</h3>
     <img src="https://github.com/deivomaciel/Worshop-T.C.C/assets/31144383/74ac8008-40bc-472e-b855-12a172f75303" alt="Imagem 1">
    </td>
    <td>
     <h3>Imagem com filtro</h3>
     <img src="https://github.com/deivomaciel/Worshop-T.C.C/assets/31144383/a906b621-9e2b-4907-9049-bcbd3c0b499f" alt="Imagem 2">
    </td>
  </tr>
</table>


### Corrigir brilho de uma imagem

```python
imagem = ler_imagem('./Assets/dog.jpg')
imagem_corrigida = corrigir_brilho(imagem)
exibir_imagem(imagem_corrigida)
```

<table>
  <tr style="border: none;">
    <td>
     <h3>Imagem original</h3>
     <img src="https://github.com/deivomaciel/Worshop-T.C.C/assets/31144383/74ac8008-40bc-472e-b855-12a172f75303" alt="Imagem 1">
    </td>
    <td>
     <h3>Imagem com brilho corrigido</h3>
     <img src="https://github.com/deivomaciel/Worshop-T.C.C/assets/31144383/396f1fa5-0cc2-40c9-b6b4-56427228b3dd" alt="Imagem 2">
    </td>
  </tr>
</table>

