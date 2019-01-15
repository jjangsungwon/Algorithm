#define _CRT_SECURE_NO_WARNINGS

#include<stdio.h>

//JJang Sung Won BaekJoon_11022

int main(void)
{
	int i, N;
	int a[10000], b[10000], result[10000];
	int n1, n2;
	scanf("%d", &N);

	for (i = 0; i < N; i++)
	{
		scanf("%d %d", &n1, &n2);

		if (n1 < 0 || n2 < 0)
			return 0;
		if (n1 >= 10 || n2 >= 10)
			return 0;

		a[i] = n1;
		b[i] = n2;
		result[i] = n1 + n2;
	}

	for (i = 0; i < N; i++)
		printf("Case #%d: %d\n", i + 1, result[i]);

	return 0;
}