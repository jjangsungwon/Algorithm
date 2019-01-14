#define _CRT_SECURE_NO_WARNINGS

#include<stdio.h>

//JJang Sung Won BaekJoon_10872
int factorial(int n);
int main(int argc, char *argv[])
{
	int N;

	scanf("%d", &N);

	if (N < 0 || N>12)
		return 0;

	printf("%d", factorial(N));

	return 0;
}

int factorial(int n)
{
	if (n <= 1)
		return 1;
	else
		return n * factorial(n - 1);
}