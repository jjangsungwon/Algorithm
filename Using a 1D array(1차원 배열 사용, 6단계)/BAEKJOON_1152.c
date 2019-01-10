#include<stdio.h>
#include<string.h>
#include<stdlib.h>

int count = 0;
void num(int arr[], int len);
int main(void)
{
	char ch[1000000];
	int i = 0;
	int count = 0;
	int flag = 1;
	gets(ch);

	while (ch[i] != 0) {
		if (flag) {
			count++;
			flag = 0;
		}

		if (ch[i] == ' ') {
			if (i == 0)
				count--;
			if (ch[i+1] == ' ' || ch[i+1] == '\n' || ch[i+1] == 0)
				count--;
			count++;
		}
		i++;
	}

	printf("%d", count);
	return 0;
}
