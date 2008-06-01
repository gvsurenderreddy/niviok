/* This file was generated by SableCC (http://www.sablecc.org/). */

package Dextr.Sablecc.node;

import java.util.*;
import Dextr.Sablecc.analysis.*;

public final class AASimple extends PSimple
{
    private PBlock _block_;

    public AASimple ()
    {
    }

    public AASimple (
            PBlock _block_
    )
    {
        setBlock (_block_);
    }

    public Object clone()
    {
        return new AASimple (
            (PBlock)cloneNode (_block_)
        );
    }

    public void apply(Switch sw)
    {
        ((Analysis) sw).caseAASimple(this);
    }

    public PBlock getBlock ()
    {
        return _block_;
    }

    public void setBlock (PBlock node)
    {
        if(_block_ != null)
        {
            _block_.parent(null);
        }

        if(node != null)
        {
            if(node.parent() != null)
            {
                node.parent().removeChild(node);
            }

            node.parent(this);
        }

        _block_ = node;
    }

    public String toString()
    {
        return ""
            + toString (_block_)
        ;
    }

    void removeChild(Node child)
    {
        if ( _block_ == child )
        {
            _block_ = null;
            return;
        }
    }

    void replaceChild(Node oldChild, Node newChild)
    {
        if ( _block_ == oldChild )
        {
            setBlock ((PBlock) newChild);
            return;
        }
    }

}
