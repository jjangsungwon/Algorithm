#define _CRT_SECURE_NO_WARNINGS

#include<stdio.h>
/*
	baekjoon_1193
	github : JJANGSUNGWON
	
*/

int main()
{
	int X;
	int count = 1;
	int sum = 0;
	int num = 0;
	//input
	scanf("%d", &X);

	while (1)
	{
		if (X == 1)
			break;
		sum += count;
		count++;

		if (sum+count >= X)
			break;
	}
	
	num = X - sum;

	if (count % 2 == 0)
		printf("%d/%d", num, count+1-num);
	else
		printf("%d/%d", count+1-num, num);
	
	return 0;
}
