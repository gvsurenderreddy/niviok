/* This file was generated by SableCC (http://www.sablecc.org/). */

package Dextr.Sablecc.node;

import java.util.*;
import Dextr.Sablecc.analysis.*;

public final class ABComparisonfunction extends PComparisonfunction
{
    private TKeywordLte _keyword_lte_;

    public ABComparisonfunction ()
    {
    }

    public ABComparisonfunction (
            TKeywordLte _keyword_lte_
    )
    {
        setKeywordLte (_keyword_lte_);
    }

    public Object clone()
    {
        return new ABComparisonfunction (
            (TKeywordLte)cloneNode (_keyword_lte_)
        );
    }

    public void apply(Switch sw)
    {
        ((Analysis) sw).caseABComparisonfunction(this);
    }

    public TKeywordLte getKeywordLte ()
    {
        return _keyword_lte_;
    }

    public void setKeywordLte (TKeywordLte node)
    {
        if(_keyword_lte_ != null)
        {
            _keyword_lte_.parent(null);
        }

        if(node != null)
        {
            if(node.parent() != null)
            {
                node.parent().removeChild(node);
            }

            node.parent(this);
        }

        _keyword_lte_ = node;
    }

    public String toString()
    {
        return ""
            + toString (_keyword_lte_)
        ;
    }

    void removeChild(Node child)
    {
        if ( _keyword_lte_ == child )
        {
            _keyword_lte_ = null;
            return;
        }
    }

    void replaceChild(Node oldChild, Node newChild)
    {
        if ( _keyword_lte_ == oldChild )
        {
            setKeywordLte ((TKeywordLte) newChild);
            return;
        }
    }

}
