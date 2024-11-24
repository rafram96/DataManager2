import pandas as pd
import random
from faker import Faker
import os

locales = {
    "United States": "en_US", "Canada": "en_CA", "Mexico": "es_MX",
    "Argentina": "es_AR", "Brazil": "pt_BR", "Chile": "es_CL", "Colombia": "es_CO",
    "Peru": "es_ES", "Uruguay": "es_ES", "Ecuador": "es_ES", "Bolivia": "es_ES",
    "Spain": "es_ES", "France": "fr_FR", "Germany": "de_DE", "Italy": "it_IT",
    "United Kingdom": "en_GB", "Russia": "ru_RU", "Poland": "pl_PL",
    "Sweden": "sv_SE", "Norway": "no_NO", "Denmark": "da_DK", "Finland": "fi_FI",
    "China": "zh_CN", "India": "en_IN", "Japan": "ja_JP", "South Korea": "ko_KR",
    "New Zealand": "en_NZ", "Australia": "en_AU"
}
fake_generators = {country: Faker(locale) for country, locale in locales.items()}

def generar_compradores(usuarios, output_folder, filename):
    print("Ejecutando generar_compradores.py...")
    data = []

    for username in usuarios:
        pais = random.choice(list(fake_generators.keys()))
        fake = fake_generators[pais]
        data.append({
            "username": username,
            "direccion_envio": fake.address().replace("\n", ", "),
            "pais": pais
        })

    compradores_df = pd.DataFrame(data)
    compradores_path = os.path.join(output_folder, filename)
    compradores_df.to_csv(compradores_path, index=False, encoding="utf-8")