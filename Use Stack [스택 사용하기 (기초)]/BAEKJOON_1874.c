#define _CRT_SECURE_NO_WARNINGS

#include<stdio.h>
#include<stdlib.h>
//Jang Sung Won
void push(int n);
int pop();

int *arr;
int top = 0;

int main(void)
{
	int n, i,j;
	int *input, *copy;
	int count = 0, check, max = 0, flag = 1, check1, flag2;
	int t = 0,m;
	int len = 0;
	char p[1000000];
	//input
	scanf("%d", &n);

	//error check
	if (n < 1 || n>100000)
		return 0;

	input = (int*)malloc(sizeof(int) * n);
	copy = (int*)malloc(sizeof(int) * n);

	//input
	for (i = 0; i < n; i++) {
		scanf("%d", &input[i]);

		if (max < input[i])
			max = input[i];
		//init
		copy[i] = 0;
	}

	//제일 큰 수만큼 동적할당
	arr = (int*)malloc(sizeof(int) * max);

	i = 0;

	while (count < n) {
		check = input[i];
		if (flag) {
			for (j = 1; j <= check; j++) {
				p[len++] = '+';
				push(j);
			}
			flag = 0;
			flag2 = check;
		}
		else {
			if (flag2 < input[i]) {
				for (j = flag2+1; j <= check; j++) {
					p[len++] = '+';
					push(j);
				}
				flag2 = check;
			}
		}

		while (1) {
			check1 = pop();
			if (check1 < check) {
				printf("NO");
				return 0;
			}
			p[len++] = '-';
			copy[t++] = check1;

			if (check == check1)
				break;
		}
		i++;
		count++;
	}

	for (i = 0; i < len; i++)
		printf("%c\n", p[i]);

	return 0;
}

void push(int n)
{
	arr[top++] = n;
}

int pop()
{
	return arr[--top];
}
