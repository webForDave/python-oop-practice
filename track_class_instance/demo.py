class Vehicle:

    vehicle_count = 0

    def __init__(self):
        self.vehicle_count += 1

    @classmethod
    def total_vehicles(cls):
        return Vehicle.vehicle_count
    
    @staticmethod
    def is_valid_registration(reg_number):        
        if len(reg_number) < 6:
            return 'Reg number cannot be less than six characters'
        elif len(reg_number) > 8:
            return 'Reg number cannot be more than eight characters'
        else:
            return True


print(Vehicle.is_valid_registration('12lloty'))