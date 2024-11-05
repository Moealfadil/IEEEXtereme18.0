#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_set>
#include <limits>

using namespace std;

class UnionFind {
public:
    UnionFind(int n) : parent(n), rank(n, 0) {
        for (int i = 0; i < n; ++i) {
            parent[i] = i;
        }
    }

    int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }

    void unionSet(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);
        if (rootX != rootY) {
            if (rank[rootX] > rank[rootY]) {
                parent[rootY] = rootX;
            } else if (rank[rootX] < rank[rootY]) {
                parent[rootX] = rootY;
            } else {
                parent[rootY] = rootX;
                rank[rootX]++;
            }
        }
    }

private:
    vector<int> parent;
    vector<int> rank;
};

vector<int> shortest_string_to_connect_components(const string& S) {
    int N = S.size();
    vector<int> dp(N + 1, numeric_limits<int>::max());
    dp[0] = 0;

    for (int length = 1; length <= N; ++length) {
        for (int start = 0; start <= N - length; ++start) {
            string substring = S.substr(start, length);
            UnionFind uf(N + 1);

            for (int i = 0; i <= N - length; ++i) {
                if (S.substr(i, length) == substring) {
                    for (int j = i; j < i + length - 1; ++j) {
                        uf.unionSet(j + 1, j + 2);
                    }
                }
            }

            unordered_set<int> components;
            for (int i = 1; i <= N; ++i) {
                components.insert(uf.find(i));
            }

            int connected_components = components.size();
            dp[connected_components] = min(dp[connected_components], length);
        }
    }

    vector<int> result(N);
    for (int k = 1; k <= N; ++k) {
        result[k - 1] = (dp[k] == numeric_limits<int>::max()) ? 0 : dp[k];
    }

    return result;
}

int main() {
    string S;
    cin >> S;

    vector<int> result = shortest_string_to_connect_components(S);
    for (int r : result) {
        cout << r << " ";
    }
    cout << endl;

    return 0;
}
