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


tree = Tree()
tree.insert(8)
tree.insert(7)
tree.insert(3)
tree.insert(10)
tree.insert(14)
tree.insert(6)
tree.insert(1)
tree.insert(4)
print(tree.inorder())
print(tree.search(1))
