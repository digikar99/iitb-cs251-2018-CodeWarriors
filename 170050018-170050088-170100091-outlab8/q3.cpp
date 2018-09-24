#include<iostream>
#include<map>
#include<string>
#include<algorithm>
#include<unordered_set>
using namespace std;
int main()
{
	string s;
	map<string,int>mp;
	string filename;
	while(cin>>s)
	{
		if(s==" "||s=="\n")
		{
			continue;
		}
		else
		{
			transform(s.begin(),s.end(),s.begin(),::tolower);
			auto a=mp.find(s);
			if(a==mp.end())
			{
				mp[s]=1;
			}
			else
			{
				a->second=a->second+1;
			}
		}
	}

	unordered_set<string>stop_words={"and","the","is","in","at","of","his","her","him"};

	for(auto itr=mp.begin();itr!=mp.end();itr++)
	{
		if(stop_words.find(itr->first)==stop_words.end())
		cout<<itr->first<<","<<itr->second<<"\n";
	}
}