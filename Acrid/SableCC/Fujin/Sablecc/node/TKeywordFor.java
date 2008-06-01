/* This file was generated by SableCC (http://www.sablecc.org/). */

package Dextr.Sablecc.node;

import Dextr.Sablecc.analysis.*;

public final class TKeywordFor extends Token
{
    public TKeywordFor()
    {
        super.setText("for");
    }

    public TKeywordFor(int line, int pos)
    {
        super.setText("for");
        setLine(line);
        setPos(pos);
    }

    public Object clone()
    {
      return new TKeywordFor(getLine(), getPos());
    }

    public void apply(Switch sw)
    {
        ((Analysis) sw).caseTKeywordFor(this);
    }

    public void setText(String text)
    {
        throw new RuntimeException("Cannot change TKeywordFor text.");
    }
}
