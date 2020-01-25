#include <iostream>

using namespace std;

string algo(long int p){
    int d = 1; 
    while (d > 0) {
        if (p > 0) {
            if (d % 2 != 0) {
                p = p - (d + 1);
            } else {
                p = p - d;
            }
        } else { break; }
		
		d++;
	}
	
	d--;

    if (d % 2 == 0) {
        return "CAPTAIN AMERICA";
    } else {
        return "IRON MAN";
    }
}

int main(){
    long int p;
    std::cin >> p;
	
	if (p > 0){
		string res = algo(p);
	    cout << res << endl;	
	} else { 
		cout << "Enter value greater than 0" << endl;
	}

    return 0;
}
