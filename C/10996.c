#define _CRT_SECURE_NO_WARNINGS

#include<stdio.h>

int main(void)
{
	int n;

	//input
	scanf("%d", &n);

	if (n == 1) 
		printf("*");
	else {
		for (int i = 0; i < 2 * n; i++)
		{
			for (int j = 0; j < n; j++)
			{
				if (i % 2 == 0)
				{
					if (j % 2 == 0)
						printf("*");
					else
						printf(" ");
				}
				else
				{
					if (j % 2 == 0)
						printf(" ");
					else
						printf("*");
				}
			}
			printf("\n");
		}
	}
	return 0;
}