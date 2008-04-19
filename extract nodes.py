"""
extracts the node layout information from the Desam spec
and writes it out to an XML file
"""

import os
import xml.dom.minidom as DOM
from lib import *

desalBase = "/media/files/Desal"
inputPath = os.path.join(desalBase,"specs/docbook/Desal Semantics - Nodes.docbook")
outputPath = os.path.join(desalBase,"nodes.xml")

#@return: array of NodeType objects
#NodeType: { category:"family", typename:String, members:[String] }
#NodeType: { category:"tree", typename:String, layout:[LayoutEntry] }
#NodeType: { category:"terminal", typename:String }
#LayoutEntry: { count:String, typename:String, ?label:String }
def extractNodeTypes(filePath) :
	def definesNode(elem) :
		return elem.getAttribute("xml:id").find("node.") == 0
	
	def isFamily(node) :
		return hasAncestorElement(
			node, lambda x: x.getAttribute("xml:id") == "family-node-types" )
	
	def isTree(elem) :
		for child in childElements(elem) :
			if child.getAttribute("role") == "layout" :
				return True
		return False
	
	def getTitle(elem) :
		assert definesNode(elem)
		return textValue(elem.getElementsByTagName("title")[0])

	def isExpressionNodeType(elem) :
		def isNonExec(elem) :
			return hasAncestorElement(
				elem, lambda x: x.getAttribute("xml:id") == "non-executable" )
		
		def isNestedNode(elem) :
			return hasAncestorElement(
				elem, lambda x: x.getAttribute("xml:id").find("node.") == 0 )
		
		assert definesNode(elem)

		return \
			not isFamily(elem) and \
			not isNonExec(elem) and \
			not isNestedNode(elem.parentNode)
	
	def extractFamilyType(sectElem) :
		def findTypes() :
			listElem = filter(
				lambda x: x.getAttribute("role") == "family-contents",
				childElements(sectElem) )[0]
			return map(
				textValue, childElements(listElem))
		
		typename = getTitle(sectElem)
		if typename == "expression" :
			types = expressionNodeTypes
		else :
			types = findTypes()
		
		return {
			"category" : "family",
			"typename" : typename,
			"members" : types
		}
	
	def extractTreeType(sectElem) :
		def parseChild(member) :
			text = textValue(member)
			tokens = text.split(" ")
			child = {}
			
			#count (e.g. *)
			if tokens[0] in ["*", "+", "?"] :
				child["count"] = tokens.pop(0)
			else :
				child["count"] = "1"
			
			#typename (e.g. "alpha-beta-gamma")
			child["typename"] = tokens.pop(0)
			
			#label (e.g. "alpha beta gamma")
			if len(tokens) > 0 :
				child["label"] = " ".join(tokens)
	
			return child
		
		layoutElem = filter(
			lambda x: x.getAttribute("role") == "layout",
			childElements(sectElem) )[0]
		members = layoutElem.getElementsByTagName("member")
		
		return {
			"category" : "tree",
			"typename" : getTitle(sectElem),
			"layout" : map(parseChild, members)
		}
	
	def extractTerminalType(elem) :
		return {
			"category" : "terminal",
			"typename" : getTitle(elem)
		}
	
	def extractNodeType(elem) :
		assert definesNode(elem)
		
		if isExpressionNodeType(elem) :
			expressionNodeTypes.append(getTitle(elem))
		if isFamily(elem) :
			return extractFamilyType(elem)
		elif isTree(elem) :
			return extractTreeType(elem)
		else :
			return extractTerminalType(elem)

	doc = DOM.parse(filePath)
	expressionNodeTypes = [] #modified by nested functions
	nodeElems = filter(definesNode, descendantElements(doc))
	nodeTypes = map(extractNodeType, nodeElems)
	return nodeTypes

def serializeNodeTypes(nodeTypes, path) :
	def append(parentNode, tagName, content) :
		doc = parentNode.ownerDocument
		child = doc.createElement(tagName)
		if content != None :
			child.appendChild(doc.createTextNode(content))
		parentNode.appendChild(child)
		return child

	def appendToRoot(tagName, nodeType) :
		elem = append(doc.documentElement, tagName, None)
		append(elem, "typename", nodeType["typename"])
		return elem

	def appendFamilyNodeType(nodeType) :
		elem = appendToRoot("family", nodeType)
		membersElem = append(elem, "members", None)
		for type in nodeType["members"] :
			append(membersElem, "typename", type)
	
	def appendTreeNodeType(nodeType) :
		elem = appendToRoot("tree", nodeType)
		for layoutEntry in nodeType["layout"] :
			entryElem = append(elem, "entry", None)
			append(entryElem, "count", layoutEntry["count"])
			append(entryElem, "typename", layoutEntry["typename"])
			if "label" in layoutEntry :
				append(entryElem, "label", layoutEntry["label"])

	def appendNodeType(nodeType) :
		if nodeType["category"] == "family" :
			appendFamilyNodeType(nodeType)
		elif nodeType["category"] == "tree" :
			appendTreeNodeType(nodeType)
		else :
			assert nodeType["category"] == "terminal"
			appendToRoot("terminal", nodeType)
	
	doc = DOM.parseString("<node-types/>")
	for nodeType in nodeTypes :
		appendNodeType(nodeType)
	file = open(path, "w")
	doc = DOM.parseString(doc.toprettyxml())
	for elem in doc.getElementsByTagName("*") :
		if len(elem.getElementsByTagName("*")) == 0 :
			elem.firstChild.nodeValue = elem.firstChild.nodeValue.strip()
	file.write(doc.toxml())
	file.close()


#----- entry point

nodeTypes = extractNodeTypes(inputPath)

#ensure no types are listed twice (it's happened)
typenames = set(map(lambda x: x["typename"], nodeTypes))
assert len(nodeTypes) == len(typenames)

serializeNodeTypes(nodeTypes, outputPath)