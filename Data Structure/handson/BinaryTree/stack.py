class TreeStack():

	def __init__(self, n=None):
		self.root = n

	def preorder(self):
		stack = [self.root]
		while len(stack) > 0:
			item = stack.pop()
			print(item.value, end=' ')
			if item.right:
				stack.append(item.right)
			if item.left:
				stack.append(item.left)

	def inorder_without_stack(self):
		current = self.root
		while current:
			if current.left is None:
				print(current.value, end=' ')
				current = current.right
			else:
				pre = current.left
				while pre.right and pre.right != current:
					pre = pre.right

				if pre.right is None:
					pre.right = current
					current = current.left

				else:
					pre.right = None
					print(current.value, end=' ')
					current = current.right

	def inorder(self):
		stack, current, loop = [], self.root, True
		while loop:
			if current:
				stack.append(current)
				current = current.left
			elif stack:
				current = stack.pop()
				print(current.value, end=' ')
				current = current.right
			else:
				loop = False

	def postorder(self):
		stack, root, ans = [], self.root, []

		while True:
			while root:
				if root.right:
					stack.append(root.right)
				stack.append(root)

				root = root.left

			root = stack.pop()

			if (root.right and
				self.peek(stack) == root.right):
				stack.pop() # 오른쪽 자식 제거
				stack.append(root)
				root = root.right

			else:
				ans.append(root.value)
				root = None

			if len(stack) <= 0:
				for i in ans:
					print(i, end=' ')
				return

	def peek(self, stack):
		if len(stack) > 0:
			return stack[-1]
		return None


if __name__ == '__main__':
	from linked import Node
	n1 = Node('A')
	n2 = Node('B')
	n3 = Node('C')
	n4 = Node('D')
	n5 = Node('E')
	n6 = Node('F')
	n7 = Node('G')
	n8 = Node('H')

	n1.left = n2
	n1.right = n3
	n2.left = n4
	n2.right = n5
	n3.left = n6
	n3.right = n7
	n4.left = n8

	t = TreeStack(n1)
	print('전위순회: ', end='')
	t.preorder()
	print('\n중위순회: ', end='')
	t.inorder()
	print('\nㄴ스택X : ', end='')
	t.inorder_without_stack()
	print('\n후위순회: ', end='')
	t.postorder()
