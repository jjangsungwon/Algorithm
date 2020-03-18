#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>

int main(void)
{
	int N, M;
	int cnt = 0;

	//input
	scanf("%d %d", &N, &M);

	//error check
	if (N < 1 || N>300 || M < 1 || M>300)
		return;

	cnt = N * M - 1;

	printf("%d", cnt);
	return 0;
}