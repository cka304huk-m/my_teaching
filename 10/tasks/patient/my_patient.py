import patient, procedure

def main():

    name, address, telephone, contact = get_patient()
    info(name, address, telephone, contact)

def get_patient():
    """Информация о пациенте"""
    name = input('имя, отчество и фамилия: ')
    address = input('адрес, город, область и почтовый индекс: ')
    telephone = input('телефонный номер: ')
    contact = input('имя и телефон контактного лица для экстренной связи: ')

    return name, address, telephone, contact
def info(name, address, telephone, contact):
    print('\nИнформация о пациенте:')
    info_patient = patient.Patient(name, address, telephone, contact)
    print('имя, отчество и фамилия:', info_patient.get_name_patronymic_surname())
    print('адрес, город, область и почтовый индекс:', info_patient.get_address_city_region_zip())
    print('телефонный номер:', info_patient.get_number_telephone())
    print('имя и телефон контактного лица для экстренной связи:', info_patient.get_name_telephone_emergency())
    print()
    for i in range(1, 4):
        print('Процедура №', i, sep='')
        name_procedure = input('Название процедуры: ')
        date_procedure = input('Дата: ')
        name_doctor_performed_procedure = input('Врач: ')
        cost_procedure = float(input('Стоимость: '))
        my_procedure = procedure.Procedure(name_procedure,
                                           date_procedure,
                                           name_doctor_performed_procedure,
                                           cost_procedure)
        print('Название процедуры:', '\n', my_procedure.get_name_procedure())
        print('Дата:', my_procedure.get_date_procedure())
        print('Врач:', my_procedure.get_name_doctor_performed_procedure())
        print('Стоимость:', my_procedure.get_cost_procedure())
        print()
    print('-' * 76)

main()