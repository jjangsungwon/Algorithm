#define _CRT_SECURE_NO_WARNINGS

#include<stdio.h>
#include<math.h>

//JJang Sung Won BAEKJOON_16431

int main(void)
{
	int b_x, b_y;
	int d_x, d_y;
	int j_x, j_y;
	int result1 = 0, result2 = 0;

	//input
	scanf("%d %d", &b_x, &b_y); // bessie
	scanf("%d %d", &d_x, &d_y); // daisy
	scanf("%d %d", &j_x, &j_y); // tie

	//error check
	if (b_x < 1 || b_x > 1000)
		return 0;
	if (b_y < 1 || b_y > 1000)
		return 0;
	if (d_x < 1 || d_x > 1000)
		return 0;
	if (d_y < 1 || d_y > 1000)
		return 0;
	if (j_x < 1 || j_x > 1000)
		return 0;
	if (j_y < 1 || j_y > 1000)
		return 0;

	if (abs(b_x - j_x) == abs(b_y - j_y)) //대각선으로만 가도 될 때
	{
		result1 = abs(b_y - j_y);
	}
	else if (b_x == j_x)
	{
		result1 = abs(b_y - j_y);
	}
	else if (b_y == j_y)
	{
		result1 = abs(b_x - j_x);
	}
	else if(abs(b_x - j_x) > abs(b_y - j_y))
	{
		result1 = abs(b_x - j_x);
	}
	else
	{
		result1 = abs(b_y - j_y);
	}

	result2 = abs(d_x - j_x) + abs(d_y - j_y); //dasiy 길이

	//printf("result1 = %d\nresult2 = %d\n", result1, result2);

	if (result1 == result2)
		printf("tie");
	else if (result1 > result2)
		printf("daisy");
	else
		printf("bessie");

	//system("pause");
	return 0;
}