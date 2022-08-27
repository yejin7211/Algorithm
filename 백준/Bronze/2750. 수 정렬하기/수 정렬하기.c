#include <stdio.h>
int main(){
    int num;
    scanf("%d",&num);
    int arr[1000];
    for(int i=0;i<num;i++)
        scanf("%d",&arr[i]);
    
    int temp;
    for(int i=0;i<num-1;i++)
    {
        for(int j=0;j<num-1;j++)
        {
            if(arr[j]>arr[j+1])
            {
                temp=arr[j];
                arr[j]=arr[j+1];
                arr[j+1]=temp;
            }
        }
    }
    for(int i=0;i<num;i++)
        printf("%d\n", arr[i]);
    
    return 0;
}







