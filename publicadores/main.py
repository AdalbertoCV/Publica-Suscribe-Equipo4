import random
from src.patient import Patient
from src.helpers.publicador import Publisher
import time

if __name__ == '__main__':
    publisher = Publisher()
    print("Iniciando simulación del sistema SMAM...")
    older_patients = []
    total_patients = random.randint(1, 5)
    print(f"actualmente hay {total_patients} adultos mayores...")
    for _ in range(total_patients):
        older_patients.append(Patient())
    print("Comenzando monitoreo de signos vitales...")
    print()
    for _ in range(20):
        for patient in older_patients:
            print("extrayendo signos vitales...")
            patient.check_devices()
            print()
            print("analizando signos vitales...")
            if patient.wearable.blood_pressure > 110 or patient.wearable.temperature > 37.5 or patient.wearable.heart_rate > 110:
                print("anomalía detectada, notificando signos vitales...")
                publisher.publish('notifier', patient.to_json())
            print()
            print("actualizando expediente...")
            publisher.publish('record', patient.to_json())
            publisher.publish('monitor', patient.to_json())
            time.sleep(1)
