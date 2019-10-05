#define _CRT_SECURE_NO_WARNINGS

//BaekJoon_2783
#include<stdio.h>

int main(void)
{
	double X, Y;
	double average[100];
	double min = 9999;
	int flag = 0;
	int i,N;
	double result = 0;

	scanf("%lf %lf", &X, &Y);
	
	scanf("%d", &N);

	average[0] = X / Y;
	min = X / Y;

	for (i = 1; i <= N; i++)
	{
		scanf("%lf %lf", &X,&Y);
		average[i] = X / Y;

		if (min > average[i])
			min = average[i];
	}
	
	result = min * 1000;

	printf("%.2lf", result);

	return 0;
}