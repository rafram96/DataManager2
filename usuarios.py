import pandas as pd
from faker import Faker
import os
import random
import string

def generar_usuarios(num_records, output_folder, filename):
    print("Ejecutando generar_usuarios_unicos.py...")
    fake = Faker()
    unique_usernames = set()
    data = []

    # Listas de palabras base
    nombres = [fake.first_name() for _ in range(1000)]
    apellidos = [fake.last_name() for _ in range(1000)]
    palabras = [fake.word() for _ in range(1000)]
    caracteres_especiales = list(string.punctuation)

    while len(unique_usernames) < num_records:
        # Crear un username único combinando diferentes elementos
        username = (
            random.choice(nombres) +
            random.choice(apellidos) +
            random.choice(palabras) +
            str(random.randint(0, 999)) +
            random.choice(caracteres_especiales)
        )
        if username not in unique_usernames:
            unique_usernames.add(username)
            data.append({
                "username": username,
                "nombre": fake.name(),
                "email": fake.email(),
                "fecha_registro": fake.date()
            })

    usuarios_df = pd.DataFrame(data)
    usuarios_path = os.path.join(output_folder, filename)
    usuarios_df.to_csv(usuarios_path, index=False, encoding="utf-8")
    return list(unique_usernames)