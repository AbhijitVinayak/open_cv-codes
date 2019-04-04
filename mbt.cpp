#include <iostream>
#include <list>
using namespace std;
list<int> l;
int main() {
  /* code */
  int n;
  cin>>n;
  l.push_back();
  cin>>n;
  l.push_back();
  cin>>n;
  l.push_back();
  list<int>::iterator it;
  for(it=l.begin();it!=l.end();it++)
  {
    cout<<*it<<" ";
  }
  l.pop_front();
  cout<<"\n"<<l.front()<<endl;
  return 0;
}
