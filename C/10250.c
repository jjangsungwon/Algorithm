#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>

int main(void)
{
	int T;
	int H, W, N;
	int x, y, result;

	scanf("%d", &T);

	for (int i = 0; i < T; i++)
	{
		scanf("%d %d %d", &H, &W, &N);

		x = N / H;
		y = N % H;

		if (y == 0)
			result = (100 * H) + x;
		else
			result = (100 * y) + (x + 1);
		printf("%d\n", result);
	}
}