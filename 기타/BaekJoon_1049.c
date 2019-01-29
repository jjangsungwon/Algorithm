#define _CRT_SECURE_NO_WARNINGS

#include<stdio.h>

//JJangSungWon BaekJoon_1049
int main(void)
{
	int N, M,i;
	int set[100];
	int one[100];
	int one_min;
	int set_min;
	int num,result;

	scanf("%d %d", &N, &M);

	if (N < 1 || N>100)
		return 0;
	if (M < 1 || M>50)
		return 0;

	for (i = 0; i < M; i++)
	{
		scanf("%d %d", &set[i], &one[i]);
	}

	//가정
	set_min = set[0];
	one_min = one[0];

	//세트값, 1개 값이 제일 싼 거 확인
	for (i = 0; i < M; i++)
	{
		if (set_min > set[i])
			set_min = set[i];
		if (one_min > one[i])
			one_min = one[i];
	}

	if (N < 6)
	{
		if (set_min >= (one_min * 6))
			result = one_min * 6;
		else
			result = set_min;
	}
	else
	{
		if (set_min < one_min * 7)
		{
			num = N / 6;
			result = num * set_min;
			N = N - 6*num;

			if (set_min >= (one_min * N))
			{
				num = N % 6;
				result += num * one_min;
			}
			else
			{
				result += set_min;
			}
		}
		else
		{
			result = N * one_min;
		}
	}

	printf("%d", result);

	return 0;
}