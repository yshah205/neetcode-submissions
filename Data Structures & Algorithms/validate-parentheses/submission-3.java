class Solution {
    public boolean isValid(String s) {
    
        Stack<Character> stack = new Stack<>();

    if (s.length() % 2 != 0) return false;
    
    for (int i = 0; i < s.length(); i++){
        
        char brac = s.charAt(i);

    if (brac == '{' || brac == '[' || brac == '(') {
        stack.push(brac);

    } else if (brac == '}' || brac == ']' || brac == ')') {
    if (stack.isEmpty()) return false;
     char top = stack.pop();

    
    if (top == '[' && brac != ']') return false;
    if (top == '{' && brac != '}') return false;
    if (top == '(' && brac != ')') return false;

    }



    }
    return stack.isEmpty();




    }
}
