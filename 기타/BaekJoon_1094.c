#define _CRT_SECURE_NO_WARNINGS

//BAEKJOON_1094
#include<stdio.h>

int stick[100] = { 64, };

int total()
{
	int i = 0, sum = 0;

	while (stick[i] != 0)
		sum += stick[i++];
	return sum;
}

int main(void)
{
	int X;
	int check = 0;
	int num,i=0;

	//input
	scanf("%d", &X);

	while (total() > X)
	{
		num = stick[check] / 2;
		stick[check++] = num;
		stick[check] = num;

		//하나를 버린다.
		if (total() - stick[check] >= X) {
			stick[check] = 0;
			check--;
		}
	}

	check = 0;
	while (stick[i] != 0)
	{
		check++;
		i++;
	}

	printf("%d", check);
	
	return 0;
}
