#define _CRT_SECURE_NO_WARNINGS

//BaekJoon_2442
#include<stdio.h>

void star(int n)
{
	//n번째자리에 center
	int center = n;
	int check = 1;
	for (int i = 0; i < n; i++)
	{
		for (int j = i + 1; j < n; j++)
		{
			printf(" ");
		}

		for (int k = 1; k <= check; k++)
			printf("*");

		if(i+1 != n)
			puts("");

		check += 2;
	}
}

int main(void)
{
	int n;

	scanf("%d", &n);

	star(n);

	return 0;
}