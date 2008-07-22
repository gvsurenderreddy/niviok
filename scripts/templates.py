#templates for use by "code generator.py"

warning = """
//THIS FILE WAS GENERATED PROGRAMMATICALLY.
//DO NOT EDIT THIS FILE DIRECTLY.
//CHANGES TO THIS FILE WILL BE OVERRIDDEN.
""".strip()

csHeader = warning + "\n\n" + """
using System;
using System.Collections.Generic;
""".strip()


#---- NODE CLASSES

nodeClassFile = csHeader + """

namespace Acrid.NodeTypes {

%s

} //namespace

"""

nodeClass = """
public class %(csType)s : %(inherit)s {
	%(fields)s
	string m_nodeSource;
	
	public %(csType)s(
	%(parameters)s,
	string @nodeSource ) {
		%(assignments)s
		m_nodeSource = @nodeSource;
	}
	
	%(getters)s

	public string typeName {
		get { return "%(specType)s"; }
	}
	
	public ICollection<INode> childNodes {
		get {
			return G.collect<INode>(
				%(fieldList)s );
		}
	}
	
	public string @nodeSource {
		get { return m_nodeSource; }
	}
}
""".strip()

nodeGetter = """
	public %(csType)s @%(csName)s {
		get { return m_%(csName)s; }
	}
""".strip()


#----- DESIBLE PARSER

desibleParserFile = csHeader + """
using System.Xml;
using Acrid.NodeTypes;

namespace Acrid.Desible {

public abstract class DesibleParserAuto : DesibleParserBase {
	%s
}

} //namespace

"""

desibleFamilyParser = """
	protected virtual %(csTypename)s parse%(csName)s(XmlElement element) {
		switch(element.LocalName) {
			%%s
			default:
				throw new ParseError(
					String.Format(
						"element with name '{0}' is not recognized as a %(csName)s node",
						element.LocalName),
					getSource(element));
		}
	}
""".strip()

desibleFamilyCase = """
			case "%(typename)s":
				return parse%(csName)s(element);
""".strip()

desibleTerminalParser = """
	protected virtual %(csTypename)s parse%(csName)s(XmlElement element) {
		checkElement(element, "%(typename)s");
		return new %(csTypename)s(element.InnerText, getSource(element));
	}
""".strip()

desibleTreeParser = """
	protected virtual %(csTypename)s parse%(csName)s(XmlElement element) {
		checkElement(element, "%(typename)s");
		return new %(csTypename)s(
			%%s,
			getSource(element) );
	}
""".strip()

desibleTreeParserCall = '%s<%s>(parse%s, element, %s, %s)'


#----- DESIBLE SERIALIZER

desibleSerializerFile = csHeader + """
using System.Xml;
using Acrid.NodeTypes;

namespace Acrid.Desible {

public abstract class DesibleSerializerAuto : DesibleSerializerBase {
	%(methods)s
	
	protected XmlElement serializeAny(INode node) {
		switch(node.typeName) {
			%(cases)s
			default:
				throw new ApplicationException(
					String.Format(
						"can't serialize node of type {0} from {1}",
						node.typeName,
						node.nodeSource));
		}
	}
}

} //namespace

"""

desibleSerializerTerminal = """
	protected virtual XmlElement serialize(%(csTypename)s node) {
		XmlElement elem = _doc.CreateElement(node.typeName, desible1NS);
		elem.AppendChild(_doc.CreateTextNode(node.ToString()));
		return elem;
	}
""".strip()

desibleSerializerTree = """
	protected virtual XmlElement serialize(%(csTypename)s node) {
		XmlElement elem = _doc.CreateElement(node.typeName, desible1NS);
		%%s
		return elem;
	}
""".strip()

desibleSerializerCase = """
			case "%(typename)s":
				return serialize((%(csTypename)s)node);
""".strip()


#----- IVAN GRAMMAR

ivanGrammarFamilyProduction = """
	%(familyName)s {-> %(familyName)s}
		= %(options)s ;
""".strip()
	
ivanGrammarFamilyOption = """
		{%(optionName)s} %(optionName)s
			{-> New %(familyName)s.%(optionName)s(%(optionName)s)}
""".strip()

ivanGrammarTreeANode = """
	%(name)s
		= %(entries)s ;
""".strip()


#----- IVAN PARSER

ivanParserFile = csHeader + """
using Acrid.NodeTypes;
using Acrid.Ivan.SableCC.node;

namespace Acrid.Ivan {

public abstract class IvanParserAuto : IvanParserBase {
	%s
}

} //namespace

"""

ivanFamilyParser = """
	protected virtual %(csTypename)s parse%(csName)s(%%(sableName)s node) {
		%%(ifs)s
		else
			throw new Exception("unknown node type: " + node);
	}
""".strip()

ivanFamilyIfTree = """
		if( node is A%%(childSableName)s%%(parentSableName)s )
			return parse%(csName)s( (A%%(childSableName)s)(node as A%%(childSableName)s%%(parentSableName)s).Get%%(childSableName)s() );
""".strip()

ivanFamilyIfTerminal = """
		if( node is A%%(childSableName)s%%(parentSableName)s )
			return parse%(csName)s( (node as A%%(childSableName)s%%(parentSableName)s).Get%%(childSableName)s() );
""".strip()

ivanTerminalParser = """
	protected virtual %(csTypename)s parse%(csName)s(T%%(sableName)s node) {
		return new %(csTypename)s(
			node.Text,
			getSource(node));
	}
""".strip()

ivanTerminalEnumParser = """
	protected abstract %(csTypename)s parse%(csName)s(P%%(sableName)s node);
""".strip()

ivanTreeParser = """
	protected virtual %(csTypename)s parse%(csName)s(A%%(sableName)s node) {
		return new %(csTypename)s(
			%%(calls)s,
			getSource(node));
	}
""".strip()

ivanTreeParserCall = '%s<%s,%s>(parse%s, %snode.Get%s())'


#----- TOY PARSER

toyParserFile = csHeader + """
using Acrid.NodeTypes;

namespace Acrid.Toy {

public abstract class ToyParserAuto : ToyParserBase {
	%s
}

} //namespace

"""

toyFamilyParser = """
	protected virtual %(csTypename)s parse%(csName)s(Sexp sexp) {
		if( sexp.type != SexpType.LIST )
			return parseTerminal%(csName)s(sexp);
		if( sexp.list.Count == 0 )
			throw new ParseError(
				"this list cannot be empty",
				getSource(sexp));
		if( sexp.list.First.Value.type != SexpType.WORD )
			return parseNonword%(csName)s(sexp);
		Sexp first = sexp.list.First.Value;
		string specType = first.atom;
		sexp.list.RemoveFirst();
		switch(specType) {
			%%s
			default:
				sexp.list.AddFirst(first);
				return parse%(csName)sDefault(sexp);
		}
	}
	protected virtual %(csTypename)s parseTerminal%(csName)s(Sexp sexp) {
		throw new ParseError(
			"%(csName)s expression must be a list",
			getSource(sexp));
	}
	protected virtual %(csTypename)s parseNonword%(csName)s(Sexp sexp) {
		throw new ParseError(
			"expression must begin with a word",
			getSource(sexp));
	}
	protected virtual %(csTypename)s parse%(csName)sDefault(Sexp sexp) {
		throw new ParseError(
			String.Format(
				"unknown type of %(csName)s '{0}'",
				sexp.list.First.Value.atom),
			getSource(sexp));
	}
""".strip()

toyFamilyCase = """
			case "%(typename)s":
				return parse%(csName)s(sexp);
""".strip()

toyTerminalParser = """
	protected virtual %(csTypename)s parse%(csName)s(Sexp sexp) {
		try {
			return new %(csTypename)s(sexp.atom, getSource(sexp));
		}
		catch(FormatException e) {
			throw new ParseError(
				String.Format(
					"node of type %(csName)s cannot be of value '{0}'",
					sexp.atom),
				getSource(sexp),
				e);
		}
		catch(ArgumentException e) {
			throw new ParseError(
				String.Format(
					"node of type %(csName)s cannot be of value '{0}'",
					sexp.atom),
				getSource(sexp),
				e);
		}
	}
""".strip()

toyTreeParser = """
	protected virtual %(csTypename)s parse%(csName)s(Sexp sexp) {
		if( sexp.list.Count != %%(childCount)s )
			throw new ParseError(
				String.Format(
					"'%(typename)s' node must have %%(childCount)s children ({0} given)",
					sexp.list.Count),
				getSource(sexp));
		return new %(csTypename)s(
   			%%(childNodes)s,
			getSource(sexp) );
	}
""".strip()

toyTreeParserCall = '%s<%s>(parse%s, sexp)'


#----- EXECUTOR

executorFile = csHeader + """
using Acrid.NodeTypes;

namespace Acrid.Execution {

public static partial class Executor {
	public static IWorker executeAny(INode_Expression node, IScope scope) {
		switch(node.typeName) {
			%s
			default:
				throw new ApplicationException(String.Format(
					"can't execute node of type '{0}'",
					node.typeName));
		}
	}
}

} //namespace

"""

executorCase = """
			case "%(typename)s":
				return execute((%(csTypename)s)node, scope);
""".strip()
