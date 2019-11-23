#define _CRT_SECURE_NO_WARNINGS

#include<stdio.h>
/*
	baekjoon_10870
	github : JJANGSUNGWON
	
*/

int fibo(int n)
{
	if (n == 0)
		return 0;
	else if (n == 1)
		return 1;
	else
		return fibo(n - 1) + fibo(n - 2);
}

int main()
{
	int n;
	int value;

	scanf("%d", &n);
	value = fibo(n);

	printf("%d", value);
	return 0;
}
