import pandas as pd
import random
from faker import Faker
import os

def generar_ventas(num_records, output_folder, filename, inventario_df, compradores):
    print("Ejecutando generar_ventas.py...")
    fake = Faker()
    ventas_path = os.path.join(output_folder, filename)

    dynamic_inventory = inventario_df.set_index(["vendedor_username", "producto_id"])["cantidad"].to_dict()
    ventas = []

    for _ in range(num_records):
        available_products = {key: stock for key, stock in dynamic_inventory.items() if stock > 0}
        if not available_products:
            print("No hay más productos disponibles para vender.")
            break

        vendedor, producto = random.choice(list(available_products.keys()))
        max_stock = dynamic_inventory[(vendedor, producto)]
        if max_stock <= 0:
            continue

        cantidad = random.randint(1, max_stock)
        dynamic_inventory[(vendedor, producto)] -= cantidad

        ventas.append({
            "comprador_username": random.choice(compradores),
            "vendedor_username": vendedor,
            "producto_id": producto,
            "fecha": fake.date_between(start_date='-4y', end_date='today'),
            "importe": round(random.uniform(10, 500), 2),
            "cantidad": cantidad
        })

    ventas_df = pd.DataFrame(ventas)
    ventas_df.to_csv(ventas_path, index=False, encoding="utf-8")