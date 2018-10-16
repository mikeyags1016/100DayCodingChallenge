#include <iostream>
using namespace std;

float addition(float x, float y)
{
    return x + y;
}

float subtraction(float x, float y)
{
    return x - y;
}

float multiplication(float x, float y)
{
    return x * y;
}

float division(float x, float y)
{
    if (y == 0)
    {
        throw "0 Division";
    }
    return x / y;
}

float exponent(float x, float y)
{
    float sum = 1;
    for (int i = 0; i < y; i++)
    {
        sum *= x;
    }
    return sum;
}

void equation_definer(char operators, float x, float y)
{
    switch (operators)
    {
        case '+':
            cout << addition(x, y) << endl;
            break;
        case '-':
            cout << subtraction(x, y) << endl;;
            break;
        case '*':
            cout << multiplication(x, y) << endl;;
            break;
        case '/':
            try
        {
            cout << division(x, y) << endl;
        }
            catch (const char* message)
        {
            cerr << message << endl;
        }
            break;
        case '^':
            cout << exponent(x, y) << endl;
            break;
        default:
            throw string("Invalid Input");
            break;
    }
}

int main(int argc, const char * argv[])
{
    float x = 0, y = 0;
    char operator_sign;
    
    cout << "Enter a number: ";
    cin >> x;
    cout << endl << "Enter another number: ";
    cin >> y;
    cout << endl << "Enter your operator: ";
    cin >> operator_sign;
    
    equation_definer(operator_sign, x, y);
}
