def from_string_to_list(string, container):
    container.extend(map(int, string.split()))


container = [1, 2, 3]
from_string_to_list("1 3 99 52", container)
print(*container)