/* This file was generated by SableCC (http://www.sablecc.org/). */

package Dextr.Sablecc.node;

import Dextr.Sablecc.analysis.*;

public final class TKeywordGt extends Token
{
    public TKeywordGt()
    {
        super.setText("gt");
    }

    public TKeywordGt(int line, int pos)
    {
        super.setText("gt");
        setLine(line);
        setPos(pos);
    }

    public Object clone()
    {
      return new TKeywordGt(getLine(), getPos());
    }

    public void apply(Switch sw)
    {
        ((Analysis) sw).caseTKeywordGt(this);
    }

    public void setText(String text)
    {
        throw new RuntimeException("Cannot change TKeywordGt text.");
    }
}
