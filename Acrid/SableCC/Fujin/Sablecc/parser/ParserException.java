/* This file was generated by SableCC (http://www.sablecc.org/). */

package Dextr.Sablecc.parser;

import Dextr.Sablecc.node.*;

public class ParserException extends Exception
{
    Token token;

    public ParserException(Token token, String  message)
    {
        super(message);
        this.token = token;
    }

    public Token getToken()
    {
        return token;
    }
}
