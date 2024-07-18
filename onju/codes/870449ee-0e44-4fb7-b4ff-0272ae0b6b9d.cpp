#include <bits/stdc++.h>
using namespace std;
int main()
{
    int n,t=0,r=0,e;
    cin >> n;
    int arr[n];
    for (int i = 0; i < n; i++)
    {
        cin>>arr[i];
    }
    for (int i = 0; i < n; i++)
    {
        if(arr[i]%2!=0){
            t++;
        }
        else if(arr[i]%2==0){
            r++;
        }
    }
    if(t>r){
        for (int i = 0; i < n; i++)
        {
            if(arr[i]%2==0){
                cout<<i+1<<endl;
                break;
            }
        
        }
      
    }
       if(t<r){
        for (int i = 0; i < n; i++)
        {
            if(arr[i]%2!=0){
                cout<<i+1<<endl;
                break;
            }
        
        }
      
    }
    return 0;
}