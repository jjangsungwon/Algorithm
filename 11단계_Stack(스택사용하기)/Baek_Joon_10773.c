#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h> 

int* arr;

int top = -1;
int bottom = 0;

//Baek_Joon_10773
int main(void)
{
	int N;
	int i, j;
	int num;
	int sum = 0;

	//input
	scanf("%d", &N);
	arr = (int*)malloc(sizeof(int) * N);

	for (i = 0; i < N; i++)
	{
		scanf("%d", &num);

		if (num == 0)
			top--;
		else
			arr[++top] = num;
	
	}

	//sum
	for (i = 0; i <= top; i++)
		sum += arr[i];

	printf("%d", sum);

	free(arr);
	return 0;
}