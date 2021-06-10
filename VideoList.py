# Biblioteca
import PIL
import cv2
import numpy as np
from PIL import Image
#max_allowed_packet=1073741824;

# listas
listaIMG = []
#IMG = []

#video
a = cv2.VideoCapture('Basler_acA640-120uc__21379673__20201213_080543930.avi')

# imagem para comparar
c = cv2.imread("frame10.jpg")
                #c = cv2.cvtColor(c, cv2.COLOR_RGB2BGR)
c = np.resize(c,(658,492))


emLoop, image = a.read()
count = 0
emLoop = True

while (emLoop):
    a.set(cv2.CAP_PROP_POS_MSEC, (count * 1000)) #Limitador de frames (Para testes)
    emLoop, image = a.read()
                    #cv2.imwrite("frame%d.jpg" % count, image) #SALVAR IMAGENS
    image = np.resize(image,(658, 492))
                    #image = cv2.cvtColor(image, cv2.COLOR_BGR2)
    listaIMG.append(image)
    try:
        np.testing.assert_array_equal(listaIMG[count], c) #salvar imagem apenas quando forem iguais (PROBLEMA)
        res = True
        cv2.imwrite("frameVideo%d.jpg" % count, image)
        print("Objeto localizado, imagem salva como: frame%d.jpg" % count, image)
        # IMG.append(image) ideia - salvar imagem que deram igualdade em outra lista, para fazer comparações pixel a pixel
    except AssertionError as err:
        res = False


    if cv2.waitKey(10) == 27:
        break
    count += 1


    _, frame = a.read()

    # Escrevo um texto orientativo para o usuário saber como sair
    cv2.putText(frame, "Pressione ESC para encerrar", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)
    cv2.imshow("video", frame)

    k = cv2.waitKey(100)

    # Caso se pressione a tecla ESC
    if k == 27:
        emLoop = False
    if count >= 60:
        break


print(listaIMG[10])
print("--------------------------------------\n")
print(c)
#print(type(c))

a.release()