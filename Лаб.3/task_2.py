# TODO Напишите функцию find_common_participants
def find_common_participants(str_first,str_second,s = ","):
    common_participants = list(set(str_first.split(s)).intersection(str_second.split(s)))
    common_participants.sort()
    return common_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group,participants_second_group,s = "|") )