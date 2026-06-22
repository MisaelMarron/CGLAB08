import cv2
import os
import sys

sys.path.append(os.path.dirname(__file__))
from utils import cargar_imagen, guardar_imagen

def get_ruta_proyecto():
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def principal():
    base_dir = get_ruta_proyecto()
    
    # 1. Abrir una imagen
    ruta_entrada = os.path.join(base_dir, "imagenes", "imagen2.jpg")
    img = cargar_imagen(ruta_entrada)
    
    if img is None:
        print(f"Error: No se encontró la imagen en {ruta_entrada}")
        return
        
    # 2. Convertirla a escala de grises
    # El umbral binario requiere procesar valores de un solo canal (intensidad)
    img_grises = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # 3. Aplicar umbral binario con cv2.threshold
    # Explicación:
    # El threshold binario (umbral) clasifica cada píxel en uno de dos valores.
    # Compara el valor del píxel con el 'valor_umbral'.
    # Si el píxel es mayor que el umbral, se le asigna el 'valor_maximo' (255 = blanco).
    # Si el píxel es menor o igual, se le asigna 0 (negro).
    # Esto es extremadamente útil para segmentar imágenes, encontrar bordes o separar el fondo del objeto.
    
    valor_umbral = 127
    valor_maximo = 255
    
    # La función retorna dos valores, el umbral usado y la imagen resultante.
    umbral_aplicado, img_binaria = cv2.threshold(img_grises, valor_umbral, valor_maximo, cv2.THRESH_BINARY)
    
    # Mostrar el valor de umbral usado
    print(f"Se aplicó el umbral binario.")
    print(f"Valor de umbral especificado: {valor_umbral}")
    print(f"Valor de umbral retornado por la función: {umbral_aplicado}")
    
    # 4. Guardar la imagen en blanco y negro
    ruta_salida = os.path.join(base_dir, "resultados", "imagen_umbral_binario.png")
    guardar_imagen(ruta_salida, img_binaria)

if __name__ == "__main__":
    principal()
