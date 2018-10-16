//
//  main.cpp
//  list sorter
//
//  Created by Michael A on 10/16/18.
//  Copyright © 2018 Michael A. All rights reserved.
//

#include <iostream>
#include <random>
#include <time.h>
using namespace std;

int arr[20000];

void swap(int *i, int *j)
{
    int temp = *i;
    *i = *j;
    *j = temp;
}

void bubble_sort(int *list, int size)
{
    //Loop through entire list
    for (int i = 0; i < size - 1; i++)
    {
        //For each element, loop through the rest of the elements
        for (int j = 0; j < size - i - 1; j++)
        {
            //If j is bigger than the next element, swap
            if (list[j] > list[j + 1])
            {
                swap(&arr[j], &arr[j + 1]);
            }
        }
    }
}

void selection_sort(int *list, int size)
{
    //Loop through entire list
    for (int i = 0; i < size - 1; i++)
    {
        //Set current element to i
        int smallest = i;
        
        //Loop through rest of list
        for (int j = i + 1; j < size; j++)
        {
            //If current element is smaller than the current smallest,
            //set current to smallest
            if (list[j] < list[smallest])
            {
                smallest = j;
            }
            //When you have gone through the entire list,
            //swap the old smallest (i) with the current smallest
            //if they aren't equal
            if (smallest != i)
            {
                swap(&list[smallest], &list[i]);
            }
        }
    }
}

void print(int *arr, int size)
{
    for (int i = 0; i < size; i++)
    {
        cout << arr[i] << ", ";
    }
    cout << endl;
}

int main(int argc, const char * argv[]) {
    int n = (sizeof(arr)/sizeof(*arr));
    
    for (int i = 0; i < 20000; i++)
    {
        arr[i] = rand() % 100 + 1;
    }
    
    time_t start = time(0);
    
    selection_sort(arr, n);
    print(arr, n);
    
    double seconds_since_start = difftime( time(0), start);
    cout << seconds_since_start << " s" << endl;
}
