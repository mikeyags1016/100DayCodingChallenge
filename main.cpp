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
#include <cmath>
using namespace std;

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
                swap(&list[j], &list[j + 1]);
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

void merge(int *list, int left, int middle, int right)
{
    int i, j, k, temp[right - left + 1];
    
    //Merge the lists together into combined list
    //based off of which element is smaller
    i = left;
    j = middle + 1;
    k = 0;
    
    while (i <= middle && j <= right)
    {
        if (list[i] < list[j])
        {
            temp[k] = list[i];
            i++;
        }
        else
        {
            temp[k] = list[j];
            j++;
        }
        k++;
    }
    
    //Put remaining elements into list
    while (i <= middle)
    {
        temp[k] = list[i];
        i++;
        k++;
    }
    while (j <= right)
    {
        temp[k] = list[j];
        j++;
        k++;
    }
    
    //Assign elements of the temp into the list
    for (i = left; i <= right; i++)
    {
        list[i] = temp[i - left];
    }
}

void merge_sort(int *list, int left, int right)
{
    //While there are still elements in the list
    if (left < right)
    {
        //Find the middle and split the list in half
        int middle = (right + left) / 2;
        merge_sort(list, left, middle);
        merge_sort(list, middle + 1, right);
        merge(list, left, middle, right);
    }
}

int partition(int *list, int left, int right)
{
    //We will compare everything to this pivot
    int pivot = right;
    int i = left - 1; //Border for partition
    int j = left;
    
    //Loop through the list
    for (; j < right; j++)
    {
        //If the current element is less than the pivot,
        //move the border and swap the elements in
        //index j and i
        if (list[j] <= list[pivot])
        {
            i++;
            swap(&list[i], &list[j]);
        }
    }
    
    //Place the pivot back in the middle and return it
    swap(&list[i + 1], &list[right]);
    return i + 1;
}

void quick_sort(int *list, int left, int right)
{
    //While there is more than one element in the list
    if (left < right)
    {
        //Return the pivot after partitioning for two halves
        int p = partition(list, left, right);
        
        quick_sort(list, left, p - 1);
        quick_sort(list, p + 1, right);
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
    int arr[100000];
    int n = (sizeof(arr)/sizeof(arr[0]));
    
    for (int i = 0; i < n; i++)
    {
        arr[i] = rand() % 100 + 1;
    }
    
    time_t start = time(0);
    
    selection_sort(arr, n-1);
    
    double seconds_since_start = difftime(time(0), start);
    print(arr, n);
    
    cout << seconds_since_start << " s" << endl;
}
