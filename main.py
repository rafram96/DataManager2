import os
import time
import pandas as pd
from usuarios import generar_usuarios
from vendedores import generar_vendedores
from compradores import generar_compradores
from sets import generar_sets
from productos import generar_productos
from inventarios import generar_inventario
from ventas import generar_ventas
from resenas import generar_resenas
from cartas import generar_cartas
from boosterboxes import generar_boosterboxes

def get_filename(base_name, con_i):
    suffix = "CON-I" if con_i else "SIN-I"
    return f"{base_name}_{suffix}.csv"

# Configuración inicial
output_base = "output_data"
os.makedirs(output_base, exist_ok=True)
record_options = {"1k": 1_000, "10k": 10_000, "100k": 100_000, "1M": 1_000_000}
selection = "100k"
num_records = record_options.get(selection)
if not num_records:
    raise ValueError("Opción inválida seleccionada.")
output_folder = os.path.join(output_base, selection)
os.makedirs(output_folder, exist_ok=True)

# Crear subcarpetas
folders = ["Usuarios", "Vendedores", "Compradores", "Sets", "Productos", "Inventario", "Ventas", "Resenas", "Cartas", "BoosterBoxes"]
for folder in folders:
    os.makedirs(os.path.join(output_folder, folder), exist_ok=True)

# Definir si se usa INDICES
con_i = False  # Cambia a False para SIN_I

# Generar datos
start_time = time.time()
print("Generando usuarios...")
usuarios = generar_usuarios(num_records, os.path.join(output_folder, "Usuarios"), get_filename("usuarios", con_i))

print("Generando vendedores...")
generar_vendedores(usuarios, os.path.join(output_folder, "Vendedores"), get_filename("vendedores", con_i))

print("Generando compradores...")
generar_compradores(usuarios, os.path.join(output_folder, "Compradores"), get_filename("compradores", con_i))

print("Generando sets...")
generar_sets(num_records, os.path.join(output_folder, "Sets"), get_filename("sets", con_i))

print("Generando productos...")
generar_productos(num_records, os.path.join(output_folder, "Productos"), get_filename("productos", con_i))

productos_df = pd.read_csv(os.path.join(output_folder, "Productos", get_filename("productos", con_i)))
productos = productos_df["id"].tolist()

print("Generando cartas...")
generar_cartas(productos_df, os.path.join(output_folder, "Cartas"), get_filename("cartas", con_i))

print("Generando booster boxes...")
generar_boosterboxes(productos_df, os.path.join(output_folder, "BoosterBoxes"), get_filename("boosterboxes", con_i))

vendedores = usuarios[:len(usuarios) // 2]

print("Generando inventario...")
generar_inventario(num_records, os.path.join(output_folder, "Inventario"), get_filename("inventario", con_i), vendedores, productos)

compradores = usuarios[len(usuarios) // 2:]
inventario_df = pd.read_csv(os.path.join(output_folder, "Inventario", get_filename("inventario", con_i)))

print("Generando ventas...")
generar_ventas(num_records, os.path.join(output_folder, "Ventas"), get_filename("ventas", con_i), inventario_df, compradores)

ventas_df = pd.read_csv(os.path.join(output_folder, "Ventas", get_filename("ventas", con_i)))

print("Generando reseñas...")
generar_resenas(num_records, os.path.join(output_folder, "Resenas"), get_filename("resenas", con_i), ventas_df)

end_time = time.time()
elapsed_time = (end_time - start_time) / 60
print(f"Generación completa. Tiempo total: {elapsed_time:.4f} minutos.")