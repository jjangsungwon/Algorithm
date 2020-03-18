#define _CRT_SECURE_NO_WARNINGS

//BaekJoon_9316
#include<stdio.h>

int main(void)
{
	int n;

	//input
	scanf("%d", &n);

	for (int i = 0; i < n; i++)
	{
		printf("Hello World, Judge %d!", i + 1);

		if (i + 1 != n)
			puts("");
	}

	return 0;
}