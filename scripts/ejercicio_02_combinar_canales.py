import cv2
import os
import sys

sys.path.append(os.path.dirname(__file__))
from utils import cargar_imagen, guardar_imagen

def get_ruta_proyecto():
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def principal():
    base_dir = get_ruta_proyecto()
    
    # 1. Usar las tres imágenes ya redimensionadas del ejercicio anterior
    ruta1 = os.path.join(base_dir, "resultados", "imagen1_redimensionada.png")
    ruta2 = os.path.join(base_dir, "resultados", "imagen2_redimensionada.png")
    ruta3 = os.path.join(base_dir, "resultados", "imagen3_redimensionada.png")
    
    img1 = cargar_imagen(ruta1)
    img2 = cargar_imagen(ruta2)
    img3 = cargar_imagen(ruta3)
    
    if img1 is None or img2 is None or img3 is None:
        print("Error: No se encontraron todas las imágenes redimensionadas.")
        print("Asegúrate de ejecutar primero el script 'ejercicio_01_redimensionar.py'.")
        return
        
    # Explicación:
    # OpenCV por defecto lee y trabaja con las imágenes en formato BGR (Blue, Green, Red).
    # Esto significa que el canal 0 es Azul, el canal 1 es Verde y el canal 2 es Rojo.
    # Para trabajar con canales individuales, usamos cv2.split para dividirlos en matrices separadas.
    b1, g1, r1 = cv2.split(img1)
    b2, g2, r2 = cv2.split(img2)
    b3, g3, r3 = cv2.split(img3)
    
    # 2. Crear una nueva imagen usando:
    # - Canal ROJO de la primera imagen (r1)
    # - Canal VERDE de la segunda imagen (g2)
    # - Canal AZUL de la tercera imagen (b3)
    
    # Utilizamos cv2.merge para recombinar canales.
    # Es VITAL mantener el orden B, G, R porque es como OpenCV va a interpretar la imagen combinada.
    imagen_combinada = cv2.merge((b3, g2, r1))
    
    # 3. Guardar la imagen final
    ruta_salida = os.path.join(base_dir, "resultados", "imagen_canales_combinados.png")
    guardar_imagen(ruta_salida, imagen_combinada)

if __name__ == "__main__":
    principal()
