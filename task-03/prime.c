#include <stdio.h>
int main(){

int i,j,n;
int c;

printf("Enter limit n \n");
scanf("%d",&n);

for(i=2;i<n;i++)
{
	c=0;
	for(j=1;j<n;j++)
	{
		if(i%j==0)
		{
			c++;
		}
	}

if(c==2)
{
	printf("%d ",i);
}
}

return 0;
}
