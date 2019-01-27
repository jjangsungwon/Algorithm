#define _CRT_SECURE_NO_WARNINGS

#include<stdio.h>
#include<time.h>
#include<stdlib.h>

//JJang Sung Won BAEKJOON_15913

int main(void)
{
	srand((unsigned)time(NULL));
	int temp;

	temp = rand() % 3;

	printf("%d", temp);

	return 0;
}
