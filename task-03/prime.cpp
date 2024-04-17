#include<iostream>
using namespace std;

int main()
{
	int i,j,n;
	int c;

	cout<<"Enter the limit n"<<endl; 
	cin>>n;

	for(i=2;i<n;i++)
	{
		c=0;
		for(j=1;j<=i;j++)
		{
			if(i%j==0)
			c++;
		}
		if(c==2)
		cout<<i<<" ";
	}

	return 0;
}
