"""Este archivo recibe datos del producto, llena parámetros para Climatiq, llama a climatiq_client, 
manda el resultado a calculators, devuelve un objeto final"""
from .climatiq_client import consultar_climatiq
from .calculators import calcular_huella_base, calcular_eco_score, clasificar_eco_badge

def procesar_producto(producto):
    # 1. definir actividad
    activity_id = producto.get("activity_id")

    # 2. definir parámetros para Climatiq
    parameters = {
        "mass": producto["peso_neto"],
        "mass_unit": "kg"
    }

    # 3. llamar a Climatiq
    datos = consultar_climatiq(activity_id, parameters, api_key="XXXX")

    # 4. calcular huella base
    huella = calcular_huella_base(datos)

    # 5. eco score
    score = calcular_eco_score(huella, producto["packaging"], producto["ingredientes"])

    # 6. badge
    badge = clasificar_eco_badge(score)

    return {
        "huella_carbono": huella,
        "eco_score": score,
        "badge": badge
    }
