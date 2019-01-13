#define _CRT_SECURE_NO_WARNINGS

//JJang Sung Won BaekJoon_1015

#include<stdio.h>
#include<stdlib.h>

int main(void)
{
	int N,i,j;
	int *arr, *copy, temp=0,check=0;

	scanf("%d", &N);

	arr = (int*)malloc(sizeof(int) * N);
	copy = (int*)malloc(sizeof(int) * N);

	for (i = 0; i < N; i++)
		scanf("%d", &arr[i]);

	copy[0] = temp++;

	for (i = 1; i < N; i++)
	{
		for (j = 0; j < i; j++)
		{
			if (arr[i] > arr[j])
				continue;
		}
		if (i == j)
			copy[i] = temp++;

		
		for (j = 0; j < i; j++)
		{
			if (arr[j] < arr[i])
				continue;
			else if (arr[j] == arr[i])
			{
				
			}
			else {
				copy[j]++;
				check++;
			}
		}
		temp++;
		copy[j] = i - check;
		check = 0;
	}

	for (i = 0; i < N; i++)
		printf("%d ", copy[i]);

	return 0;
}