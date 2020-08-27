#define _CRT_SECURE_NO_WARNINGS

#include<stdio.h>
#include<stdlib.h>
#include<memory.h>

//JJangSungWon BaekJoon_9085
int main(void)
{
	int n,n1; // 테스트 개수
	int i, j;
	int *sum;
	int v;

	scanf("%d", &n);

	sum = (int*)malloc(sizeof(int) * n);
	memset(sum, 0, sizeof(int) * n); //합 저장

	for (i = 0; i < n; i++)
	{
		scanf("%d", &n1);

		for (j = 0; j < n1; j++)
		{
			scanf("%d",&v);
			sum[i] += v;
		}
	}

	for (i = 0; i < n; i++)
		printf("%d\n", sum[i]);

	free(sum);
	//system("pause");
	return 0;
}