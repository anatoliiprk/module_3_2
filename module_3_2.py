def send_email (message, recipient, *, sender='university.help@gmail.com'):
    check = ['.ru', '.com', '.net',]
    a = len(check)
    flag_1 = False
    flag_2 = False
    flag_3 = False
    c = 0
    d = 0
    if recipient.find('@') != -1:
        flag_1 = True
    for i in range(a):
        c = recipient.find(check[i])
        if c != -1:
            flag_2 = True
            break
    for i in range(a):
        d = sender.find(check[i])
        if d != -1:
            flag_3 = True
            break
    if flag_1 == False or flag_2 == False or flag_3 == False:
        print('Невозможно отправить письмо с адреса', sender, 'на адрес', recipient)
    elif sender == recipient:
        print('Нельзя отправить письмо самому себе!')
    elif sender == 'university.help@gmail.com':
        print('Письмо успешно отправлено с адреса', sender, 'на адрес', recipient)
    else:
        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса', sender, 'на адрес', recipient)

send_email('Письмо с неверным доменом почты', 'anatoliiprk@gmail.com', sender='university.help@gmail.uk')
send_email('Письмо с отправителем не по умолчанию', 'anatolii-karpov2009@yandex.ru', sender='urban.info@gmail.com')
send_email('Письмо, отправленное самому себе', 'anatoliiprk@gmail.com', sender='anatoliiprk@gmail.com')
send_email('Стандартное письмо', 'anatoliiprk@gmail.com')