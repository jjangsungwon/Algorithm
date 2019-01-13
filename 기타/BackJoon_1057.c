#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>    

//JJang Sung Won BaekJoon_1057

int main(void)
{
	int N, p1, p2,i,check=0;
	int count = 0;
	
	scanf("%d %d %d", &N, &p1, &p2);

	if (N > 100000 || N<1) //error check
		return 0;
	if (p1 > N || p2 > N)
		return 0;
	if (p1 < 1 || p2 < 1)
		return 0;
	if (p1 == p2)
		return 0;


	if (N % 2)
		count++;

	while (1) //경기 개수
	{
		N = N / 2;
		if (N == 0)
			break;
		count++;
	}

	if (p1 < p2) {
		for (i = 0; i <= count; i++)
		{
			check++;
			if (p1 % 2) {
				if ((p2 - p1) == 1) {
					printf("%d", check);
					return 0;
				}
			}
			if (p1 % 2)
				p1 = p1 / 2 + 1;
			else
				p1 = p1 / 2;

			if (p2 % 2)
				p2 = p2 / 2 + 1;
			else
				p2 = p2 / 2;
		}
	}
	else {
		for (i = 0; i <= count; i++)
		{
			check++;
			if (p2 % 2) {
				if ((p1 - p2) == 1) {
					printf("%d", check);
					return 0;
				}
			}
			if (p1 % 2)
				p1 = p1 / 2 + 1;
			else
				p1 = p1 / 2;

			if (p2 % 2)
				p2 = p2 / 2 + 1;
			else
				p2 = p2 / 2;
		}
	}

	printf("-1"); //하지만 이 경우는 없다.
	return 0;
}
