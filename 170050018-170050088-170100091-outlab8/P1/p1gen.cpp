#include<iostream>
#include<random>
#include<cmath>
using namespace std;

int main(){
	int n,p;
	cin>>n>>p;

	cout<<n<<" "<<p<<endl;
	int np = pow(p,n);
	for(int i=0; i<np; i++)
		cout<<i+1<<" ";

	return 0;
}
