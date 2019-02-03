#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#include<string.h>

//BaekJoon_11023

int main() {
	int N;
	int sum = 0,num;
	while (scanf("%d", &num) != EOF)
	{
		sum += num;
	}

	printf("%d", sum);
	return 0;
}