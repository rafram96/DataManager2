import pandas as pd
import random
from faker import Faker
import os

def generar_cartas(productos_df, output_folder, filename):
    print("Ejecutando generar_cartas.py...")
    fake = Faker()
    cartas_path = os.path.join(output_folder, filename)
    data = []

    for _, producto in productos_df[productos_df["categoria"] == "Carta"].iterrows():
        data.append({
            "producto_id": producto["id"],
            "descripcion": fake.sentence(),
            "rareza": random.choice(["Common", "Uncommon", "Rare", "Special", "Promotional"]),
            "estado": random.choice(["Poor", "Played", "Light Played", "Good", "Excellent", "Mint"]),
        })

    cartas_df = pd.DataFrame(data)
    cartas_df.to_csv(cartas_path, index=False, encoding="utf-8")