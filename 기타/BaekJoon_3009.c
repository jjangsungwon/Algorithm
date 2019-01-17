#define _CRT_SECURE_NO_WARNINGS

#include<stdio.h>

//JJangSungWon BaekJoon_3009
int main(void)
{
	int x[3], y[3];
	int i;
	int x_value[1001] = { 0, }, y_value[1001] = { 0, };
	int result_x, result_y;

	for (i = 0; i < 3; i++)	
		scanf("%d %d", &x[i], &y[i]);
	
	for (i = 0; i < 3; i++)
	{
		x_value[x[i]]++;
		y_value[y[i]]++;
	}

	for (i = 1; i <= 1000; i++)
	{
		if (x_value[i] == 1)
			result_x = i;

		if (y_value[i] == 1)
			result_y = i;
	}

	printf("%d %d", result_x, result_y);
	//system("pause");
	return 0;
}