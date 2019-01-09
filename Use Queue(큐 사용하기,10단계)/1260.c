#define _CRT_SECURE_NO_WARNINGS

#include<stdio.h>
#include<stdlib.h>

//JJang Sung Won BaekJoon 1260

int **arr;
int queue[1000];
int **copy;
void DFS(int start, int len);
void BFS(int start, int len);
int pop();
void push(int n);

int rear = 0;
int front = 0;

int main(void)
{
	int N, M, V;
	int i, x, y;

	//input
	scanf("%d %d %d", &N, &M, &V);

	arr = (int**)malloc(sizeof(int *) * (N+1));
	copy = (int**)malloc(sizeof(int *) * (N + 1));

	for (i = 0; i <= N; i++) {
		arr[i] = (int*)malloc(sizeof(int) * (N + 1));
		copy[i] = (int*)malloc(sizeof(int) * (N + 1));
	}
	for (i = 0; i <= N; i++) { //모든 값 0 초기화 (연결이 없는 상태)
		memset(arr[i], 0, N + 1);
		memset(copy[i], 0, N + 1);
	}

	//error check
	if (N < 1 || N>1000)
		return 0;
	if (M < 1 || M > 10000)
		return 0;

	for (i = 0; i < M; i++)
	{
		scanf("%d %d", &x, &y);
		arr[x][y] = 1;		   //연결 되었다고 표시
		arr[y][x] = 1;		   //양 방향
		copy[x][y] = 1;
		copy[y][x] = 1;
	}

	DFS(V, N);

	puts("");

	BFS(V, N);

	return 0;
}

void DFS(int start, int len)
{
	int i,j;
	printf("%d ", start);
	for (i = 1; i <= len; i++)
	{
		if (arr[start][i] == 1) {
			arr[start][i] = 2;
			arr[i][start] = 2; //사용했다는 의미.
			for (j = 1; j <= len; j++) {
				arr[j][start] = 2;
				arr[j][i] = 2;
			}

			DFS(i, len);
		}
	}
}

void BFS(int start, int len)
{
	printf("%d ", start);
	int i,j,result;
	for (i = 1; i <= len;i++) //push
		if (copy[start][i] == 1) {
			push(i);
			
			for (j = 1; j <= len; j++)
			{
				copy[j][i] = 2;
			}
		}


	for (j = 1; j <= len; j++)
	{
		copy[j][start] = 2;
	}

	result = pop();

	if (result == -1)
		return 0;
	else
		BFS(result, len);
}

void push(int n)
{
	queue[rear++] = n;
}

int pop()
{
	if (front == rear)
		return -1;
	return queue[front++];
}