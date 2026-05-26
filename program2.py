#include <iostream>
using namespace std;
void trmatr(int matr[3][3], int restr[3][3]) {
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            restr[j][i] = matr[i][j];
        }
    }
}
int main() {
    int A[3][3], B[3][3], C[3][3];
    int AB[3][3], AC[3][3], BC[3][3];
    int ABt[3][3], ACt[3][3], BCt[3][3];
    int s[3][3];
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            cin >> A[i][j];
        }
    }
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            cin >> B[i][j];
        }
    }
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            cin >> C[i][j];
        }
    }
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            AB[i][j] = A[i][j] + B[i][j];  
            AC[i][j] = A[i][j] + C[i][j];  
            BC[i][j] = B[i][j] + C[i][j];  
        }
    }
    trmatr(AB, ABt);  
    trmatr(AC, ACt);  
    trmatr(BC, BCt); 
    
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            s[i][j] = ABt[i][j] - ACt[i][j] + BCt[i][j];
        }
    }
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            cout << s[i][j] << " ";
        }
        cout << endl;
    }
}
