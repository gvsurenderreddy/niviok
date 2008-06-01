/* This file was generated by SableCC (http://www.sablecc.org/). */

package Dextr.Sablecc.node;

import Dextr.Sablecc.analysis.*;

public final class TOperatorOpeningParenthesis extends Token
{
    public TOperatorOpeningParenthesis()
    {
        super.setText("(");
    }

    public TOperatorOpeningParenthesis(int line, int pos)
    {
        super.setText("(");
        setLine(line);
        setPos(pos);
    }

    public Object clone()
    {
      return new TOperatorOpeningParenthesis(getLine(), getPos());
    }

    public void apply(Switch sw)
    {
        ((Analysis) sw).caseTOperatorOpeningParenthesis(this);
    }

    public void setText(String text)
    {
        throw new RuntimeException("Cannot change TOperatorOpeningParenthesis text.");
    }
}
