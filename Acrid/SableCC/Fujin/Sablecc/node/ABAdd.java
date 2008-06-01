/* This file was generated by SableCC (http://www.sablecc.org/). */

package Dextr.Sablecc.node;

import java.util.*;
import Dextr.Sablecc.analysis.*;

public final class ABAdd extends PAdd
{
    private PAdd _add_;
    private TOperatorPlus _operator_plus_;
    private PMult _mult_;

    public ABAdd ()
    {
    }

    public ABAdd (
            PAdd _add_,
            TOperatorPlus _operator_plus_,
            PMult _mult_
    )
    {
        setAdd (_add_);
        setOperatorPlus (_operator_plus_);
        setMult (_mult_);
    }

    public Object clone()
    {
        return new ABAdd (
            (PAdd)cloneNode (_add_),
            (TOperatorPlus)cloneNode (_operator_plus_),
            (PMult)cloneNode (_mult_)
        );
    }

    public void apply(Switch sw)
    {
        ((Analysis) sw).caseABAdd(this);
    }

    public PAdd getAdd ()
    {
        return _add_;
    }

    public void setAdd (PAdd node)
    {
        if(_add_ != null)
        {
            _add_.parent(null);
        }

        if(node != null)
        {
            if(node.parent() != null)
            {
                node.parent().removeChild(node);
            }

            node.parent(this);
        }

        _add_ = node;
    }
    public TOperatorPlus getOperatorPlus ()
    {
        return _operator_plus_;
    }

    public void setOperatorPlus (TOperatorPlus node)
    {
        if(_operator_plus_ != null)
        {
            _operator_plus_.parent(null);
        }

        if(node != null)
        {
            if(node.parent() != null)
            {
                node.parent().removeChild(node);
            }

            node.parent(this);
        }

        _operator_plus_ = node;
    }
    public PMult getMult ()
    {
        return _mult_;
    }

    public void setMult (PMult node)
    {
        if(_mult_ != null)
        {
            _mult_.parent(null);
        }

        if(node != null)
        {
            if(node.parent() != null)
            {
                node.parent().removeChild(node);
            }

            node.parent(this);
        }

        _mult_ = node;
    }

    public String toString()
    {
        return ""
            + toString (_add_)
            + toString (_operator_plus_)
            + toString (_mult_)
        ;
    }

    void removeChild(Node child)
    {
        if ( _add_ == child )
        {
            _add_ = null;
            return;
        }
        if ( _operator_plus_ == child )
        {
            _operator_plus_ = null;
            return;
        }
        if ( _mult_ == child )
        {
            _mult_ = null;
            return;
        }
    }

    void replaceChild(Node oldChild, Node newChild)
    {
        if ( _add_ == oldChild )
        {
            setAdd ((PAdd) newChild);
            return;
        }
        if ( _operator_plus_ == oldChild )
        {
            setOperatorPlus ((TOperatorPlus) newChild);
            return;
        }
        if ( _mult_ == oldChild )
        {
            setMult ((PMult) newChild);
            return;
        }
    }

}
