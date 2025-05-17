# import hou


obj = hou.node("/obj")
if obj is not None:
    geo_node = obj.createNode("geo", "geo1")
    geo_node.moveToGoodPosition()

