#include<stdio.h>

int count = 0;
void o_num(int n);
int main(void)
{
	int n;
	int i;
	scanf("%d", &n);

	//error check
	if (n < 1 || n>1000)
		return 0;

	for (i = 1; i <= n; i++)
			o_num(i);

	printf("%d", count);

	return 0;
}

void o_num(int n)
{
	int div = 100;
	int num1, num2, num3;
	if (n < 100)
		count++;
	else if(n<1000){
		num1 = n / 100;
		n = n % 100;
		
		num2 = n / 10;
		n = n % 10;

		num3 = n / 1;

		if ((num1 - num2) == (num2 - num3))
			count++;
	}
}