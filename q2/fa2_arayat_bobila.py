class Patient:
    name = ""
    bill_amount = 0
    def __init__(self, name, bill_amount):
        self.__name = name
        self.__bill_amount = bill_amount
    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name
    def get_bill_amount(self):
        return self.__bill_amount
    def set_bill_amount(self, bill_amount):
        self.__bill_amount = bill_amount
    def calculate_bill(self):
        print(f"Patient Name: {self.__name}\nOriginal Bill: ₱{self.__bill_amount}\nFinal Bill: ₱{self.__bill_amount}\n")

class Senior_Patient(Patient):
    def __init__(self, name, bill_amount):
        super().__init__(name, bill_amount)
    def calculate_bill(self):
        print(f"Patient Name: {self._Patient__name}\nOriginal Bill: ₱{self._Patient__bill_amount}\nFinal Bill: ₱{self._Patient__bill_amount*0.80}\n")

class PhilHealth_Patient(Patient):
    def __init__(self, name, bill_amount):
        super().__init__(name, bill_amount)
    def calculate_bill(self):
        print(f"Patient Name: {self._Patient__name}\nOriginal Bill: ₱{self._Patient__bill_amount}\nFinal Bill: ₱{self._Patient__bill_amount*0.85}\n")
    
regular_patient = Patient("Juan Dela Cruz", float(15000))

old_patient = Senior_Patient("Maria Santos", float(15000))

special_patient = PhilHealth_Patient("Pedro Reyes", float(15000))
print("Hospital Billing System\n","-"*23)
regular_patient.calculate_bill()
old_patient.calculate_bill()
special_patient.calculate_bill()

    
    
