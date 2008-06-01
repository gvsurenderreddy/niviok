/* This file was generated by SableCC (http://www.sablecc.org/). */

package Dextr.Sablecc.node;

import java.util.*;
import Dextr.Sablecc.analysis.*;

public final class ADBooleanfunction extends PBooleanfunction
{
    private TKeywordNor _keyword_nor_;

    public ADBooleanfunction ()
    {
    }

    public ADBooleanfunction (
            TKeywordNor _keyword_nor_
    )
    {
        setKeywordNor (_keyword_nor_);
    }

    public Object clone()
    {
        return new ADBooleanfunction (
            (TKeywordNor)cloneNode (_keyword_nor_)
        );
    }

    public void apply(Switch sw)
    {
        ((Analysis) sw).caseADBooleanfunction(this);
    }

    public TKeywordNor getKeywordNor ()
    {
        return _keyword_nor_;
    }

    public void setKeywordNor (TKeywordNor node)
    {
        if(_keyword_nor_ != null)
        {
            _keyword_nor_.parent(null);
        }

        if(node != null)
        {
            if(node.parent() != null)
            {
                node.parent().removeChild(node);
            }

            node.parent(this);
        }

        _keyword_nor_ = node;
    }

    public String toString()
    {
        return ""
            + toString (_keyword_nor_)
        ;
    }

    void removeChild(Node child)
    {
        if ( _keyword_nor_ == child )
        {
            _keyword_nor_ = null;
            return;
        }
    }

    void replaceChild(Node oldChild, Node newChild)
    {
        if ( _keyword_nor_ == oldChild )
        {
            setKeywordNor ((TKeywordNor) newChild);
            return;
        }
    }

}
