#define _CRT_SECURE_NO_WARNINGS

//Baek_Joon_2562
#include<stdio.h>

int main(void)
{
	int arr[9];
	int i, j;
	int error_check;
	int max;
	int temp;

	//input
	for (i = 0; i < 9; i++)
		scanf("%d", &arr[i]);

	// Suppose first index is max
	max = arr[0];
	temp = 1;

	for (i = 1; i < 9; i++) {
		if (max < arr[i]) {
			max = arr[i];
			temp = i+1;
		}
	}

	printf("%d\n", max);
	printf("%d\n", temp);

	return 0;
}