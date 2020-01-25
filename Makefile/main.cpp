#include <iostream>
#include <fstream>
using namespace std;

int main () {
    const char* DATA = "X=1,2,3,4 Y=0,3,4,6";

    ofstream dataFile;
    dataFile.open("Data.txt");
    dataFile << DATA;
    dataFile.close();
    return 0;
}