def count_common_elements(*lists):
    # Создаем множество для хранения уникальных элементов
    unique_elements = set(lists[0])
    # Перебираем оставшиеся списки и находим их пересечение с множеством уникальных элементов
    for lst in lists[1:]:
        unique_elements = unique_elements.intersection(set(lst))
    # Возвращаем количество элементов в пересечении
    return len(unique_elements)