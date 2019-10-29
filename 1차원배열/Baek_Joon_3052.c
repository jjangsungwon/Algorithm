#define _CRT_SECURE_NO_WARNINGS

//Baek_Joon_3052
#include<stdio.h>

int main(void)
{
	int i, j;
	int arr[11];
	int divison[11];
	int count = 0;

	for (i = 1; i <= 10; i++)
		scanf("%d", &arr[i]);

	for (i = 1; i <= 10; i++)
		divison[i] = arr[i] % 42;

	for (i = 1; i < 10; i++) {
		for (j = i + 1; j <= 10; j++) {
			if (divison[i] == divison[j])
				divison[i] = -1;
		}
	}

	for (i = 1; i <= 10; i++) {
		if (divison[i] != -1)
			count++;
	}

	printf("%d", count);
	return 0;
}