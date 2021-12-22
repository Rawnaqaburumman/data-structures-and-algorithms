# 563. Binary Tree Tilt
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findTilt(self, root: TreeNode) -> int:
        self.tilt = 0
        def findSum(root):
            if root == None: return 0
            l = findSum(root.left)
            r = findSum(root.right)
            self.tilt += abs(l-r)
            return l + r + root.val
        findSum(root)
        return self.tilt

#==================================================================
# 572. Subtree of Another Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        '''
        Depth first searches both trees and compares
        all nodes.
        Returns False whenever two different nodes
        encountered
        Returns True when both trees are completely
        explored and equal.
        '''
        def check_equal(tree1, tree2):
            if tree1 and not tree2 or tree2 and not tree1:
                return False
            elif tree1 and tree2:
                if tree1.val != tree2.val:
                    return False
                if not check_equal(tree1.left, tree2.left):
                    return False
                if not check_equal(tree1.right, tree2.right):
                    return False
            return True

        def explore(curr, t):
            if curr:
                # if a node which has same value as root s is encountered, we check for quality
                if curr.val == t.val and check_equal(curr, t):
                    return True
                if explore(curr.left, t):
                    return True
                if explore(curr.right, t):
                    return True

        return explore(s, t)

#==================================================================

# 589. N-ary Tree Preorder Traversal
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node', ans: list = None) -> List[int]:
        if not root: return ans
        if ans == None: ans = []
        ans.append(root.val)
        for child in root.children:
            self.preorder(child, ans)
        return ans


#======================================================================
# 590. N-ary Tree Postorder Traversal

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        def dfs(root, result):
            for child in root.children:
                if child:
                    dfs(child, result)
            result.append(root.val)

        result = []
        if root:
            dfs(root, result)
        return result



##
112. Path Sum
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        def helper(node, target):
            if node != None:
                target =target- node.val
            else:
                return False

            if(target == 0 and (node.left == node.right == None)):
                return True
            else:
                return helper(node.left, target) or helper(node.right, target)

        return helper(root, targetSum)


144. Binary Tree Preorder Traversal


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []

        def inorder(tree):
            if tree:
                result.append(tree.val)
                inorder(tree.left)
                inorder(tree.right)

        inorder(root)
        return result

145. Binary Tree Postorder Traversal

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []

        def inorder(tree):
            if tree:

                inorder(tree.left)
                inorder(tree.right)
                result.append(tree.val)
        inorder(root)
        return result

226. Invert Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            temp = root.left
            root.left = root.right
            root.right = temp
            root.left = self.invertTree(root.left)
            root.right = self.invertTree(root.right)
        return root


235. Lowest Common Ancestor of a Binary Sear

        # Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        if root.val > max(p.val, q.val):
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val < min(p.val, q.val):
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root


#
#637

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = [root]
        result = []
        while(q):
            summation = 0
            numberOfNode = len(q)
            for i in range(numberOfNode):
                node = q.pop(0)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                summation += node.val
            result.append(summation / numberOfNode)

        return result


#653
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:

        def inorder(tree):
            if tree:
                inorder(tree.left)
                arr.append(tree.val)
                inorder(tree.right)

        arr = []
        inorder(root)
        left = 0
        right = len(arr)-1
        while left < right:
            if arr[left]+arr[right] == k:
                return True
            elif arr[left]+arr[right] < k:
                left += 1
            else:
                right -= 1
        return False


#671
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        res = float("inf")
        nodequeue = [root]
        while nodequeue:
            node = nodequeue.pop()
            if node.left:
                if node.right.val != root.val:
                    small = node.right.val
                    res = min(res, small)
                nodequeue.append(node.left)
                if node.left.val != root.val:
                    small = node.left.val
                    res = min(res, small)
                nodequeue.append(node.right)
        return res if res != float("inf") else -1

#700
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        cur=root
        while cur:
            if cur.val==val:
                return cur
            if cur.val>val:
                cur=cur.left
            elif cur.val<val:
                cur=cur.right
        else:
            return None


#703
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k
        heapq. heapify(self.minHeap)
        while len(self.minHeap) > k:
             heapq.heappop(self.minHeap)


    def add(self, val: int) -> int:

        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)


#783
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        stack = []
        curr = root
        prev = None
        minimum = float('inf')
        while stack or curr:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                if prev:
                    minimum = min(minimum, curr.val - prev.val)
                prev = curr
                curr = curr.right
        return minimum


#

class Solution:
     def sumOfLeftLeaves(self,root,summing = 0):
        if root.left:
            if not root.left.left and not root.left.right:
                summing += root.left.val
            summing =self.sumOfLeftLeaves(root.left, summing)
        # summing -= root.left.val

        if root.right:
            summing =self.sumOfLeftLeaves(root.right, summing)

        return summing


class Solution:
    def binaryTreePaths(self, root):
        def dfs(root, output = ''):
            if not root:
                return "empty list"
            if not root.left and not root.right:
                tmp.append(f"{root.val}")
                res.append("->".join(tmp))
                tmp.pop()
                return
            tmp.append(f"{root.val}")
            dfs(root.left)
            dfs(root.right)
            tmp.pop()
        tmp = []
        res = []
        dfs(root)
        return res

# 404

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
     def sumOfLeftLeaves(self,root):

        def sum_leaves(root , summing):
            if root.left:
                if not root.left.left and not root.left.right:
                    summing += root.left.val
                summing = sum_leaves(root.left, summing)

            if root.right:
                summing =sum_leaves(root.right, summing)

            return summing
        return sum_leaves(root,0)


#637
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = [root]
        result = []
        while(q):
            summation = 0
            numberOfNode = len(q)
            for i in range(numberOfNode):
                node = q.pop(0)
                summation += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(summation / numberOfNode)

        return result


#other solution
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = deque([root])
        result = []
        while(q):
            summation = 0
            numberOfNode = len(q)
            for i in range(numberOfNode):
                node = q.popleft()
                summation += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(summation / numberOfNode)

        return result
# Binary tree path

class Solution:
    def binaryTreePaths(self, root):
        def dfs(root, output = ''):
            if not root:
                return "empty list"
            if not root.left and not root.right:
                tmp.append(str(root.val))
                res.append("->".join(tmp))
                tmp.pop()
                return
            tmp.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
            tmp.pop()
        tmp = []
        res = []
        dfs(root)
        return res


#653
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        # it will work only with in order and binary search tree
        def inorder(tree):
            if tree:
                inorder(tree.left)
                arr.append(tree.val)
                inorder(tree.right)
# it is sorted as in the left small num and in the right bigger
        arr = []
        inorder(root)
        left = 0
        #to take the last element in the array len(7)-1
        right = len(arr)-1

        while left < right:
            if arr[left]+arr[right] == k:
                return True
            # checking the num is grater than the left and the right we will increase the left other than that it will decrese the right
            elif arr[left]+arr[right] < k:
                   left += 1
            else:
                right -= 1


        return False
