from binarytree import bst


# number это число для поиска
def search(bin_search_tree, number, path=''):
    if bin_search_tree.value == number:
        return f'Число {number} обнаружено по следующему пути: \nКорень{path}'

    # если искомое число меньше того, которое храниться в данном узле и при этом у этого узла СЛЕВА есть дочерний узел
    if number < bin_search_tree.value and bin_search_tree.left != None:
        # то продолжаем поиск в ЛЕВОЙ части дерева
        return search(bin_search_tree.left, number, path=f'{path}\n Шаг влево')

    # если искомое число меньше того, которое храниться в данном узле и при этом у этого узла СПРАВА есть дочерний узел
    if number > bin_search_tree.value and bin_search_tree.right != None:
        # то продолжаем поиск в ПРАВОЙ части дерева
        return search(bin_search_tree.right, number, path=f'{path}\n Шаг вправо')

    return f'Число {number} отсутствует в дереве'


bt = bst(height=5, is_perfect=False)
print(bt)
num = int(input('Введите число для поиска: '))
print(search(bt, num))
