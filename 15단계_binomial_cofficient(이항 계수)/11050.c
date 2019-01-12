#define _CRT_SECURE_NO_WARNINGS

#include<stdio.h>
//BaekJoon JJang Sung Won 11050

int bionomial_coefficient(int N, int K);
int factorial(int n);

int main(int argc, int *argv[])
{
	int N, K;
	int result;

	scanf("%d %d", &N, &K); //input

	//error check
	if (N < 1 || N>10)
		return 0;
	if (K < 0 || K>N)
		return 0;

	result = bionomial_coefficient(N, K);
	printf("%d", result);

	return 0;
}

int bionomial_coefficient(int N, int K)
{
	return factorial(N) / (factorial(K) * factorial(N - K));
}

int factorial(int n)
{
	int i,result= 1;

	for (i = 1; i <= n; i++)
		result *= i;

	return result;
}