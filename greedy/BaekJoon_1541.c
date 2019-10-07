#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

int main(void)
{
	char a[51];
	int i, iom = 0, c = 1, p = 0, m = 0, len;

	scanf("%s", a);

	//전체 길이
	len = strlen(a);

	//-가 처음 나오는 위치 찾기.
	for (iom = 0; iom < len; iom++)
		if (a[iom] == '-')
			break;

	//- 처음 나오는 부분 앞
	for (i = iom - 1; i >= 0; i--) {
		if (a[i] == '+' || a[i] == '-') {
			c = 1;
		}
		else {
			p = p + (a[i] - '0') * c;
			c *= 10;
		}
	}
	c = 1;

	//- 이후
	for (i = len - 1; i > iom; i--) {
		if (a[i] == '+' || a[i] == '-') {
			c = 1;
		}
		else {
			m = m + (a[i] - '0') * c;
			c *= 10;
		}
	}

	printf("%d", p - m);

	return 0;
}