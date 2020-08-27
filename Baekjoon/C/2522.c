#define _CRT_SECURE_NO_WARNINGS

#include<stdio.h>

//JJang Sung Won BaekJoon_1066
int main(int argc, char *argv[])
{
	int N;
	int i, j;
	int check = 1, temp = 1;
	scanf("%d", &N);

	if (N > 100 || N < 1) //error check
		return 0;

	for (i = 0; i < 2 * N - 1; i++) //전체 줄 수 
	{
		for (j = N; j > 0; j--)
		{
			if (j <= check)
				printf("*");
			else
				printf(" ");
		}
		if (check == N)
			temp = -1;

		check = check + temp;

		puts("");
	}
	return 0;
}