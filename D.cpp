#include<iostream>
using namespace std;
int main(){
    float x,y,R; 
    int cnt=0;
    cin >> x >> y >>R;

    int A_min,A_max, B_min,B_max;
    float right;
    float left;
    float Nx, My;
    left = R*R;

    A_max = int(x)+R+1;
    A_min = int(x)-R;
    B_min = int(y)-R;
    B_max = int(y)+R+1;

    for (int n=A_min; n<A_max; n++){
        for (int m=B_min; m<B_max; m++){
            Nx = n-x;
            My = m-y;
            right = Nx*Nx+My*My;
            if (right<=left){
                cnt +=1;
            };
        };
    };
    cout << cnt << endl;
    return 0;
}