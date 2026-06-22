import cv2
import numpy as np
import os
import sys

sys.path.append(os.path.dirname(__file__))
from utils import cargar_imagen, guardar_imagen

def get_ruta_proyecto():
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def principal():
    base_dir = get_ruta_proyecto()
    
    # Abrir una imagen para la aplicación interactiva
    ruta_entrada = os.path.join(base_dir, "imagenes", "imagen2.jpg")
    img = cargar_imagen(ruta_entrada)
    
    if img is None:
        print(f"Error: No se encontró la imagen en {ruta_entrada}")
        return
        
    # Variables booleanas para controlar qué canales se muestran
    mostrar_r = True
    mostrar_g = True
    mostrar_b = True
    
    titulo_ventana = "Visualizador Interactivo de Canales"
    
    print("\n" + "="*40)
    print(" INSTRUCCIONES DEL VISUALIZADOR")
    print("="*40)
    print(" Presiona las siguientes teclas en la ventana:")
    print("  [r] : Activar/Desactivar canal ROJO")
    print("  [g] : Activar/Desactivar canal VERDE")
    print("  [b] : Activar/Desactivar canal AZUL")
    print("  [s] : Guardar captura actual")
    print("  [q] : Salir de la aplicacion")
    print("="*40 + "\n")
    
    while True:
        # Copiar la imagen para no sobreescribir la original y tener siempre datos limpios
        img_mostrar = img.copy()
        
        # Apagar los canales modificando su matriz a 0 (negro/ausencia de luz de ese color)
        # Recordatorio: En OpenCV el índice de colores es BGR: 0=Azul, 1=Verde, 2=Rojo
        if not mostrar_b:
            img_mostrar[:, :, 0] = 0
        if not mostrar_g:
            img_mostrar[:, :, 1] = 0
        if not mostrar_r:
            img_mostrar[:, :, 2] = 0
            
        # Mostrar imagen resultante
        cv2.imshow(titulo_ventana, img_mostrar)
        
        # Esperar la entrada del teclado y obtener su valor ASCII
        tecla = cv2.waitKey(33) & 0xFF
        
        # Actuar en función de la tecla presionada
        if tecla == ord('r'):
            mostrar_r = not mostrar_r
            print(f"-> Canal Rojo:  {'ACTIVO' if mostrar_r else 'INACTIVO'}")
        elif tecla == ord('g'):
            mostrar_g = not mostrar_g
            print(f"-> Canal Verde: {'ACTIVO' if mostrar_g else 'INACTIVO'}")
        elif tecla == ord('b'):
            mostrar_b = not mostrar_b
            print(f"-> Canal Azul:  {'ACTIVO' if mostrar_b else 'INACTIVO'}")
        elif tecla == ord('s'):
            ruta_guardado = os.path.join(base_dir, "resultados", "captura_visualizador_canales.png")
            guardar_imagen(ruta_guardado, img_mostrar)
            print(f"-> ¡Captura guardada!")
        elif tecla == ord('q'):
            print("-> Saliendo del visualizador...")
            break

    # Cerrar todas las ventanas de OpenCV
    cv2.destroyAllWindows()

if __name__ == "__main__":
    principal()
