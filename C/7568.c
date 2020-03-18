#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
/*
	baekjoon_7568
	github : JJANGSUNGWON
	단순하게 모든 경로를 돌아보면 된다.
*/

int main(void)
{
	int N;
	int i, j;
	int height[300], weight[300];
	int result[100] = { 0, };
	int count = 0;

	//input
	scanf("%d", &N);

	for (i = 1; i <= N; i++)
		scanf("%d %d", &height[i], &weight[i]);

	for (i = 1; i <= N; i++)
	{
		for (j = 1; j <= N; j++)
		{
			if ((height[i] < height[j]) & (weight[i] < weight[j]))
				count++;
		}
		result[i] = count + 1;
		count = 0;
	}

	for (i = 1; i <= N; i++) 
			printf("%d ", result[i]);
	
	return 0;
}