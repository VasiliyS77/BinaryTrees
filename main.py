class Node:
    """Класс Узел дерева"""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Tree:
    """Класс Дерево"""
    def __init__(self):
        self.root = None
        self.tree_to_list = []

    def search(self, value) -> bool:
        """Поиск значения в дереве"""
        if self.root is None:
            return False
        else:
            search_result = self.__search__(self.root, value)
            return False if search_result is None else True

    def __search__(self, root: Node, value):
        """Поиск значения в дереве
        (рекурсивная функция)"""
        if root.value == value:
            return value

        if value < root.value:
            if root.left is None:
                return None
            else:
                return self.__search__(root.left, value)
        else:
            if root.right is None:
                return None
            else:
                return self.__search__(root.right, value)


    def inorder(self) -> list:
        """Возвращает упорядоченный список как результат обхода дерева"""
        self.tree_to_list = []
        return self.__inorder__(self.root)

    def __inorder__(self, root: Node) -> list:
        """Возвращает упорядоченный список как результат обхода дерева
        (рекурсивная функция)"""
        if root is not None:

            # Обход левого поддерева
            self.__inorder__(root.left);

            # Корень (под) дерева
            self.tree_to_list.append(root.value)

            # Обход правого поддерева
            self.__inorder__(root.right)

            return self.tree_to_list


    def insert(self, value) -> None:
        """Вставка узла дерева"""

        # Новый узел
        new_item = Node(value)

        # Если дерево не существует, то оно создается (создается корень)
        if not self.root:
            self.root = new_item
        else:
            self.__insert_item__(self.root, new_item)

    def __insert_item__(self, node: Node, new_node: Node) -> None:
        """Вставка нового узла (рекурсивная функция)"""

        # Если значение уже существует, выбрасывается ошибка
        if new_node.value == node.value:
            raise ValueError(f"Значение < {new_node.value} > существует.")

        if new_node.value < node.value:
            # Вставка по левой ветке
            if not node.left:
                node.left = new_node
                return
            else:
                self.__insert_item__(node.left, new_node)
        else:
            # Вставка по правой ветке
            if not node.right:
                node.right = new_node
                return
            else:
                self.__insert_item__(node.right, new_node)

    def delete(self, value) -> None:
        """Удаление значения из дерева"""
        if self.root is not None:
            self.__delete_item__(self.root, value)

    def __min_value_node_(self, root: Node):
        """Поиск крайнего левого узла (относительно указанного)"""
        current = root
        while (current.left is not None):
            current = current.left
        return current

    def __delete_item__(self, root: Node, value):
        """Удаление значения из дерева
        (рекурсивная функция)"""
        # Возвращаем, если поддерево пустое
        if root is None:
            return None

        if value < root.value:
            root.left = self.__delete_item__(root.left, value)
        elif value > root.value:
            root.right = self.__delete_item__(root.right, value)
        else:
            # Если у элемента только один дочерний узел или таковых вообще нет
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp

            # Если у узла два дочерних узла,
            # помещаем центрированного преемника
            # на место узла, который нужно удалить
            temp = self.__min_value_node_(root.right)
            root.value = temp.value
            # Удаляем inorder-преемниа
            root.right = self.__delete_item__(root.right, temp.value)

        return root

    def tree_view(self):
        """Визуализация дерева"""
        # Ширина позиции под число
        position_width = 6

        # Создание ступенчатого списка
        view = []
        view.append([self.root])
        level = 0
        while True:
             level_view: list[Node] = []
             for it in view[level]:
                 if it is None:
                     level_view.append(None)
                     level_view.append(None)
                 else:
                     level_view.append(it.left)
                     level_view.append(it.right)
             if not any(level_view):
                 break
             else:
                 view.append(level_view)
                 level += 1

        # Текстовая визуализация дерева
        tree_text_view = ""
        # Ширина "основания" дерева
        tree_width = len(view[-1])
        # Ширина строки
        line_width = position_width * tree_width
        #
        # empty_pos = ' ' * position_width

        for line in view:
            line_str = ''
            # Ширина позиции исходя из уровня дерева
            curren_line_pos_width = int(line_width / len(line))
            for it in line:
                if it is None:
                    # Добавляется 'пустая' позиция
                    line_str += ' ' * curren_line_pos_width
                else:
                    # Добавляется позиция с числом (отцентрованным по текущей позиции)
                    value_in_pos = self.__centre__(curren_line_pos_width, position_width, it.value)
                    line_str += value_in_pos
            tree_text_view += line_str
            # Если строка не последняя добавляются 'графы'
            if len(line) < tree_width:
                tree_text_view += '\n'
                line_str = self.__graph_str__(curren_line_pos_width, position_width)
                tree_text_view += line_str * len(line) + '\n'

        return tree_text_view

    def __centre__(self, str_len: int, pos_width: int, value) -> str:
        """Возвращает отцентрованную строку
        str_len - ширина строки
        pos_width - ширина позиции под число
        value отображаемое значение"""

        # Число в строковом формате
        value_str = str(value)
        # Ширина отступа
        if len(value_str) < pos_width:
            indent_width = int((str_len - len(value_str)) / 2)
        else:
            indent_width = int((str_len - pos_width) / 2)
        # Отступ
        indent = ' ' * indent_width
        # Результирующая строка
        output_line = indent + str(value) + indent
        return output_line

    def __graph_str__(self, str_len: int, pos_width: int) -> str:
        """Возвращает строку с 'графами'  /\
        str_len: ширина строки
        pos_width: ширина позиции под число"""

        # Ширина отступа
        indent_width = int((str_len - pos_width) / 2) - 1
        # Отступ
        indent = ' ' * indent_width
        position = ' ' * pos_width
        # Результирующая строка
        output_line = indent + '/' + position + '\\' + indent
        return output_line


tree = Tree()

tree.insert(8)
tree.insert(3)
tree.insert(1)
tree.insert(6)
tree.insert(10)
tree.insert(14)
tree.insert(7)
tree.insert(4)

list_v = tree.tree_view()
print(list_v)
print()
print()

tree.delete(3)
list_v = tree.tree_view()
print(list_v)

# print(tree.__centre__(16, 4, 9))
# print(tree.__graph_str__(16, 4))


#         8
#        / \
#       4   9
#      / \
#     3   6
