class Vehicle():

    rented_vehicles = 0
    
    def __init__(self, vehicle_id, model, status):
        self.vehicle_id = vehicle_id
        self.model = model
        self.status = status


    def rent_vehicle(self):
        self.status = 'rented'        


    def return_vhicle(self):
        self.status = 'available'


vehicle1 = Vehicle(1, 'Toyota', 'available')
vehicle2 = Vehicle(2, 'Honda', 'available')
vehicle3 = Vehicle(3, 'Camry', 'available')
vehicle4 = Vehicle(4, 'Benz', 'available')

vehicle2.rent_vehicle()
vehicle1.rent_vehicle()
vehicle4.return_vhicle()

list_of_vehicles = [vehicle1, vehicle2, vehicle3, vehicle4]


for vehicle in list_of_vehicles:
    if vehicle.status == 'rented':
        Vehicle.rented_vehicles += 1

print(Vehicle.rented_vehicles)

