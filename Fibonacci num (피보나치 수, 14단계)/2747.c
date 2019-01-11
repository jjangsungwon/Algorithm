#define _CRT_SECURE_NO_WARNINGS

#include<stdio.h>
//BaekJoon JJang Sung Won 2747

int fibo(int count);
int main(void)
{
	int n,result;
	
	scanf("%d", &n);//input

	if (n < 1 || n>45)//error check
		return 0;

	result = fibo(n);
	printf("%d", result);

	return 0;
}

int fibo(int count)
{
	int temp = 2;
	int n0 = 0, n1 = 1,result;
	if (count == 0)
		return n0;
	else if (count == 1)
		return n1;

	while (1)
	{
		result = n0 + n1;
		if (temp == count)
			return result;

		n0 = n1;
		n1 = result;
		temp++;
	}
}