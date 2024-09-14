def alert_listener(data):
    print(f"ALERTA: El sensor {data['sensor']} ha superado el umbral con un valor de {data['value']}")
