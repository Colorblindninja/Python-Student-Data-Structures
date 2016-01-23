class Node:
	def __init__(self, data = None, left = None, right = None):
		self.data = data
		self.right = right
		self.left = left


class BST: #Binary Search Tree
	def __init__(self):
		self.count = 0
		self.root = None

	def exists(self, data):
		return self.existsR(data, self.root)

	def existsR(self, data, cur):
		if cur == None:
			return False
		elif cur.data == data:
			return True
		elif data < cur.data:
			return self.existsR(data, cur.left)
		else:
			return self.existsR(data, cur.right)


	def insertRecursive(self, item, current):
		if current is None:
			current = item
		elif item.data < current.data:
			current.left = self.insertRecursive(item, current.left)
		else:
			current.right = self.insertRecursive(item, current.right)
		return current
	
	def insert(self, item):
		if self.exists(item):
			return False
		n = Node(item)	
		self.root = self.insertRecursive(n, self.root)
		self.count += 1
		return True


	def retrieve(self, key):
		return self.retriveR(key, self.root)

	def retriveR(self, item, cur):
		if cur == None:
			return None
		elif cur.data == item:
			return cur.data
		elif item < cur.data:
			return self.retriveR(item, cur.left)
		else:
			return self.retriveR(item, cur.right)


	def traverse(self, callback):
		self.traverseR(self.root, callback)

	def traverseR(self, cur, callback):
		if cur:
			callback(cur.data)
			self.traverseR(cur.left, callback)
			self.traverseR(cur.right, callback)
			
	def delete(self, data):
		if not self.exists(data):
			return False
		self.root = self.deleteR(data, self.root)
		self.count -= 1
		return True
		
	def deleteR(self, data, cur):
		if data < cur.data:
			cur.left = self.deleteR(data, cur.left)
		elif data > cur.data:
			cur.right = self.deleteR(data, cur.right)
		else:
			if cur.left == None and cur.right == None:
				cur = None
			elif cur.right == None:
				cur = cur.left
			elif cur.left == None:
				cur = cur.right
			else:
				lol = cur.right 
				while lol.left:
					lol = lol.left
				cur.data= lol.data
				cur.right = self.deleteR(lol.data, cur.right)
		return cur
			

	def count(self):
		return self.count

	def trueCount(self):
		self.count = 0
		self.countR(self.root)
		return self.count

	def countR(self, node):
		if node == None:
			return
		else:
			if node.right:
				self.count += 1
				self.countR(node.right)
			if node.left:
				self.count +=1
				self.countR(node.left)