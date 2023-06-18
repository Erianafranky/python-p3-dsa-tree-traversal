class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, id):
    return self._dfs_find_node(self.root, id)
  
  def _dfs_find_node(self, node, id):
    if node is None:
      return None

    if node['id'] == id:
      return node

    for child in node['children']:
      result = self._dfs_find_node(child, id)
      if result:
        return result

    return None
