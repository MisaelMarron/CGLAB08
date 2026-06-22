import os
import sys

# Agregar la ruta actual al path del sistema para importar utils correctamente
sys.path.append(os.path.dirname(__file__))
from utils import cargar_imagen, guardar_imagen, redimensionar_aspect_ratio, agregar_bordes_negros

def get_ruta_proyecto():
    """Obtiene la ruta base del proyecto para no depender de rutas absolutas locales."""
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def principal():
    base_dir = get_ruta_proyecto()
    
    # 1. Definir las rutas relativas de las 3 imágenes
    rutas = [
        os.path.join(base_dir, "imagenes", "imagen1.jpg"),
        os.path.join(base_dir, "imagenes", "imagen2.jpg"),
        os.path.join(base_dir, "imagenes", "imagen3.jpg")
    ]
    
    imagenes = []
    
    # 2. Abrir tres imágenes a color
    for ruta in rutas:
        img = cargar_imagen(ruta)
        if img is None:
            print(f"Por favor, asegúrate de colocar la imagen correspondiente en la ruta: {ruta}")
            return
        imagenes.append(img)
        
    # 3. Detectar cuál tiene mayor ancho y alto
    max_w = max(img.shape[1] for img in imagenes)
    max_h = max(img.shape[0] for img in imagenes)
    
    print(f"Dimensiones máximas encontradas entre todas las imágenes: Ancho={max_w}, Alto={max_h}")
    
    # 4. Redimensionar y agregar bordes
    for i, img in enumerate(imagenes):
        # Paso A: Redimensionar manteniendo la relación de aspecto sin deformar
        img_redimensionada = redimensionar_aspect_ratio(img, max_w, max_h)
        
        # Paso B: Rellenar los espacios vacíos con bordes negros
        img_final = agregar_bordes_negros(img_redimensionada, max_w, max_h)
        
        # Paso C: Guardar los resultados en la carpeta resultados/
        ruta_guardado = os.path.join(base_dir, "resultados", f"imagen{i+1}_redimensionada.png")
        guardar_imagen(ruta_guardado, img_final)

if __name__ == "__main__":
    principal()
