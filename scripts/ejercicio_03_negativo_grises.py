import cv2
import os
import sys

sys.path.append(os.path.dirname(__file__))
from utils import cargar_imagen, guardar_imagen

def get_ruta_proyecto():
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def principal():
    base_dir = get_ruta_proyecto()
    
    # 1. Abrir la imagen combinada del ejercicio anterior
    ruta_entrada = os.path.join(base_dir, "resultados", "imagen_canales_combinados.png")
    img = cargar_imagen(ruta_entrada)
    
    if img is None:
        print("Error: No se encontró la imagen combinada.")
        print("Asegúrate de ejecutar primero el script 'ejercicio_02_combinar_canales.py'.")
        return
        
    # 2. Convertirla a negativo invirtiendo los valores de los píxeles
    # Fórmula del negativo: 255 - pixel
    # Como los píxeles (uint8) toman valores de 0 a 255, si el píxel es oscuro (cercano a 0), 
    # la resta resultará en un valor alto (claro). Y si el píxel original es claro, la resta será baja.
    imagen_negativa = 255 - img
    
    # 3. Guardar el negativo
    ruta_negativo = os.path.join(base_dir, "resultados", "imagen_negativa.png")
    guardar_imagen(ruta_negativo, imagen_negativa)
    
    # 4. Convertir el negativo a escala de grises
    # Utilizamos la función cvtColor para cambiar el espacio de color de BGR a Grayscale
    imagen_grises = cv2.cvtColor(imagen_negativa, cv2.COLOR_BGR2GRAY)
    
    # 5. Guardar la imagen en escala de grises
    ruta_grises = os.path.join(base_dir, "resultados", "imagen_negativa_grises.png")
    guardar_imagen(ruta_grises, imagen_grises)

if __name__ == "__main__":
    principal()
