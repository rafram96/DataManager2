import pandas as pd
import random
from faker import Faker
import os

def generar_resenas(num_records, output_folder, filename, ventas_df):
    print("Ejecutando generar_resenas.py...")
    fake = Faker()
    resenas_path = os.path.join(output_folder, filename)
    ventas_df["fecha"] = pd.to_datetime(ventas_df["fecha"])
    data = []

    for _, row in ventas_df.iterrows():
        data.append({
            "Vendedor_Username": row["vendedor_username"],
            "Comprador_Username": row["comprador_username"],
            "Producto_ID": row["producto_id"],
            "FechaPublicada": fake.date_between(start_date=row["fecha"], end_date='today'),
            "comentario": fake.sentence(),
            "puntuacion": random.randint(1, 5)
        })

    resenas_df = pd.DataFrame(data)
    resenas_df.to_csv(resenas_path, index=False, encoding="utf-8")