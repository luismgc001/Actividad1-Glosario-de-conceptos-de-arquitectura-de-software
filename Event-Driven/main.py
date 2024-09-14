from event_manager import EventManager
from sensors import Sensor
from listeners import alert_listener

def main():
    event_manager = EventManager()

    # Suscribimos el listener al evento de superación de umbral
    event_manager.subscribe('threshold_exceeded', alert_listener)

    # Creamos algunos sensores con diferentes umbrales
    sensor1 = Sensor("Sensor 1", 70, event_manager)
    sensor2 = Sensor("Sensor 2", 50, event_manager)

    # Simulamos que los sensores detectan valores
    for _ in range(5):
        sensor1.detect_value()
        sensor2.detect_value()

if __name__ == "__main__":
    main()
