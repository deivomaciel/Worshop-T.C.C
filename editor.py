import cv2

def ler_imagem(image_path):
    '''
    Lê uma imagem e retorna sua representação como uma matriz de pixels.

    Parâmetros:
        image_path (str): O caminho da imagem a ser lida.

    Retorna:
        A matriz de pixels da imagem.
    '''
    imagem = cv2.imread(image_path)
    return imagem
    

def exibir_imagem(imagem, titulo='Imagem'):
    '''
    Exibe uma imagem em uma janela na tela e aguarda até que uma tecla seja pressionada.

    Parâmetros:
        imagem: A matriz de pixels da imagem a ser exibida.
        titulo (str): O título da janela que exibe a imagem. Default é 'Imagem'.
    '''
    cv2.imshow(titulo, imagem)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def salvar_imagem(nome_imagem, imagem_editada):
    '''
    Salva uma imagem em um arquivo.

    Parâmetros:
        nome_imagem (str): O nome do arquivo para salvar a imagem. A extensão do arquivo deve ser incluída.
        imagem_editada: A matriz de pixels da imagem a ser salva.
    '''
    cv2.imwrite(nome_imagem, imagem_editada)


def redimensionar_imagem(imagem, largura, altura):
    '''
    Redimensiona uma imagem para uma nova largura e altura.

    Parâmetros:
        imagem: A matriz de pixels da imagem a ser redimensionada.
        largura (int): A largura desejada para a imagem redimensionada.
        altura (int): A altura desejada para a imagem redimensionada.

    Retorna:
        A matriz de pixels da imagem redimensionada.
    '''
    nova_imagem = cv2.resize(imagem, (largura, altura))
    return nova_imagem


def aplicar_filtro(imagem):
    '''
    Aplica um filtro de suavização a uma imagem.

    Parâmetros:
        imagem: A matriz de pixels da imagem a ser suavizada.

    Retorna:
        A matriz de pixels da imagem suavizada.
    '''
    imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    imagem_suavizada = cv2.GaussianBlur(imagem_cinza, (5, 5), 0)
    return imagem_suavizada


def corrigir_brilho(imagem):
    '''
    Corrige o brilho de uma imagem se for muito escuro.

    Parâmetros:
        imagem: A matriz de pixels da imagem a ser corrigida.

    Retorna:
        A matriz de pixels da imagem corrigida.
    '''
    image_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    brilho = cv2.mean(image_cinza)[0]
    limiar_de_brilho = 100
    limiar_de_contraste = 1.5

    if brilho > limiar_de_brilho:
        return imagem
    else:
        fator_de_correcao = limiar_de_brilho - brilho
        return cv2.convertScaleAbs(imagem, alpha=limiar_de_contraste, beta=fator_de_correcao)


imagem = ler_imagem('./Assets/porsche_cayenne.png')
exibir_imagem(imagem)

imagem_redimencionada = redimensionar_imagem(imagem, 200, 200)
exibir_imagem(imagem_redimencionada)
salvar_imagem('redimencionada.png', imagem_redimencionada)


imagem_com_filtro = aplicar_filtro(imagem)
exibir_imagem(imagem_com_filtro)
salvar_imagem('com_filtro.png', imagem_com_filtro)


imagem_corrigida = corrigir_brilho(imagem)
exibir_imagem(imagem_corrigida)
salvar_imagem('corrigida.png', imagem_corrigida)