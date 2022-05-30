"""Tree DFS recursive approach time and space complexity O(n)
            linear approach has same time and space complexity"""
from tree_node import TreeNode

def dfs(root, target, path=()):
  path = path + (root,)

  if root.value == target:
    return path

  for child in root.children:
    path_found = dfs(child, target, path)

    if path_found is not None:
      return path_found

  return None
        


sample_root_node = TreeNode("Home")
docs = TreeNode("Documents")
photos = TreeNode("Photos")
sample_root_node.children = [docs, photos]
my_wish = TreeNode("WishList.txt")
my_todo = TreeNode("TodoList.txt")
my_cat = TreeNode("Fluffy.jpg")
my_dog = TreeNode("Spot.jpg")
docs.children = [my_wish, my_todo]
photos.children = [my_cat, my_dog]

print(sample_root_node)
# Change the 2nd argument below
goal_path = dfs(sample_root_node, "Fluffy.jpg")
if goal_path is None:
  print("No path found")
else:
  print("Path found")
  for node in goal_path:
    print(node.value)




path = dfs(sample_root_node, "F")
print(path)