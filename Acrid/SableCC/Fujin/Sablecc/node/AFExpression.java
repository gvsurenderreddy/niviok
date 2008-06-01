/* This file was generated by SableCC (http://www.sablecc.org/). */

package Dextr.Sablecc.node;

import java.util.*;
import Dextr.Sablecc.analysis.*;

public final class AFExpression extends PExpression
{
    private PForrange _forrange_;

    public AFExpression ()
    {
    }

    public AFExpression (
            PForrange _forrange_
    )
    {
        setForrange (_forrange_);
    }

    public Object clone()
    {
        return new AFExpression (
            (PForrange)cloneNode (_forrange_)
        );
    }

    public void apply(Switch sw)
    {
        ((Analysis) sw).caseAFExpression(this);
    }

    public PForrange getForrange ()
    {
        return _forrange_;
    }

    public void setForrange (PForrange node)
    {
        if(_forrange_ != null)
        {
            _forrange_.parent(null);
        }

        if(node != null)
        {
            if(node.parent() != null)
            {
                node.parent().removeChild(node);
            }

            node.parent(this);
        }

        _forrange_ = node;
    }

    public String toString()
    {
        return ""
            + toString (_forrange_)
        ;
    }

    void removeChild(Node child)
    {
        if ( _forrange_ == child )
        {
            _forrange_ = null;
            return;
        }
    }

    void replaceChild(Node oldChild, Node newChild)
    {
        if ( _forrange_ == oldChild )
        {
            setForrange ((PForrange) newChild);
            return;
        }
    }

}
