from timeit import default_timer as timer

class Node:
    def __init__(self, val):
        self.YoutubeViews = val.YoutubeViews
        self.Track=val
        self.left = None
        self.right = None

class PagodaClass:
    def __init__(self):
        self.root = None
        
    def isEmpty(self):
        return self.root == None
        
    def clear(self):
        self.root = None
        
    def insert(self, val):
        node = Node(val)
        self.root = self._insert(node, self.root)
        
    def _insert(self, node, queue):
        node.left = node
        node.right = node
        return self._merge(queue, node)
        
    def _merge(self, root, newnode):
        if root == None:
            return newnode
        elif newnode == None:
            return root
        else:
            botroot = root.right
            root.right = None
            botnew = newnode.left
            newnode.left = None
            r = None
            while botroot != None and botnew != None:
                if botroot.YoutubeViews < botnew.YoutubeViews:
                    temp = botroot.right
                    if r == None:
                        botroot.right = botroot
                    else:
                        botroot.right = r.right
                        r.right = botroot
                    r = botroot
                    botroot = temp
                else:
                    temp = botnew.left
                    if r == None:
                        botnew.left = botnew
                    else:
                        botnew.left = r.left
                        r.left = botnew
                    r = botnew
                    botnew = temp
            if botnew == None:
                root.right = r.right
                r.right = botroot
                return root
            else:
                newnode.left = r.left
                r.left = botnew
                return newnode
        
    def delete(self):
        self.root = self._delete(self.root)
    
    def _delete(self, queue):
        if queue == None:
            print("Empty")
            return None
        else:
            if queue.left == queue:
                l = None
            else:
                l = queue.left
                while l.left != queue:
                    l = l.left
                l.left = queue.left
            if queue.right == queue:
                r = None
            else:
                r = queue.right
                while r.right != queue:
                    r = r.right
                r.right = queue.right
            return self._merge(l, r)
        
    def printRoot(self):
        if self.root != None:
            print(self.root.data)

    def findextremes(self,e):
        if e==1:
            return self.root

