#include <iostream>
#include <stack>
#include <cctype>
using namespace std;

// Function to determine precedence of operators
int precedence(char op) {
    if (op == '+' || op == '-') return 1;
    if (op == '*' || op == '/') return 2;
    return 0;
}

// Function to convert infix to postfix
string infixToPostfix(string infix) {
    stack<char> st;
    string postfix = "";
    
    for (char ch : infix) {
        if (isalnum(ch)) {
            postfix += ch; // If operand, add to postfix string
        } 
        else if (ch == '(') {
            st.push(ch); // Push '(' onto stack
        } 
        else if (ch == ')') {
            // Pop and add to postfix until '(' is encountered
            while (!st.empty() && st.top() != '(') {
                postfix += st.top();
                st.pop();
            }
            st.pop(); // Remove '('
        } 
        else { // Operator
            while (!st.empty() && precedence(st.top()) >= precedence(ch)) {
                postfix += st.top();
                st.pop();
            }
            st.push(ch);
        }
    }

    // Pop remaining operators in stack
    while (!st.empty()) {
        postfix += st.top();
        st.pop();
    }

    return postfix;
}

// Function to evaluate postfix expression
int evaluatePostfix(string postfix) {
    stack<int> st;

    for (char ch : postfix) {
        if (isdigit(ch)) {
            st.push(ch - '0'); // Convert char to integer and push
        } else {
            int val2 = st.top(); st.pop();
            int val1 = st.top(); st.pop();

            switch (ch) {
                case '+': st.push(val1 + val2); break;
                case '-': st.push(val1 - val2); break;
                case '*': st.push(val1 * val2); break;
                case '/': st.push(val1 / val2); break;
            }
        }
    }

    return st.top(); // Final result
}

int main() {
    string infix, postfix;
    cout << "Enter infix expression: ";
    cin >> infix;

    // Convert to postfix
    postfix = infixToPostfix(infix);
    cout << "Postfix Expression: " << postfix << endl;

    // Evaluate postfix
    int result = evaluatePostfix(postfix);
    cout << "Evaluation Result: " << result << endl;

    return 0;
}
