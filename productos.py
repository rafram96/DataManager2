import pandas as pd
import random
import uuid
from faker import Faker
import os

def generar_productos(num_records, output_folder, filename):
    print("Ejecutando generar_productos.py...")
    fake = Faker()
    data = []

    num_productos = num_records * 2
    for _ in range(num_productos):
        categoria = random.choices(["Carta", "Booster Box"], weights=[0.6, 0.4], k=1)[0]
        data.append({
            "id": str(uuid.uuid4())[:8],
            "nombre": fake.word(),
            "precio": round(random.uniform(1, 100), 2),
            "categoria": categoria,
            "set_nombre": fake.word()
        })

    productos_df = pd.DataFrame(data)
    productos_path = os.path.join(output_folder, filename)
    productos_df.to_csv(productos_path, index=False, encoding="utf-8")