#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main()
{
    int n;
    vector<int> parents;
    cin >> n;
    for (int i = 0; i < n; ++i)
    {
        int inp;
        cin >> inp;
        parents.push_back(inp);
    };

    vector<int> heights;
    for (int i = 0; i < n; ++i)
    {
        heights.push_back(0);
    };

    int maxheight = 0;
    for (int vertex = 0; vertex < n; ++vertex)
    {
        if (heights[vertex] != 0)
        {
            continue;
        }
        int i = vertex;
        int height = 0;

        while (i != -1)
        {
            if (heights[i] != 0)
            {
                height += heights[i];
                break;
            }
            height++;
            i = parents[i];
        };

        maxheight = max(height, maxheight);
        i = vertex;

        while (i != -1)
        {
            if (heights[i] != 0)
            {
                break;
            }
            heights[i] = height;
            height--;
            i = parents[i];
        };
    };
    cout << maxheight << endl;
    return 0;
}