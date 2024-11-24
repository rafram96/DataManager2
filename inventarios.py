import pandas as pd
import random
import os

def generar_inventario(num_records, output_folder, filename, vendedores, productos):
    print("Ejecutando generar_inventario.py...")
    data = []

    for _ in range(num_records):
        data.append({
            "producto_id": random.choice(productos),
            "vendedor_username": random.choice(vendedores),
            "cantidad": random.randint(1, 30)
        })

    inventario_df = pd.DataFrame(data)
    inventario_path = os.path.join(output_folder, filename)
    inventario_df.to_csv(inventario_path, index=False, encoding="utf-8")