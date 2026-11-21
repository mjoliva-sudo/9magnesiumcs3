class Patient:
  def __init__(self,name,name, original_bill)
  self.name = name
  self.original_bill = original_bill

def calculate_bill(self):
  return self.original_bill

def display_patient_type(self):
  print("Patient Type: Regular Patient")

class Senior_Patient(Patient): 
  def calculate_bill(self):
    return self.original_bill * 0.8
    
  def display_patient_type(self):
    print("Patient Type: Senior Citizen")

class PhilHealth_Patient(Patient): 
  def calculate_bill(self):
    return self.original_bill * 0.85
    
  def display_patient_type(self):
    print("Patient Type: PhilHealth Member")

Patient = Patient("Juna Dela Cruz", 15000)
Senior = Senior_Patient("Maria Santos", 15000)
Phil = PhilHealth_Patient("Pedro Reyes", 15000)

p = [Patient, Senior, Phil]
for p in p:
  print(f"Patient Name: {patient.name}")
  patient.display_patient_type()
  print(f"Original Bill: ₱{patient.original_bill:,.2f}")
  print(f"Final Bill: ₱{patient.calculate_bill():,.2f}")
  print()
