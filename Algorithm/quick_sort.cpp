/*
数组为q，左边端点l，右边端点r
1. 确定分界点x (q[l], q[(l+r)>>1], q[r])
2. 根据分界点x，将数组分为两部分，左边部分小于等于x，右边部分大于等于x
3. 递归处理左右两部分


一种双指针的处理方式：
1. 选取分界点x
2. 从左往右找到第一个大于等于x的数，从右往左找到第一个小于等于x的数，交换两个数
3. 重复2，直到两个指针相遇
*/
#include <iostream>

using namespace std;

void swap(int *a, int *b)
{
    int tmp = *a;
    *a = *b;
    *b = tmp;
}

void quick_sort(int q[], int l, int r)
{
    if (l >= r)
        return;
    int x = q[l];
    int i = l;
    int j = r;
    while (i < j)
    {
        while (i < j && q[i] < x)
        {
            i++;
        }
        while (i < j && q[j] > x)
        {
            j--;
        }
        if (i < j)
            swap(&q[i], &q[j]);
        for (int i = 0; i < 5; i++)
        {
            printf("%d ", q[i]);
        }
        printf("\n");
    }

    quick_sort(q, l, j);
    quick_sort(q, j + 1, r);
}

// Test

int main()
{
    int array[5] = {2, 4, 5, 6, 1};
    for (int i = 0; i < 5; i++)
    {
        printf("%d ", array[i]);
    }
    printf("\n");
    quick_sort(array, 0, 4);
    for (int i = 0; i < 5; i++)
    {
        printf("%d ", array[i]);
    }
    printf("\n");
}