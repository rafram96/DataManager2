import pandas as pd
import random
from faker import Faker
import os

def generar_boosterboxes(productos_df, output_folder, filename):
    print("Ejecutando generar_boosterboxes.py...")
    fake = Faker()
    boosterboxes_path = os.path.join(output_folder, filename)
    data = []

    for _, producto in productos_df[productos_df["categoria"] == "Booster Box"].iterrows():
        data.append({
            "producto_id": producto["id"],
            "descripcion": fake.text(),
            "cantidad_sobres": random.randrange(12, 33, 2),
            "edicion_especial": random.choice([True, False]),
        })

    boosterboxes_df = pd.DataFrame(data)
    boosterboxes_df.to_csv(boosterboxes_path, index=False, encoding="utf-8")