import cv2
import numpy as np
import os
import sys

sys.path.append(os.path.dirname(__file__))
from utils import guardar_imagen

def get_ruta_proyecto():
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ---- Variables Globales ----
dibujando = False
modo = 'l' # Modos: 'l' (línea), 'r' (rectángulo), 'c' (círculo)
ix, iy = -1, -1
img = None
historial = []

def guardar_estado_lienzo():
    """Guarda el estado actual del lienzo para permitir la opción de deshacer."""
    global img, historial
    historial.append(img.copy())
    # Limitar el historial para no saturar memoria
    if len(historial) > 15:
        historial.pop(0)

def deshacer():
    """Restaura el lienzo al último estado guardado."""
    global img, historial
    if len(historial) > 0:
        img = historial.pop()

def eventos_mouse(event, x, y, flags, param):
    """Función de callback para capturar eventos del mouse de OpenCV."""
    global ix, iy, dibujando, modo, img
    
    if event == cv2.EVENT_LBUTTONDOWN:
        # Clic izquierdo presionado: empieza el dibujo
        dibujando = True
        ix, iy = x, y
        guardar_estado_lienzo() # Guardamos la imagen justo antes de rayarla
        
    elif event == cv2.EVENT_LBUTTONUP:
        # Clic izquierdo soltado: finaliza el dibujo de la figura actual
        dibujando = False
        if modo == 'r':
            cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), 2)
        elif modo == 'c':
            radio = int(np.sqrt((x - ix)**2 + (y - iy)**2))
            cv2.circle(img, (ix, iy), radio, (0, 0, 255), 2)
        elif modo == 'l':
            cv2.line(img, (ix, iy), (x, y), (255, 0, 0), 2)
            
    elif event == cv2.EVENT_MOUSEMOVE and dibujando:
        # Moviendo el mouse mientras se mantiene presionado el clic izquierdo
        # Mostramos una vista previa de la figura
        img_temp = img.copy()
        if modo == 'r':
            cv2.rectangle(img_temp, (ix, iy), (x, y), (0, 255, 0), 2)
        elif modo == 'c':
            radio = int(np.sqrt((x - ix)**2 + (y - iy)**2))
            cv2.circle(img_temp, (ix, iy), radio, (0, 0, 255), 2)
        elif modo == 'l':
            cv2.line(img_temp, (ix, iy), (x, y), (255, 0, 0), 2)
        # Mostrar la vista previa temporal
        cv2.imshow('Lienzo Interactivo', img_temp)

def principal():
    global img, modo
    
    # 1. Crear un lienzo en blanco (imagen negra)
    img = np.zeros((600, 800, 3), np.uint8)
    
    print("\n" + "="*40)
    print(" DIBUJO INTERACTIVO")
    print("="*40)
    print(" Usa el mouse (clic sostenido) para dibujar.")
    print(" Controles de teclado:")
    print("  [l] : Modo Línea (Azul)")
    print("  [r] : Modo Rectángulo (Verde)")
    print("  [c] : Modo Círculo (Rojo)")
    print("  [u] : Deshacer último trazo")
    print("  [s] : Guardar dibujo final")
    print("  [q] : Salir")
    print("="*40 + "\n")
    
    # Crear ventana y asignar los eventos del mouse
    cv2.namedWindow('Lienzo Interactivo')
    cv2.setMouseCallback('Lienzo Interactivo', eventos_mouse)
    
    while True:
        # Si no se está dibujando y moviendo, mostrar el lienzo base
        if not dibujando:
            cv2.imshow('Lienzo Interactivo', img)
            
        tecla = cv2.waitKey(20) & 0xFF
        
        # 2. Gestionar controles del teclado
        if tecla == ord('l'):
            modo = 'l'
            print("-> Modo cambiado a: LÍNEA")
        elif tecla == ord('r'):
            modo = 'r'
            print("-> Modo cambiado a: RECTÁNGULO")
        elif tecla == ord('c'):
            modo = 'c'
            print("-> Modo cambiado a: CÍRCULO")
        elif tecla == ord('u'):
            deshacer()
            print("-> Trazo deshecho.")
        elif tecla == ord('s'):
            base_dir = get_ruta_proyecto()
            ruta_salida = os.path.join(base_dir, "resultados", "dibujo_final.png")
            guardar_imagen(ruta_salida, img)
            print(f"-> ¡Dibujo guardado!")
        elif tecla == ord('q'):
            print("-> Saliendo del lienzo...")
            break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    principal()
