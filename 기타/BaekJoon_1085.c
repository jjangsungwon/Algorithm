#define _CRT_SECURE_NO_WARNINGS

#include<stdio.h>

//JJangSungWon BaekJoon_1085

int main(void)
{
	int x, y, w, h;
	int min;

	scanf("%d %d %d %d", &x, &y, &w, &h);
	
	min = w - x;

	if (min > x)
		min = x;

	if (min > h - y)
		min = h - y;

	if (min > y)
		min = y;

	printf("%d", min);

	system("pause");
	return 0;
}