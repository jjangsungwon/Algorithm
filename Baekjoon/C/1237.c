#define _CRT_SECURE_NO_WARNINGS
#define TRUE 1
#define FALSE 0

#include<stdio.h>

struct Heap {
	int heapsize;
	int S[100];
};

struct Heap H;

int S[100];
int S2[100];

void siftdown(int i)
{
	int siftkey, parent, found,largerchild;

	siftkey = H.S[i];
	parent = i;
	found = FALSE;

	while ((2 * parent <= H.heapsize) && (!found))
	{
		if ((2 * parent < H.heapsize) && (H.S[2 * parent] >= H.S[2 * parent + 1]))
			largerchild = 2 * parent + 1;
		else
			largerchild = 2 * parent;

		if (siftkey > H.S[largerchild])
		{
			H.S[parent] = H.S[largerchild];
			parent = largerchild;
		}
		else
			found = TRUE;
	}
	H.S[parent] = siftkey;
}

//delete
int root()
{
	int keyout;

	keyout = H.S[1];
	H.S[1] = H.S[H.heapsize];
	H.heapsize = H.heapsize - 1;
	siftdown(1);
	
	return keyout;
}

void removeKeys(int n, int *S)
{
	for (int i = 1; i <= n; i++) {
		S[i] = root();
	}
}

void makeheap(int n)
{
	H.heapsize = n;
	for (int i = n / 2; i >= 1; i--)
		siftdown(i);
}


void heapsort(int n)
{
	makeheap(n);
	removeKeys(n, S);
}

void insert(int* n, int insertKEY) { 

  
	int i = 0;
	i = ++(*n);

	while ((i >= 1) && insertKEY < H.S[i / 2]) {
		H.S[i] = H.S[i / 2];
		i = i / 2; 
	}
	H.S[i] = insertKEY;
}

int main(void)
{
	FILE *fp1, *fp2;
	int num, n;
	fp1 = fopen("make.txt", "r");
	fp2 = fopen("input.txt", "r");

	//전체 크기
	fscanf(fp1, "%d", &n);

	for (int i = 1; i <= n; i++) {
		fscanf(fp1, "%d", &H.S[i]);
	}

	makeheap(n);
	//make heap 후 heap의 상태
	for (int i = 1; i <= 20; i++) {
		printf("%2d ", H.S[i]);
		S2[i] = H.S[i];
	}

	puts("");

	removeKeys(n, S);
	//heap sort한 상태
	for (int i = 1; i <= 20; i++) {
		printf("%2d ", S[i]);
		H.S[i] = S2[i];
	}

	puts("");

	
	H.heapsize = n;
	//insert, delete
	while (!feof(fp2))
	{
		fscanf(fp2, "%d", &num);

		if (num >= 0)
		{
			insert(&H.heapsize, num);
		}
		else
		{
			root();
		}

		for (int i = 1; i <= H.heapsize; i++)
			printf("%2d ", H.S[i]);
		puts("");

	}

	fclose(fp1);
	fclose(fp2);
	return 0;
}