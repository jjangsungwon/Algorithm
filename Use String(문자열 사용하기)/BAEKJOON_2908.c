#include<stdio.h>
#include<stdlib.h>
#include<string.h>

//Jang Sung Won

int main(void)
{
	int num1, num2;		// original num
	int c_num1=0, c_num2=0; // change num

	scanf("%d %d", &num1, &num2);

	//error check
	if (num1 < 100 || num2 < 100)
		return 0;
	if (num1 > 1000 || num2 > 1000)
		return 0;

	c_num1 += num1 / 100; //100의 자리 더하기
	c_num2 += num2 / 100;

	num1 = num1 % 100; //100의 자리 없애기
	num2 = num2 % 100;

	c_num1 = c_num1 + (10 * (num1 / 10)); // 10의 자리 더하기
	c_num2 = c_num2 + (10 * (num2 / 10));

	num1 = num1 % 10; //10의 자리 없애기
	num2 = num2 % 10; 

	c_num1 = c_num1 + (100 * (num1 / 1));
	c_num2 = c_num2 + (100 * (num2 / 1));

	if (c_num1 > c_num2)
		printf("%d", c_num1);
	else
		printf("%d", c_num2);

	return 0;
}