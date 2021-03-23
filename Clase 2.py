print(123)

class Plane:    
    def __init__(self, id, model, gasoline):        
        self.id = id        
        self.model = model        
        self.gasoline_level = gasoline    
    
    def dispatch_alarm(self, message):        
        print(f'Plane {self.id} Alarm: {message}')    
        
    def fly():       
        print ('Im flying')
        
class Car:    
    def __init__(self, model, gasoline):        
        self.model = model        
        self.gasoline_level = gasoline    
        
    def dispatch_alarm(self, message):        
        print(f'Car {self.model} - Alarm: {message}')       
        print ('Go to a gasoline station')    
        
    def drive():        
        pass
    
class GasolineSensor:    
    def __init__(self, machine):        
        self.machine = machine    
        
    def check_gasoline_level(self):        
        if self.machine.gasoline_level < 20:            
            self.machine.dispatch_alarm('Gasoline Low!!')       
         else:            
             pass
            
plane = Plane('CDA-100', '787', 10)
plane_2 = Plane('AH-100', '474', 100)
car = Car('Renault Latitud', 15)
gasoline_sensor = GasolineSensor(plane)
gasoline_sensor_2 = GasolineSensor(car)
gasoline_sensor_3 = GasolineSensor(plane_2)
gasoline_sensor.check_gasoline_level()
gasoline_sensor_2.check_gasoline_level()
gasoline_sensor_3.check_gasoline_level()