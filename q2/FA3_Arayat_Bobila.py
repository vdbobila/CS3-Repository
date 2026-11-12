from abc import ABC, abstractmethod

class Sensor(ABC):
    @abstractmethod
    def get_reading(self):
        pass

class PHSensor(Sensor):
    def get_reading(self):
        return "[pH Sensor] Reading: 7.2 pH (Neutral)"
    def __str__(self):
        return "[pH Sensor] Reading: 7.2 pH (Neutral)"

class TempSensor(Sensor):
    def get_reading(self):
        return "[Temperature Sensor] Reading: 24.5°C"
    def __str__(self):
        return "[Temperature Sensor] Reading: 24.5°C"

sensor1 = PHSensor()
sensor2 = TempSensor()

print("--- Lab Inventory System ---","\n")
print(sensor1)
print(sensor2,"\n")
print("-"*28)
