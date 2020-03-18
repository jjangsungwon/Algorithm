#define _CRT_SECURE_NO_WARNINGS

#include<stdio.h>

int main(void)
{
	int N, K;
	int arr[100];
	int total = 0;
	int count = 0;

	scanf("%d %d", &N, &K);

	for (int i = 0; i < N; i++)
		scanf("%d", &arr[i]);


	for (int i = N - 1; i >= 0; i--)
	{
		if (total + arr[i] <= K)
			while (1)
			{
				total += arr[i];
				count++;

				if (total + arr[i] > K)
					break;
			}

		if (total == K)
		{
			printf("%d", count);
			break;
		}
	}
}