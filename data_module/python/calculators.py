#Contiene la lógica de datos, trae significado a los números crudos que provienen de la API de Climatiq
def calcular_huella_base(datos_climatiq):
    # extrae el número de CO₂
    return datos_climatiq.get("co2e")

def calcular_eco_score(huella, packaging, ingredientes):
    # fórmula que vos definas
    pass

def clasificar_eco_badge(score):
    if score >= 80:
        return "🌳 Excelente"
    elif score >= 50:
        return "🌿 Bueno"
    else:
        return "🌱 Básico"
    