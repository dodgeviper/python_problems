class Node(object):
	def __init__(self, data):
		self.data = data
		self.right = None
		self.left = None
		self.parent = None


class BinarySearchTree(object):
	def __init__(self):
		self.root = None

	"""
	INSERT happens in O(ln(n)) time
	"""
	def insert(self, data):
		new_node = Node(data)
		if self.root == None:
			self.root = new_node
		else:
			node = self.root
			while node is not None:
				(new_word, new_w_count) = new_node.data
				(word, w_count) = node.data
				if ((new_w_count > w_count) 
					or (new_w_count == w_count and new_word < word)):
					if node.left is None:
						new_node.parent = node
						node.left = new_node
						break
					else:
						node = node.left
				else:
					if node.right is None:
						new_node.parent = node
						node.right = new_node
						break
					else:
						node = node.right


def count_words(s, n):
	"""
	The return value should be a list of tuples - the top n words
	paired with their respective counts, sorted in descending count order
	"""
	wordset = set(s.split())
	wordlist = s.split()
	bst = BinarySearchTree()
	for x in wordset:
		bst.insert((x, wordlist.count(x)))
	inorder_list = list()
	def fetch_list(node):
		if node is not None:
			fetch_list(node.left)
			inorder_list.append(node.data)
			fetch_list(node.right)
	fetch_list(bst.root)
	def sort_count(data):	w,c =data; return c;
	#return sorted(inorder_list, reverse=True, key=sort_count)[:n]
	return inorder_list[:n]
	

def test():
	s, n = "betty bought a bit of butter but the butter was bitter", 3
	assert count_words(s, n) == [('butter', 2), ('a', 1), ('betty', 1)]
	s, n = "cat bat mat cat bat cat", 3
	assert count_words(s, n) == [('cat', 3), ('bat', 2), ('mat', 1)]
	print 'tests pass'

test()
