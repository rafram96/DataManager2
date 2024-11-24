import pandas as pd
import random
import os

def generar_vendedores(usuarios, output_folder, filename):
    print("Ejecutando generar_vendedores.py...")
    data = []

    for username in usuarios:
        data.append({
            "username": username,
            "verificado": random.choice([True, False]),
            "valoracion": round(random.uniform(1.0, 5.0), 2)
        })

    vendedores_df = pd.DataFrame(data)
    vendedores_path = os.path.join(output_folder, filename)
    vendedores_df.to_csv(vendedores_path, index=False, encoding="utf-8")