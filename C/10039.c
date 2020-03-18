#include<stdio.h>
#include<string.h>
#include<stdlib.h>
//Jang Sung Won

#define MIN 40

int main(void)
{
	int n1, n2, n3, n4, n5;
	int mean;

	//input
	scanf("%d", &n1);
	scanf("%d", &n2);
	scanf("%d", &n3);
	scanf("%d", &n4);
	scanf("%d", &n5);

	//error check
	if ((n1 < 0) || (n2 < 0) || (n3 < 0) || (n4 < 0) || (n5 < 0))
		return 0;
	if ((n1 > 100) || (n2 > 100) || (n3 > 100) || (n4 > 100) || (n5 > 100))
		return 0;

	//40점이하는 40점으로 취급
	if (n1 <= MIN)
		n1 = MIN;

	if (n2 <= MIN)
		n2 = MIN;

	if (n3 <= MIN)
		n3 = MIN;

	if (n4 <= MIN)
		n4 = MIN;

	if (n5 <= MIN)
		n5 = MIN;

	mean = (n1 + n2 + n3 + n4 + n5) / 5;

	printf("%d", mean);

	return 0;
}
