# coding: utf-8

"""
outputs the children of nodes that can appear more than once
e.g. "* foo bar" but not "? foo bar"
this is helpful in ensuring all plural names are not accidentially used
	for children than can appear more than once
"""

import sys
import string
import xml.dom.minidom as DOM

inputPath = "specs/docbook/Desal Semantics - Nodes.docbook"

#xxx need better way to store this information
#specType -> string (e.g. identifier -> INode_Expression)
superTypes = {}

#layout: specType-> children[]
#child: { "count", "specType", "specName" }
def extractLayouts(filePath) :
	def findLayouts(elem) :
		for child in elem.childNodes :
			if child.nodeType == DOM.Node.ELEMENT_NODE :
				findLayouts(child)
		if not elem.hasAttribute("role") :
			return
		role = elem.getAttribute("role")
		if role != "layout" :
			return
		outputLayout(elem)
	
	def outputLayout(elem) :
		specType = getTitle(elem)
		children = elem.getElementsByTagName("member")
		layouts[specType] = []
		for child in children :
			layouts[specType].append(
				parseChild(child.firstChild.nodeValue))
		superTypes[specType] = getSuperType(elem)
	
	def getTitle(elem) :
		if elem.nodeType != DOM.Node.ELEMENT_NODE :
			raise Exception("@elem must be an element")
		childTitles = elem.getElementsByTagName("title")
		if len(childTitles) == 0 :
			return getTitle(elem.parentNode)
		return childTitles[0].firstChild.nodeValue

	def parseChild(text) :
		child = {}
		tokens = text.split(" ")
		
		#count (e.g. *)
		if tokens[0] in ["*", "+", "?"] :
			child["count"] = tokens.pop(0)
		else :
			child["count"] = "1"
		
		#spec type (e.g. alpha-beta-gamma)
		child["specType"] = tokens.pop(0)
		
		#spec name (e.g. alpha beta gamma)
		if len(tokens) > 0 :
			child["specName"] = " ".join(tokens)
		else :
			child["specName"] = child["specType"].replace("-", " ")

		return child
	
	#@return - INode, INode_{ Expression, Declaration, ScopeAlteration }
	def getSuperType(elem) :
		def isNonExec(elem) :
			if elem.getAttribute("xml:id") == "non-executable" :
				return True
			if elem.parentNode.nodeType == DOM.Node.ELEMENT_NODE :
				return isNonExec(elem.parentNode)
			return False
		
		def isNestedNode(elem) :
			id = elem.getAttribute("xml:id") or ""
			if id.find("node.") == 0 :
				return True
			if elem.parentNode.nodeType == DOM.Node.ELEMENT_NODE :
				return isNestedNode(elem.parentNode)
			return False
		
		specType = getTitle(elem)
		
		if specType.find("declare") > -1 :
			return "INode_Declaration"
		if specType in ["using", "import", "expose"] :
			return "INode_ScopeAlteration"
		if isNonExec(elem) :
			return "INode"
		if isNestedNode(elem.parentNode.parentNode) :
			return "INode"
		else :
			return "INode_Expression"

	dom = DOM.parse(filePath)
	layouts = {}
	findLayouts(dom.documentElement)
	return layouts

def lowerCamelCase(text) :
	upperCamel = upperCamelCase(text)
	return string.lower(upperCamel[0]) + upperCamel[1:]

def upperCamelCase(text) :
	upperFirst = lambda t : string.upper(t[0]) + t[1:]
	return "".join(map(upperFirst, text.replace(" ", "-").split("-")))

layouts = extractLayouts(inputPath)

'''
#xxx remove types that I don't want to deal with yet
del layouts["interface"]
del layouts["class"]
del layouts["generic-interface"]
del layouts["generic-class"]
del layouts["statused-member"]
del layouts["comprehension"]
del layouts["bundle"]
del layouts["plane"]
'''

#map specType to csType e.g. foo-bar-baz to Node_FooBarBaz
csTypes = { #xxx temporary -- terminal nodes and family nodes -- need way to automate this
	"expression" : "INode_Expression",
	"declaration" : "INode_Declaration",
	"scope-alteration" : "INode_ScopeAlteration",
	
	"identifier" : "Node_Identifier",
	"boolean" : "Node_Boolean",
	"member-status" : "Node_MemberStatus",
	"interface-member" : "Node_InterfaceMember",
	"comprehension-type" : "Node_ComprehensionType",
	"access" : "Node_Access",
	"string" : "Node_String",
	"integer" : "Node_Integer",
	"direction" : "Node_Direction",
	"identikey-category" : "Node_IdentikeyCategory"
}
for specType in layouts :
	csTypes[specType] = "Node_%s" % upperCamelCase(specType)

#add csType and csName to children, e.g. IList<Node_FooBarBaz> and fooBarBaz
for specType in layouts :
	for child in layouts[specType] :
		child["csName"] = lowerCamelCase(child["specName"])
		csType = csTypes[child["specType"]]
		if child["count"] == "1" or child["count"] == "?" :
			child["csType"] = csType
		else :
			child["csType"] = "IList<%s>" % csType

for specType in layouts :
	foo = False
	for child in layouts[specType] :
		if child["count"] in ["*", "+"] and child["specType"] != child["specName"].replace(" ", "-") :
			foo = True
			print child["specName"], "(%s)" % specType
	if foo :
		print

