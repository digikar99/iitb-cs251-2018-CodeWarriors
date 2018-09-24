#include<iostream>
#include<cmath>

using namespace std;
int main(){
	int n, p;
	cin>>n>>p;
		
	int pn = pow(p,n);
	cout<<n<<" "<<p<<endl;
	for(int i=0; i<pn; i++){
		cout<<rand()<<" ";
	}
	cout<<endl;
	return 0;
}

	
