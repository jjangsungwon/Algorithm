#define _CRT_SECURE_NO_WARNINGS

#include<stdio.h>
//BaekJoon JJang Sung Won 1008

int main(int argc, int *argv[])
{
	int A, B;
	double div_result;

	scanf("%d %d", &A, &B); //input

	if (A < 0 || B < 0)
		return 0;
	if (A > 9 || B > 9)
		return 0;

	div_result = (double)A / B;
	
	printf("%.10lf", div_result);

	return 0;
}