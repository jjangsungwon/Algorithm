#define _CRT_SECURE_NO_WARNINGS

#include<stdio.h>
//BaekJoon JJang Sung Won 2748

long long int fibo(int count);
int main(void)
{
	long long int result;
	int n;
	
	scanf("%d", &n);//input

	if (n == 0) {
		printf("%d", 0);
		return 0;
	}
	if (n < 1 || n>90)//error check
		return 0;

	result = fibo(n);
	printf("%lld", result);

	return 0;
}

long long int fibo(int count)
{
	int temp = 2;
	long long int n0 = 0, n1 = 1,result;

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