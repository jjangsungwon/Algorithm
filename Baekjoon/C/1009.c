#define _CRT_SECURE_NO_WARNINGS

#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<memory.h>

//BaekJoon JJang Sung Won 1009
int	cal(int n1, int n2);

int main(int argc, int *argv[])
{
	int *a, *b;
	int T,i,result;

	scanf("%d", &T);


	a = (int*)malloc(sizeof(int) * T);
	b = (int*)malloc(sizeof(int) * T);

	memset(a, 0, T);
	memset(b, 0, T);

	for (i = 0; i < T; i++) {
		scanf("%d %d", &a[i], &b[i]);
		if (a[i] < 1 || a[i]>99)
			return;
		if (b[i] < 1 || b[i] >= 1000000)
			return;

	}
	
	for (i = 0; i < T; i++) {
		a[i] = a[i] % 10;
		result = cal(a[i], b[i]);
		if (result == 0)
			result = 10;
		printf("%d\n", result);
	}

	system("pause");
	return 0;
}

int	cal(int n1, int n2)
{
	/* 오류나는 부분이 있는 것 같다.
	int i;
	int temp = n1;
	if (temp % 10 == 1 || temp % 10 == 5 || temp % 10 == 6)//끝 자리 반복
		return temp % 10;
	else if (temp % 10 == 2 || temp % 10 == 3 || temp % 10 == 7 || temp % 10 == 8)//5번 순환
	{
		
		if (n2 % 5 == 0) {
			if (n2 % 4 == 0)
				n2 = n2 / 5;
		}
		else {
			if (n2 < 5) {
			}
			else {
				n2 = n2 % 5 + 1;
			}
		}
		for (i = 1; i < n2; i++) {
			n1 *= temp;
			n1 %= 10; //어짜피 끝자리만 필요하기 때문에
		}
		return n1 % 10;
	}
	else//2번 순환
	{
		if (n2 % 2) // 홀수
			return (n1 % 10);
		else
			return ((n1 * n1) % 10);
	}
	*/
	int temp = n1; //위 함수는 오류가 나서 어쩔수없이 길지만 확실하게 다시 코드 구성.
	if (temp % 10 == 1)
	{
		return 1;
	}
	else if (temp % 10 == 0)
		return 10;

	else if (temp % 10 == 2)
	{
		if (n2 == 0)
			return 1;
		else {
			switch (n2 % 4) {
			case 1:
				return 2;
			case 2:
				return 4;
			case 3:
				return 8;
			case 0:
				return 6;
			}
		}

	}
	else if (temp % 10 == 3)
	{
		if (n2 == 0)
			return 1;
		else {
			switch (n2 % 4) {
			case 1:
				return 3;
			case 2:
				return 9;
			case 3:
				return 7;
			case 0:
				return 1;
			}
		}
	}
	else if (temp % 10 == 5)
	{
		if (n2 == 0)
			return 1;
		else
			return 5;
	}
	else if (temp % 10 == 6)
	{
		if (n2 == 0)
			return 1;
		else
			return 6;
	}
	else if (temp % 10 == 7)
	{
		if (n2 == 0)
			return 1;
		else {
			switch (n2 % 4) {
			case 1:
				return 7;
			case 2:
				return 9;
			case 3:
				return 3;
			case 0:
				return 1;
			}
		}
	}
	else if (temp % 10 == 8)
	{
		if (n2 == 0)
			return 1;
		else {
			switch (n2 % 4) {
			case 1:
				return 8;
			case 2:
				return 4;
			case 3:
				return 2;
			case 0:
				return 6;
			}
		}
	}
	else//2번 순환
	{
		if (n2 == 0)
			return 1;

		if (n2 % 2) // 홀수
			return (n1 % 10);
		else
			return ((n1 * n1) % 10);
	}
}