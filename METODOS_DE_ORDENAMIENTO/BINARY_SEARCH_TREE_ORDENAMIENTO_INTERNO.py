class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return TreeNode(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def inorder_traversal(root):
    if root:
        # Realiza el recorrido inorden (izquierda, raiz, derecha) del arbol.
        inorder_traversal(root.left)
        print(root.val)
        inorder_traversal(root.right)

# Ejemplo de uso:
if __name__ == "__main__":
    root = None
    keys = [50, 30, 20, 40, 70, 60, 80]
    
    for key in keys:
        root = insert(root, key)
    
    print("Recorrido inorden del arbol ordenado:")
    inorder_traversal(root)

