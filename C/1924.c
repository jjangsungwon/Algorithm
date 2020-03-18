#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>

//BaekJoon_1924
int main(void)
{
	int x, y;
	int result = 0;
	int i, j;

	scanf("%d %d", &x, &y);

	//x error check
	if (x < 1 || x >12)
		return 0;

	//y error check
	if (y < 1 || y>31)
		return 0;

	//1,3,5,7,8,10,12 = 31일까지
	//4,6,9,11 = 30일까지
	//2 = 28일까지

	//요일 구하기..

	for (i = 1; i < x; i++) {
		if (i % 9 == 0)
			result += 30;
		else if (i % 12 == 0)
			result += 31;
		else if (i % 6 == 0)
			result += 30;
		else if (i % 8 == 0)
			result += 31;
		else if (i % 4 == 0)
			result += 30;
		else if (i % 10 == 0)
			result += 31;
		else if ((i % 3 == 0) || (i % 5 == 0) || (i % 7 == 0))
			result += 31;
		else if ((i % 11 == 0))
			result += 30;
		else if (i % 2 == 0)
			result += 28;
		else if (i % 1 == 0)
			result += 31;

		//printf("result = %d\n", result);
	}
	for (i = 1; i <= y; i++)
		result += 1;

	result = result - 1;
	//printf("result = %d\n", result);

	if (result % 7 == 0)
		printf("MON");
	else if (result % 7 == 1)
		printf("TUE");
	else if (result % 7 == 2)
		printf("WED");
	else if (result % 7 == 3)
		printf("THU");
	else if (result % 7 == 4)
		printf("FRI");
	else if (result % 7 == 5)
		printf("SAT");
	else if (result % 7 == 6)
		printf("SUN");

	return 0;
}