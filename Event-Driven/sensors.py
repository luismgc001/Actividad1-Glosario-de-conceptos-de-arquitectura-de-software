import random
from event_manager import EventManager

class Sensor:
    def __init__(self, name, threshold, event_manager):
        self.name = name
        self.threshold = threshold
        self.event_manager = event_manager

    def detect_value(self):
        # Simular la detección de un valor aleatorio
        value = random.randint(0, 100)
        print(f"Sensor {self.name} detecta valor: {value}")
        if value > self.threshold:
            self.event_manager.notify('threshold_exceeded', {"sensor": self.name, "value": value})
