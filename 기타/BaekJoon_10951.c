#define _CRT_SECURE_NO_WARNINGS

#include<stdio.h>

//BaekJoon_10951
int main(void)
{
	int A[100], B[100], result[100];
	int i=0,j;

	while (scanf("%d %d", &A[i], &B[i]) != EOF)
		i++;
		

	for (j = 0; j < i; j++)
		printf("%d\n", A[j] + B[j]);

	return 0;
}