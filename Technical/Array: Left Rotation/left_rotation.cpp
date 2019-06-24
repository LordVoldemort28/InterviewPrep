#include <iostream>
#include <vector>
#include <stdio.h>
#include <fstream>

using namespace std;

// Complete the rotLeft function below.
vector<int> rotLeft(vector<int> a, int d) {

    int i;
    for(i=0; i<d; i++){
        
        //Push back first element in the back of vector
        a.push_back(a[0]);
        //Erase first element from vector
        a.erase (a.begin(),a.begin()+1);     
     }
    
    return a;
}

int main()
{
    vector<int> a;
    int j;
    for(j=1; j<6; j++){
        a.push_back(j);
    }
    int d = 4;

    vector<int> b = rotLeft(a, d);
    
    int i;
    for(i=0; i<b.size(); i++)
    {
        cout << b[i] << endl;
    }
}