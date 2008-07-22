/* This file was generated by SableCC (http://www.sablecc.org/). */

using System;
using System.Collections;
using System.Text;

namespace Acrid.Ivan.SableCC.node {

public abstract class Node : Switchable, ICloneable
{
    private Node parent_node;

    public abstract Object Clone();
    public abstract void Apply (Switch s);

    public Node Parent()
    {
        return parent_node;
    }

    internal void Parent(Node parent_node)
    {
        this.parent_node = parent_node;
    }

    internal abstract void RemoveChild(Node child);
    internal abstract void ReplaceChild(Node oldChild, Node newChild);

    public void ReplaceBy(Node node)
    {
        if(parent_node != null)
        {
            parent_node.ReplaceChild(this, node);
        }
    }

    protected string ToString(Node node)
    {
        if(node != null)
        {
            return node.ToString();
        }

        return "";
    }

    protected string ToString(IList list)
    {
        StringBuilder s = new StringBuilder();

        foreach (Node n in list)
        {
            s.Append(n.ToString());
        }

        return s.ToString();
    }

    protected Node CloneNode(Node node)
    {
        if(node != null)
        {
            return (Node) node.Clone();
        }

        return null;
    }

    protected IList CloneList(IList list)
    {
        // list not owned by anyone so no need for TypedList
        IList clone = new ArrayList();

        foreach (Node n in list)
        {
            clone.Add(n.Clone());
        }

        return clone;
    }
}

internal interface Cast
{
    Object Cast(Object o);      // take ownership
    Object UnCast(Object o);    // release ownership
}

internal class NodeCast : Cast
{
    private static NodeCast instance = new NodeCast();

    public static NodeCast Instance
    {
      get { return instance; }
    }

    private NodeCast()
    {
    }

    public Object Cast(Object o)
    {
        return (Node) o;
    }

    public Object UnCast(Object o)
    {
        return o;
    }
}

internal class NoCast : Cast
{
    private static NoCast instance = new NoCast();

    public static NoCast Instance
    {
      get { return instance; }
    }

    private NoCast()
    {
    }

    public Object Cast(Object o)
    {
        return o;
    }

    public Object UnCast(Object o)
    {
        return o;
    }
}

public interface Switch
{
}

public interface Switchable
{
    void Apply(Switch sw);
}

public class TypedList : IList
{
    private ArrayList list;
    private Cast cast;

    public TypedList()
    {
        list = new ArrayList();
        cast = NoCast.Instance;
    }

    public TypedList(ICollection c)
    {
        list = new ArrayList ();
        cast = NoCast.Instance;
        AddAll(c);
    }

    internal TypedList(Cast cast)
    {
        list = new ArrayList ();
        this.cast = cast;
    }

    internal TypedList(ICollection c, Cast cast)
    {
        list = new ArrayList ();
        this.cast = cast;
        AddAll(c);
    }

    internal Cast GetCast()
    {
        return cast;
    }

    public int Add(Object o)
    {
        return list.Add(cast.Cast(o));
    }

    public void AddAll (ICollection c)
    {
        foreach (Node n in c)
        {
          list.Add(cast.Cast(n));
        }
    }

    public int Count
    {
      get { return list.Count; }
    }

    public bool IsSynchronized
    {
      get { return list.IsSynchronized; }
    }

    public Object SyncRoot
    {
      get { return list.SyncRoot; }
    }

    public void CopyTo(Array array, int index)
    {
      list.CopyTo (array, index);
    }

    public bool IsFixedSize
    {
      get { return list.IsFixedSize; }
    }

    public bool IsReadOnly
    {
      get { return list.IsReadOnly; }
    }

    public Object this[int index]
    {
      get { return list[index]; }
      set { list[index] = cast.Cast(value); }
    }

    public IEnumerator GetEnumerator()
    {
      return list.GetEnumerator();
    }

    public void Clear ()
    {
      foreach (Node n in list)
          cast.UnCast(n);
      list.Clear();
    }

    public bool Contains (Object value)
    {
      return list.Contains(value);
    }

    public int IndexOf (Object value)
    {
      return list.IndexOf(value);
    }

    public void Insert (int index, Object value)
    {
      list.Insert(index, cast.Cast(value));
    }

    public void Remove (Object value)
    {
      int n = list.IndexOf(value);
      if ( n != -1 )
          RemoveAt(n);  // this will UnCast
    }

    public void RemoveAt (int index)
    {
      cast.UnCast(list[index]);
      list.RemoveAt(index);
    }
}
} // namespace Acrid.Ivan.SableCC.node
