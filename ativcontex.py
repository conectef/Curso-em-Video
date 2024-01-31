def calcular_consumo_energia(casa_area):
    # Consumo médio de energia por metro quadrado
    consumo_medio = 10  # em watts por metro quadrado
    
    # Calcular o consumo total estimado
    consumo_total = consumo_medio * casa_area
    
    # Converter para kilowatts
    consumo_total_kw = consumo_total / 1000
    
    return consumo_total_kw


# Exemplo de uso
area_casa = 100  # metros quadrados

consumo_energia = calcular_consumo_energia(area_casa)

print(f"A casa de {area_casa}m² consome aproximadamente {consumo_energia} kWh de energia.")
