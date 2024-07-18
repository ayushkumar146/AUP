#include <bits/stdc++.h>
using namespace std;
#define ll long long int
#define take(x) int x; cin>>x;
 
#define getv(v, n)  vector<int> v;for (int i = 0; i < n; i++){ take(x) v.push_back(x);}
 
#define all(v) v.begin(), v.end()
 
#define allr(v) v.rbegin(), v.rend()
 
#define sortv(v) sort(all(v))
 
#define sortvr(v) sort(allr(v))
 
#define gcd(a,b)  __gcd(a,b)
 
#define mem1(a) memset(a,-1,sizeof(a))
 
#define mem0(a) memset(a,0,sizeof(a))
 
#define pb push_back
 
#define pob pop_back
 
#define yes cout <<YES<< endl
 
#define no cout <<NO<< endl
 
#define ff first
 
#define ss second
 
#define MOD 1000000007
 
#define INF 1e18
 
#define ppc(x) __builtin_popcountll(x);
int len;
class query{
    public:
    int l,r,idx;
};
 
bool comp(query a,query b){
    if(a.l/len!=b.l/len){
        return a.l<b.l;
    }
    else{
        return a.r<b.r;
    }
    
}
 
int main()
{
    
    int n;
    cin >> n;
    
    vector<int>v;
    
    for (int i = 0; i < n; i++)
    {
        take(x);
        v.pb(x);
    }
    int q;
    cin>>q;
    vector<query>que(q+1);
    vector<int>v1(q+1,0);
    for (int i = 0; i < q; i++)
    {
        cin>>que[i].l>>que[i].r;
        que[i].idx=i;
        que[i].l--;
        que[i].r--;
    }
     len =sqrt(n);
     unordered_map<int,int>m;
    sort(que.begin(),que.begin()+q,comp);
    for (int i = 0; i < q; i++)
    {
        // cout<<que[i].l<<" "<<que[i].r<<" "<<que[i].idx<<endl;
    }
    int ML=0,MR=-1;
    int cnt=0;
    for (int i = 0; i < q; i++)
    {
        int L=que[i].l;
        int R=que[i].r;
        
        while(MR<R){
            MR++;
            m[v[MR]]++;
               if(m[v[MR]]==1){
                cnt++;
            }
            
        }
        while(ML<L){
            m[v[ML]]--;
            if(m[v[ML]]==0){
                cnt--;
            }
            ML++;
        }
        while(ML>L){
            ML--;
            m[v[ML]]++;
            if(m[v[ML]]==1){
                cnt++;
            }
           
        }
        while(MR>R){
            m[v[MR]]--;
            if(m[v[MR]]==0){
                cnt--;
            }
            MR--;
        }
        v1[que[i].idx]=cnt;
    }
    for (int i = 0; i < q; i++)
    {
        cout<<v1[i]<<endl;
    }
 
    return 0;
}