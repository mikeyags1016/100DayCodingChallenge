//
//  main.cpp
//  temperature converter
//
//  Created by Michael A on 10/16/18.
//  Copyright © 2018 Michael A. All rights reserved.
//

#include <iostream>
using namespace std;

float convert_to_celcius(float value, char units)
{
    //Other units to celcius
    if (units == 'f')
    {
        return (value - 32) * 5/9;
    }
    else if (units == 'k')
    {
        return value - 273.15;
    }
    else
    {
        throw "Invalid unit";
    }
}

float convert_to_fahrenheit(float value, char units)
{
    //Other units to fahrenheit
    if (units == 'c')
    {
        return (value * 9/5) + 32;
    }
    else if (units == 'k')
    {
        return (value - 273.15) * (9/5) + 32;
    }
    else
    {
        throw "Invalid unit";
    }
}

float convert_to_kelvin(float value, char units)
{
    //Other units to kelvin
    if (units == 'c')
    {
        return value + 273.15;
    }
    else if (units == 'f')
    {
        return (value - 32) * (5/9) + 273.15;
    }
    else
    {
        throw "Invalid unit";
    }
}

int main(int argc, const char * argv[]) {
    try
    {
        cout << convert_to_celcius(32, 'f') << " celcius" << endl;
        cout << convert_to_fahrenheit(100, 'c') << " fahrenheit" <<endl;
        cout << convert_to_kelvin(1000, 'f') << " kelvin" << endl;
        cout << convert_to_celcius(100, 'c') << endl;
    }
    catch (const char* msg)
    {
        cerr << msg << endl;
    }
    
    return 0;
}
