#define _CRT_SECURE_NO_WARNINGS

#include<stdio.h>
#define MAX 10000
// JangSungWon BaekJoon_10845

int queue[MAX];
int front = 0; //front
int rear = 0 ; // rear

void initq();
int b();
int f();
int empty();
int size();
int pop();
void push(int n);

int main(void)
{
	int N,i,input,output;
	int print[10000],len=0;
	char str[10];
	scanf("%d", &N);

	if (N < 1 || N>10000) // error check
		return 0;

	for (i = 0; i < N; i++)
	{
		scanf("%s", str);
		if (str[0] == 'p')
		{
			if (str[1] == 'u') { //push는 1번 더 입력받는다.
				scanf("%d", &input);
				push(input);
				continue;
			}
			//pop
			output = pop();
			if (output == -1)
				print[len++] = -1;
			else
				print[len++] = output;
			continue;
		}
		else if (str[0] == 's')//size
		{
			print[len++] = size();
			continue;
		}
		else if (str[0] == 'e')//empty
		{
			output = empty();
			if (output)
				print[len++] = 1;
			else
				print[len++] = 0;
			continue;
		}
		else if (str[0] == 'f')
		{
			output = f();
			if (output == -1)
				print[len++] = -1;
			else
				print[len++] = output;
			continue;
		}
		else if (str[0] == 'b')
		{
			output = b();
			if (output == -1)
				print[len++] = -1;
			else
				print[len++] = output;
			continue;
		}
	}


	for (i = 0; i < len; i++)
		printf("%d\n", print[i]);

	return 0;
}

void push(int n)
{
	if (rear > MAX - 1) //overflow
		return 0;
	queue[rear++] = n; //먼저 넣고 증가시킨다.
}

int pop()
{
	if (front == rear) // empty
		return -1;
	return queue[front++]; 
}

int size()
{
	return (rear - front);
}

int empty()
{
	if (front == rear)//empty
		return 1;
	else
		return 0;
}

int f()
{
	if (front == rear)//empty
		return -1;
	else 
		return queue[front];
}

int b()
{
	if (front == rear)//empty
		return -1;
	else {
		if (rear == 0)
			return queue[rear];
		else
			return queue[rear - 1];
	}
}

void initq()
{
	front = rear = 0; //0으로 초기화 front = (rear  = 0) 느낌으로 동작
}

