import pandas as pd
from faker import Faker
import os
import random

def generar_sets(num_records, output_folder, filename):
    print("Ejecutando generar_sets.py...")
    fake = Faker()
    data = []

    num_sets = num_records // 100
    for _ in range(num_sets):
        data.append({
            "nombre": f"{fake.word()} {fake.word()}",
            "franquicia": random.choice(["Pokemon", "Magic", "Yu-Gi-Oh"]),
            "fecha_lanzamiento": fake.date_between(start_date='-10y', end_date='today')
        })

    sets_df = pd.DataFrame(data)
    sets_path = os.path.join(output_folder, filename)
    sets_df.to_csv(sets_path, index=False, encoding="utf-8")