/* This file was generated by SableCC (http://www.sablecc.org/). */

package Dextr.Sablecc.node;

import Dextr.Sablecc.analysis.*;

public final class TKeywordElif extends Token
{
    public TKeywordElif()
    {
        super.setText("elif");
    }

    public TKeywordElif(int line, int pos)
    {
        super.setText("elif");
        setLine(line);
        setPos(pos);
    }

    public Object clone()
    {
      return new TKeywordElif(getLine(), getPos());
    }

    public void apply(Switch sw)
    {
        ((Analysis) sw).caseTKeywordElif(this);
    }

    public void setText(String text)
    {
        throw new RuntimeException("Cannot change TKeywordElif text.");
    }
}
