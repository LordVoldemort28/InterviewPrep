package technical.lowleveldesign;

import java.util.HashMap;
import java.util.Map;
import java.util.Stack;

/**
* This is the interface for the expression tree Node.
* You should not remove it, and you can define some classes to implement it.
*/

abstract class Node {
        
    public abstract int evaluate();
    // define your fields here
}

interface Operation {

    int evaluate(int op1, int op2);

}


class Addition implements Operation {

    @Override
    public int evaluate(int op1, int op2){
        return op1 + op2;
    }
}


class Subtraction implements Operation {

    @ Override
    public int evaluate(int op1, int op2){
        return op2 - op1;
    }
}


class Multiplication implements Operation {

    @ Override
    public int evaluate(int op1, int op2){
        return op1 * op2;
    }
}


class Division implements Operation {

    @Override
    public int evaluate(int op1, int op2) {
        return op2 / op1;
    }
}

class NumericNode extends Node {

    String value;

    NumericNode(String value) {
        this.value = value;
    }

    @Override
    public int evaluate() {
        return Integer.parseInt(this.value);
    }
}

class OperatorNode extends Node {

    Node left;
    Node right;
    Operation operation;

    public OperatorNode(Operation operation, Node left, Node right) {
        this.operation = operation;
        this.left = left;
        this.right = right;
    }

    @Override
    public int evaluate() {
        return this.operation.evaluate(this.left.evaluate(), this.right.evaluate());
    }
}


class TreeBuilder {
    
    static final Map<String, Operation> OPERATIONS = new HashMap<String, Operation>() {
        {
            put("+", new Addition());
            put("-", new Subtraction());
            put("/", new Division());
            put("*", new Multiplication());
        }
    };

    Node buildTree(String[] postfix) {
        
        Stack<Node> stack = new Stack<Node>();
        
        for (String value : postfix) {
            if (OPERATIONS.containsKey(value)) {
                Node op1 = stack.pop();
                Node op2 = stack.pop();
                stack.add(new OperatorNode(OPERATIONS.get(value), op1, op2));
            } else {
                stack.add(new NumericNode(value));
            }
        }
        
        return stack.peek();
    }
}


/**
* Your TreeBuilder object will be instantiated and called as such:
 * TreeBuilder obj = new TreeBuilder()
 * Node expTree = obj.buildTree(postfix)
 * int ans = expTree.evaluate()
 */
public class ExpressionTreeEvaluate {

    public static void main(String[] args) {

        String[] postfix = { "3", "4", "+", "2", "*", "7", "/" };
        TreeBuilder obj = new TreeBuilder();
        Node expTree = obj.buildTree(postfix);
        int ans = expTree.evaluate();
        System.out.println(ans);
    }

}
