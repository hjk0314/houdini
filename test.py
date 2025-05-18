

""" Create geo Node """
# import hou
obj = hou.node("/obj")
if obj is not None:
    geo_node = obj.createNode("geo", "geo1")
    geo_node.moveToGoodPosition()


""" Change a specific parts to a primitive name. """
# node = hou.pwd()
# geo = node.geometry()
path_attr = geo.findPrimAttrib("path")
if path_attr is None:
    raise hou.NodeError("No 'path' attribute found")
for prim in geo.prims():
    p = prim.stringAttribValue("path")
    parts = p.split("/")
    prim.setAttribValue(path_attr, parts[-2])