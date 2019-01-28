#define _CRT_SECURE_NO_WARNINGS

#include<stdio.h>
#include<string.h>
#include<stdlib.h>

//JJangSungWon_2775
int main(void)
{
	int T;

	int k, n;
	int temp[100][100] = { 0, };
	int i, j;
	int total[10000] = { 0, };

	scanf("%d", &T);

	for (i = 0; i <=14; i++)
	{
		for (j = 1; j <= 14; j++)
		{
			if(i==0)
				temp[i][j] = j;

			if (j == 1)
				temp[i][j] = 1;
		}
	}

	for (i = 1; i <= 14; i++)
	{
		for (j = 2; j <= 14; j++)
		{
			temp[i][j] = temp[i][j - 1] + temp[i - 1][j];
		}
	}

	for (i = 0; i < T; i++)
	{
		scanf("%d", &k);
		scanf("%d", &n);

		total[i] = temp[k][n];
	}

	for (i = 0; i < T; i++)
		printf("%d\n", total[i]);

	return 0;
}