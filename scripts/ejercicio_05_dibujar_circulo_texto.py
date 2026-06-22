import cv2
import numpy as np
import os
import sys

sys.path.append(os.path.dirname(__file__))
from utils import cargar_imagen, guardar_imagen

def get_ruta_proyecto():
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Variables globales para manejar múltiples figuras
dibujando = False
# Lista de diccionarios, cada uno representa un círculo: {"centro": (x,y), "radio": r, "texto": ""}
figuras = [] 
img_original = None

def eventos_mouse(event, x, y, flags, param):
    global dibujando, figuras
    
    if event == cv2.EVENT_LBUTTONDOWN:
        # Al hacer clic, iniciamos un nuevo círculo y lo añadimos a la lista
        dibujando = True
        figuras.append({"centro": (x, y), "radio": 0, "texto": ""})
        
    elif event == cv2.EVENT_MOUSEMOVE:
        # Al arrastrar, calculamos el radio dinámicamente para la última figura creada
        if dibujando and len(figuras) > 0:
            centro = figuras[-1]["centro"]
            figuras[-1]["radio"] = int(np.sqrt((x - centro[0])**2 + (y - centro[1])**2))
            
    elif event == cv2.EVENT_LBUTTONUP:
        # Al soltar, fijamos el círculo
        dibujando = False
        if len(figuras) > 0:
            centro = figuras[-1]["centro"]
            figuras[-1]["radio"] = int(np.sqrt((x - centro[0])**2 + (y - centro[1])**2))

def principal():
    global img_original, figuras
    base_dir = get_ruta_proyecto()
    
    # Abrir la imagen
    ruta_entrada = os.path.join(base_dir, "imagenes", "imagen3.jpg")
    img_original = cargar_imagen(ruta_entrada)
    
    if img_original is None:
        print(f"Error: No se encontró la imagen en {ruta_entrada}")
        return

    titulo_ventana = 'Dibujo Interactivo - Multiples Circulos'
    cv2.namedWindow(titulo_ventana)
    cv2.setMouseCallback(titulo_ventana, eventos_mouse)
    
    print("\n" + "="*50)
    print(" INSTRUCCIONES INTERACTIVAS MULTIPLES:")
    print(" 1. Haz clic y arrastra para dibujar un círculo.")
    print(" 2. Escribe en tu teclado; el texto irá al ÚLTIMO círculo.")
    print(" 3. Puedes repetir los pasos 1 y 2 para agregar más.")
    print(" 4. Presiona 'u' para deshacer el último círculo.")
    print(" 5. Presiona 'Enter' para guardar la imagen final.")
    print(" 6. Presiona 'Esc' para salir sin guardar.")
    print("="*50 + "\n")
    
    while True:
        img_mostrar = img_original.copy()
        
        # Dibujar todas las figuras almacenadas
        for f in figuras:
            centro = f["centro"]
            radio = f["radio"]
            texto = f["texto"]
            
            # 1. Dibujar el círculo si el radio es mayor a 0
            if radio > 0:
                cv2.circle(img_mostrar, centro, radio, (0, 255, 0), 3)
                
            # 2. Dibujar el texto proporcional al tamaño del círculo
            if texto:
                # Calcular escala proporcional: Base = 1.0 para radio de 100px
                escala = max(0.4, radio / 100.0) # mínimo de 0.4 para que siempre sea legible
                grosor = max(1, int(escala * 3))
                
                # Posicionarlo preferiblemente encima del círculo
                pos_x = int(centro[0] - radio)
                pos_y = int(centro[1] - radio - (15 * escala))
                
                # Si se sale por arriba de la imagen, lo ponemos debajo del círculo
                if pos_y < 30:
                    pos_y = int(centro[1] + radio + (35 * escala))
                    
                cv2.putText(img_mostrar, texto, (pos_x, pos_y), 
                            cv2.FONT_HERSHEY_SIMPLEX, escala, (0, 255, 255), grosor)
                        
        cv2.imshow(titulo_ventana, img_mostrar)
        
        # 3. Capturar el teclado (33 ms de espera)
        tecla = cv2.waitKey(33) & 0xFF
        
        if tecla == 27: # 'Esc'
            print("Saliendo del programa...")
            break
        elif tecla == 13: # 'Enter'
            ruta_salida = os.path.join(base_dir, "resultados", "imagen_multiples_circulos.png")
            guardar_imagen(ruta_salida, img_mostrar)
            print(f"¡Imagen con múltiples círculos guardada correctamente!")
            break
        elif tecla == ord('u') or tecla == ord('U'): # 'u' o 'U' para deshacer
            if len(figuras) > 0:
                figuras.pop()
                print("Último círculo y su texto borrados.")
            else:
                print("No hay círculos para borrar.")
        elif tecla == 8: # 'Backspace' (borrar)
            if len(figuras) > 0:
                figuras[-1]["texto"] = figuras[-1]["texto"][:-1]
        elif 32 <= tecla <= 126: # Caracteres ASCII imprimibles
            if len(figuras) > 0:
                figuras[-1]["texto"] += chr(tecla)
            else:
                print("Dibuja un círculo primero antes de escribir.")

    cv2.destroyAllWindows()

if __name__ == "__main__":
    principal()
