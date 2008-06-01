/* This file was generated by SableCC (http://www.sablecc.org/). */

package Dextr.Sablecc.node;

import java.util.*;
import Dextr.Sablecc.analysis.*;

public final class AHExpression extends PExpression
{
    private PIfelse _ifelse_;

    public AHExpression ()
    {
    }

    public AHExpression (
            PIfelse _ifelse_
    )
    {
        setIfelse (_ifelse_);
    }

    public Object clone()
    {
        return new AHExpression (
            (PIfelse)cloneNode (_ifelse_)
        );
    }

    public void apply(Switch sw)
    {
        ((Analysis) sw).caseAHExpression(this);
    }

    public PIfelse getIfelse ()
    {
        return _ifelse_;
    }

    public void setIfelse (PIfelse node)
    {
        if(_ifelse_ != null)
        {
            _ifelse_.parent(null);
        }

        if(node != null)
        {
            if(node.parent() != null)
            {
                node.parent().removeChild(node);
            }

            node.parent(this);
        }

        _ifelse_ = node;
    }

    public String toString()
    {
        return ""
            + toString (_ifelse_)
        ;
    }

    void removeChild(Node child)
    {
        if ( _ifelse_ == child )
        {
            _ifelse_ = null;
            return;
        }
    }

    void replaceChild(Node oldChild, Node newChild)
    {
        if ( _ifelse_ == oldChild )
        {
            setIfelse ((PIfelse) newChild);
            return;
        }
    }

}
