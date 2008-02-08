using System.Collections.Generic;

class Node_Or : INode_Expression {
	INode_Expression _first;
	INode_Expression _second;

	public Node_Or( INode_Expression first, INode_Expression second ) {
		_first = first;
		_second = second;
	}
	
	public IValue execute(Scope scope) {		
		IValue first = _first.execute(scope);
		//xxx downcast
		if( Bridge.unwrapBoolean(first) == true )
			return Bridge.wrapBoolean(true);
		
		IValue second = _second.execute(scope);
		//xxx downcast
		if( Bridge.unwrapBoolean(second) == true )
			return Bridge.wrapBoolean(true);
		
		return Bridge.wrapBoolean(false);
	}
	
	public void getInfo(out string name, out object objs) {
		name = "or";
		objs = new object[]{ _first, _second };
	}
}
