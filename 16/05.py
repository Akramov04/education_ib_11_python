friends = {}


def add_friends(name_of_person, list_of_friends):
    a = friends.get(name_of_person)
    if a:
        friends[name_of_person] = a + list_of_friends
    else:
        friends[name_of_person] = list_of_friends


def are_friends(name_of_person1, name_of_person2):
    if name_of_person2 in friends[name_of_person1]:
        return True
    return False


def print_friends(name_of_person):
    s = friends[name_of_person][::-1]
    for i in s:
        print(i, end=' ')
    print()


add_friends("Алла", ["Марина", "Иван"])
print(are_friends("Алла", "Мария"))
add_friends("Алла", ["Мария"])
print(are_friends("Алла", "Мария"))