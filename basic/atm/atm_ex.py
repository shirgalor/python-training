import fileinput


def bank_action(personal_info):
    request = input("please enter your request:")
    if request == "Check the balance":
        print(personal_info[2])
    elif request == "Cash withdrawal":
        less_num = input("how much do you want:")
        personal_info[2] = int(personal_info[2]) - int(less_num)
    elif request == "Cash deposit":
        add_num = input("how much do you want:")
        personal_info[2] = int(personal_info[2]) + int(add_num)
    elif request == "Change password":
        password = input("enter new password:")
        personal_info[1] = password
    else:
        print("error request")
    return personal_info


def from_file_to_list(file_bank):
    bank_info = []
    for line in file_bank:
        p = line.split()
        bank_info.append(p)
    return bank_info


def from_list_to_file(bank_list, file_bank):
    for i in bank_list:
        new_line = from_list_to_line(i)
        file_bank.write(new_line)
    return file_bank


def from_list_to_line(lst):
    for i in lst:
        i = str(i)
        new_line = ' '.join(i)
    return new_line


def atm():
    atm_file = r'C:\Users\User\Downloads\wordcount\alice.txt'
    with open(atm_file, 'r') as read_file:
        bank_info = from_file_to_list(read_file)
        print(bank_info)
        while True:
            id_of_p = input("please enter id num:")
            if id_of_p != "-1":
                for element in bank_info:
                    if element[0] == id_of_p:
                        bank_action(element)
            else:
                break
    with open(atm_file, 'w') as changed_file:
        from_list_to_file(bank_info, changed_file)


if __name__ == '__main__':
    atm()
