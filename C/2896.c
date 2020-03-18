#define _CRT_SECURE_NO_WARNINGS

#include<stdio.h>

int a, b, v;
int main() {
	
	scanf("%d %d %d", &a, &b, &v);
	
	printf("%d", (v - b - 1) / (a - b)+1);
	return 0;
}