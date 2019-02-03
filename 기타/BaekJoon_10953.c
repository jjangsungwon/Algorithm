#define _CRT_SECURE_NO_WARNINGS

#include<stdio.h>

//BaekJoon_10953
int main(void)
{
	int A[10000], B[10000];
	int N,i;

	scanf("%d", &N);

	for (i = 0; i < N; i++)
		scanf("%d,%d", &A[i], &B[i]);

	for (i = 0; i < N; i++)
		printf("%d\n", A[i] + B[i]);

	return 0;
}