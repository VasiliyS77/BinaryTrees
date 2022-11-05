class TreeNode:
    """Класс Узел дерева"""
    def __init__(self, value):
        self.value = value
        self.right = None


class Tree:
    """Класс Дерево"""
    def __init__(self):
        self.root = None

    def insert_item(self, value):
        """Вставка узла дерева"""

        # Новый узел
        new_item = TreeNode(value)

        # Если дерево не существует, то оно создается (создается корень)
        if not self.root:
            self.root = new_item
        else:
            pass
        
    def __insert__(self, root, node):
        pass

