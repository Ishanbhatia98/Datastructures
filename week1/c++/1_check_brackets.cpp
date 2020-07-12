#include<iostream>
#include<string>
#include<stack>
#include<vector>

using namespace std;

class pairs{
    int _x;
    char _c;
    public:
        pairs(char c, int i): _c(c), _x(i){}
        pairs(const pairs & rhs) {
            _x = rhs._x;
            _c = rhs._c;
        }

        int index(){return _x;}
        char ch(){return _c;}
};

class dict{
    char _k = 'a';
    char _v = 'a';
    public:
        //dict(char k, char v): _k(k), _v(v){}
        dict(char k, char v){
            _k = k;
            _v = v;
        }
        char key(){return _k;}
        char value(){return _v;}
};

int check(string s){
    if(s.size()==1){
        return 1;
    }
    dict sq('[', ']');
    dict ro('(', ')');
    dict cu('{', '}');
    vector<dict> brackets{sq, ro, cu};

    stack<pairs> stack;

    for(int i=0; i<s.size();++i){
        for(auto b:brackets){
            if(s[i]==b.key()){
                pairs item(s[i], i);
                stack.push(item);
            }else if(s[i]==b.value()){
                if(stack.empty()){
                    return i+1;
                }
                pairs item = stack.top();
                stack.pop();

                char br;
                for(auto type:brackets){
                    if(type.value()==s[i]){
                        br = type.key();
                        break;
                    }
                };
                if(item.ch()!=br){
                    //cout << item.ch() << br << endl;
                    return i+1;
                }
            }
        }

    };
    if(stack.empty()){
        return -1;
    }else{
        pairs item = stack.top();
        return item.index()+1;
    }

}

int main(){
    string s;
    cin >> s;
    int ans = check(s);
    if(ans==-1){
        cout << "Success" << endl;
    }else{
        cout << ans << endl;
    }
    return 0;
}