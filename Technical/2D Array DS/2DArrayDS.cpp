#include <iostream>
#include <vector>
#include <stdio.h>
#include <fstream>

using namespace std;

// Complete the hourglassSum function below.
int hourglassSum(vector<vector<int> > arr) {
    int i,j;
    int hourglass = 0;
    int maxSum = -9999;
    for(i=0; i<4; i++){
        for(j=0; j<4; j++){
           hourglass = arr[i][j] + arr[i][j+1] + arr[i][j+2]
                                 + arr[i+1][j+1] + 
                       arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2];
            if( hourglass > maxSum ) { maxSum = hourglass; }
        }
    }
    return maxSum;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));
    
    vector<vector<int> > arr(6);
    for (int i = 0; i < 6; i++) {
        arr[i].resize(6);

        for (int j = 0; j < 6; j++) {
            cin >> arr[i][j];
        }

        cin.ignore(numeric_limits<streamsize>::max(), '\n');
    }

    int result = hourglassSum(arr);

    fout << result << "\n";

    fout.close();

    return 0;
}