#include<stdio.h>

// BaekJoon 10828
void push(int n);
int t();
int empty();
int size();
int pop();

int arr[10000];
int top = -1;

int main(void)
{
	int N,i,input;
	char str[10];
	int print[10000], len = 0;
	scanf("%d", &N); //input
	
	if (N < 1 || N>10000) //error checks
		return 0;
	
	for (i = 0; i < N; i++)
	{
		scanf("%s", str);
		if (str[0] == 'p') {
			if (str[1] == 'u') {
				scanf("%d", &input);
				if (input < 1 || input>100000)
					return 0;
				push(input);
			}
			else {
				print[len++] = pop();
			}
		}
		else if (str[0] == 's')
			print[len++] = size();
		else if (str[0] == 'e')
			print[len++] = empty();
		else if (str[0] == 't')
			print[len++] = t();
	}

	for (i = 0; i < len; i++)
		printf("%d\n", print[i]);
	return 0;
}

int pop()
{
	if (top == -1)
		return -1;
	else
		return  arr[top--];
}

int size()
{
	return (top + 1);
}

int empty()
{
	if (top == -1)
		return 1;
	else
		return 0;
}

int t()
{
	if (top == -1)
		return -1;
	else
		return arr[top];
}

void push(int n)
{
	arr[++top] = n;
}