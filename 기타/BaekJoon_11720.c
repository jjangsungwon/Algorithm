#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<math.h>
#include<string.h>
#include<stdlib.h>

int main(void)
{
	int N;
	char value[101];
	int sum = 0, i;
	int len;
	int result;
	scanf("%d", &N);
	scanf("%s", value);

	len = strlen(value);

	for (i = 0; i <len; i++) {
		result = value[i] - '0';
		sum += result;
	}

	printf("%d", sum);

	return 0;
}