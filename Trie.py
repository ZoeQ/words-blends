#https://blog.csdn.net/ANNILingMo/article/details/80879910
class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = {}
        self.is_word = False

class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        for chars in word:
            child = node.data.get(chars)
            if not child:
                node.data[chars] = TrieNode()
            node = node.data[chars]
        node.is_word = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for chars in word:
            node = node.data.get(chars)
            if not node:
                return False
        return node.is_word  #

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for chars in prefix:
            node = node.data.get(chars)
            if not node:
                return False
        return True

    def getstart(self, prefix):
        """
          Returns words started with prefix
          :param prefix:
          :return: words (list)
        """

        def get_key(pre, pre_node):
            word_list = []
            if pre_node.is_word:
                word_list.append(pre)
            for x in pre_node.data.keys():
                word_list.extend(get_key(pre + str(x), pre_node.data.get(x)))
            return word_list

        words = []
        if not self.startsWith(prefix):
            return words
        if self.search(prefix):
            words.append(prefix)
            return words
        node = self.root
        for chars in prefix:
            node = node.data.get(chars)
        return get_key(prefix, node)


