from datetime import date, time, datetime


def trabalhando_com_datetime():
    data_atual = datetime.now()
    print(data_atual)
    print(data_atual.strftime('%d/%m/%Y %H:%M:%S'))


def trabalhando_com_date():
    data_atual = date.today()
    print(data_atual.strftime('%d/%m/%Y')) #strftime faz com que que aparece com o padrão Br


def trabalhando_com_time():
    horario = time(hour=15, minute=20, second=20)
    print(horario)


if __name__ == '__main__':
    #trabalhando_com_date()
    #trabalhando_com_time()
    trabalhando_com_datetime()