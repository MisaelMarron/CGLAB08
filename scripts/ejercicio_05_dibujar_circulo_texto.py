import cv2
import os
import sys

sys.path.append(os.path.dirname(__file__))
from utils import cargar_imagen, guardar_imagen

def get_ruta_proyecto():
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def principal():
    base_dir = get_ruta_proyecto()
    
    # 1. Abrir una imagen (idealmente de una persona o animal)
    ruta_entrada = os.path.join(base_dir, "imagenes", "imagen1.jpg")
    img = cargar_imagen(ruta_entrada)
    
    if img is None:
        print(f"Error: No se encontró la imagen en {ruta_entrada}")
        return
        
    # Variables fáciles de modificar para ajustar el dibujo a cualquier imagen
    
    # Coordenadas del centro del círculo
    # Por defecto se coloca en el medio de la imagen, pero se puede ajustar
    # Ejemplo: centro_x = 250, centro_y = 150
    centro_x = int(img.shape[1] / 2)
    centro_y = int(img.shape[0] / 2)
    
    # Configuración del círculo
    radio = 100
    color_circulo = (0, 255, 0)  # Verde en formato BGR
    grosor_circulo = 3
    
    # Configuración del texto
    texto = "Sujeto / Rostro"
    # Posicionar texto justo encima del círculo
    posicion_texto = (centro_x - 80, centro_y - radio - 20)
    fuente = cv2.FONT_HERSHEY_SIMPLEX
    escala_fuente = 1
    color_texto = (0, 255, 255)  # Amarillo en formato BGR
    grosor_texto = 2
    
    # 2. Dibujar un círculo sobre la cara (o centro de imagen)
    cv2.circle(img, (centro_x, centro_y), radio, color_circulo, grosor_circulo)
    
    # 3. Agregar el texto descriptivo
    cv2.putText(img, texto, posicion_texto, fuente, escala_fuente, color_texto, grosor_texto)
    
    # 4. Guardar la imagen final
    ruta_salida = os.path.join(base_dir, "resultados", "imagen_circulo_texto.png")
    guardar_imagen(ruta_salida, img)

if __name__ == "__main__":
    principal()
