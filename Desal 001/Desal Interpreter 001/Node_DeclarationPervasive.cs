class Node_DeclarationPervasive : INode_DeclarationAny {
	Node_Identifier _identNode;
	Node_ReferenceType _typeNode;
	INode_Expression _valueNode;
	
	public Node_DeclarationPervasive(
	Node_Identifier identNode, Node_ReferenceType typeNode, INode_Expression valueNode) {
		_identNode = identNode;
		_typeNode = typeNode;
		_valueNode = valueNode;
	}
	
	public IValue evaluate(ref Scope scope) {
		IValue val = _valueNode.evaluate(ref scope);
		scope.declarePervasive(
			_identNode.identifier,
			_typeNode.evaluateType(ref scope),
			val );
		return val;
	}
	
	public void execute(ref Scope scope) {
		evaluate(ref scope);
	}

	public void getInfo(out string name, out object objs) {
		name = "declaration-pervasive";
		objs = new object[]{ _identNode, _typeNode, _valueNode };
	}
}