#define _CRT_SECURE_NO_WARNINGS

#include<stdio.h>

//JJang Sung Won BaekJoon_10952

int main(void)
{
	int i=0,len=1;
	int a[10000], b[10000], result[10000];
	int n1, n2;

	while(1)
	{
		scanf("%d %d", &n1, &n2);

		if (n1 < 0 || n2 < 0)
			return 0;
		if (n1 >= 10 || n2 >= 10)
			return 0;

		if (n1 == 0 && n2 == 0)
			break;

		a[i] = n1;
		b[i] = n2;
		result[i] = n1 + n2;
		len++;
		i++;
	}

	len--;
	for (i = 0; i < len; i++)
		printf("%d\n",result[i]);

	return 0;
}