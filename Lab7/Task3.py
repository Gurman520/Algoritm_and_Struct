import pickle


class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key


def sr(tree):
    if tree.getLeftChild() == tree.getRightChild() == None:
        print(f"Это {tree.getRootVal()}?")
        if input() == 'ДА':
            pass
        else:
            z = input(f"Какое животное вы загадали?\n")
            c = input(f"Какой вопрос поможет отличить {tree.getRootVal()} и {z}?\n")
            tree.insertLeft(z)
            tree.insertRight(tree.getRootVal())
            tree.setRootVal(c)
    else:
        print(tree.getRootVal())
        if input() == 'ДА':
            sr(tree.getLeftChild())
        else:
            sr(tree.getRightChild())


with open('data.pickle', 'rb') as f:
    r = pickle.load(f)

# r = BinaryTree('Это млекопитающее?')
# r.insertRight('Оно покрыто чешуей?')
# r.getRightChild().insertRight('Птица')
# r.getRightChild().insertLeft('Рыба')
# r.insertLeft('Оно лает?')
# r.getLeftChild()
# r.getLeftChild().insertLeft('Собака')
# r.getLeftChild().insertRight('Кошка')
sr(r)

with open('data.pickle', 'wb') as f:
    pickle.dump(r, f)

