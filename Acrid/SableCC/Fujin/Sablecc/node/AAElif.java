/* This file was generated by SableCC (http://www.sablecc.org/). */

package Dextr.Sablecc.node;

import java.util.*;
import Dextr.Sablecc.analysis.*;

public final class AAElif extends PElif
{
    private TKeywordElif _keyword_elif_;
    private PIfexpr _ifexpr_;
    private PBlock _block_;

    public AAElif ()
    {
    }

    public AAElif (
            TKeywordElif _keyword_elif_,
            PIfexpr _ifexpr_,
            PBlock _block_
    )
    {
        setKeywordElif (_keyword_elif_);
        setIfexpr (_ifexpr_);
        setBlock (_block_);
    }

    public Object clone()
    {
        return new AAElif (
            (TKeywordElif)cloneNode (_keyword_elif_),
            (PIfexpr)cloneNode (_ifexpr_),
            (PBlock)cloneNode (_block_)
        );
    }

    public void apply(Switch sw)
    {
        ((Analysis) sw).caseAAElif(this);
    }

    public TKeywordElif getKeywordElif ()
    {
        return _keyword_elif_;
    }

    public void setKeywordElif (TKeywordElif node)
    {
        if(_keyword_elif_ != null)
        {
            _keyword_elif_.parent(null);
        }

        if(node != null)
        {
            if(node.parent() != null)
            {
                node.parent().removeChild(node);
            }

            node.parent(this);
        }

        _keyword_elif_ = node;
    }
    public PIfexpr getIfexpr ()
    {
        return _ifexpr_;
    }

    public void setIfexpr (PIfexpr node)
    {
        if(_ifexpr_ != null)
        {
            _ifexpr_.parent(null);
        }

        if(node != null)
        {
            if(node.parent() != null)
            {
                node.parent().removeChild(node);
            }

            node.parent(this);
        }

        _ifexpr_ = node;
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
            + toString (_keyword_elif_)
            + toString (_ifexpr_)
            + toString (_block_)
        ;
    }

    void removeChild(Node child)
    {
        if ( _keyword_elif_ == child )
        {
            _keyword_elif_ = null;
            return;
        }
        if ( _ifexpr_ == child )
        {
            _ifexpr_ = null;
            return;
        }
        if ( _block_ == child )
        {
            _block_ = null;
            return;
        }
    }

    void replaceChild(Node oldChild, Node newChild)
    {
        if ( _keyword_elif_ == oldChild )
        {
            setKeywordElif ((TKeywordElif) newChild);
            return;
        }
        if ( _ifexpr_ == oldChild )
        {
            setIfexpr ((PIfexpr) newChild);
            return;
        }
        if ( _block_ == oldChild )
        {
            setBlock ((PBlock) newChild);
            return;
        }
    }

}
