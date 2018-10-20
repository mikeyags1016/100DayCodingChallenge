#include <time.h>
#include <iostream>
#include <map>
#include <unistd.h>
#include <cmath>
using namespace std;

string stage(int section)
{
    map<int, string> stages;
    
    stages[1] = "Seed";
    stages[2] = "Sapling";
    stages[3] = "Child";
    stages[4] = "Young Adult";
    stages[5] = "Grown Evergreen";
    stages[6] = "Grandfather tree";
    
    if (section > 6)
        return "Invalid Input";
    return stages[section];
}

void timer(int max_time, int sections)
{
    clock_t start = time(0);
    double seconds = 0;
    int section_number = 0;
    
    while (seconds < max_time)
    {
        seconds = difftime(time(0), start);
        section_number++;
        
        cout << "Stage of tree: " << stage(section_number) << ", seconds: " << seconds << endl;
        sleep(sections);
    }
}

void tree_counter(int max_time)
{
    int section_times = round(max_time / 5);
    timer(max_time, section_times);
    cout << "Congratulations, you have completed your time!" << endl;
}

int main()
{
    tree_counter(60);
    return 0;
}
