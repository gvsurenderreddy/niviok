/* This file was generated by SableCC (http://www.sablecc.org/). */

package Dextr.Sablecc.node;

import Dextr.Sablecc.analysis.*;

public final class TKeywordTo extends Token
{
    public TKeywordTo()
    {
        super.setText("to");
    }

    public TKeywordTo(int line, int pos)
    {
        super.setText("to");
        setLine(line);
        setPos(pos);
    }

    public Object clone()
    {
      return new TKeywordTo(getLine(), getPos());
    }

    public void apply(Switch sw)
    {
        ((Analysis) sw).caseTKeywordTo(this);
    }

    public void setText(String text)
    {
        throw new RuntimeException("Cannot change TKeywordTo text.");
    }
}
