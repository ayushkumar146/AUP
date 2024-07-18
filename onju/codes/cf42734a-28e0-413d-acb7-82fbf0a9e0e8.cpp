#include <bits/stdc++.h>
using namespace std;

// Function to perform vector addition
vector<int> addVectors(const vector<int>& v1,
                    const vector<int>& v2)
{
    vector<int> result;
    if (v1.size() != v2.size()) {
        cerr << "Vectors must be of the same size for "
                "addition."
            << endl;
        return result; // Returning an empty vector
                    // indicating an error
    }

    result.reserve(v1.size());
    for (size_t i = 0; i < v1.size(); ++i) {
        result.push_back(v1[i] + v2[i]);
    }

    return result;
}

// Function to perform vector subtraction
vector<int> subtractVectors(const vector<int>& v1,
                            const vector<int>& v2)
{
    vector<int> result;
    if (v1.size() != v2.size()) {
        cerr << "Vectors must be of the same size for "
                "subtraction."
            << endl;
        return result; // Returning an empty vector
                    // indicating an error
    }

    result.reserve(v1.size());
    for (size_t i = 0; i < v1.size(); ++i) {
        result.push_back(v1[i] - v2[i]);
    }

    return result;
}

// Driver code
int main()
{

    // Example vectors
    vector<int> vector1 = { 1, 2, 3, 4, 5 };
    vector<int> vector2 = { 5, 4, 3, 2, 1 };

    // Perform vector addition
    vector<int> sum = addVectors(vector1, vector2);
    cout << "Vector Addition Result: ";
    for (int value : sum) {
        cout << value << " ";
    }
    cout << endl;

    // Perform vector subtraction
    vector<int> difference
        = subtractVectors(vector1, vector2);
    cout << "Vector Subtraction Result: ";
    for (int value : difference) {
        cout << value << " ";
    }
    cout << endl;

    return 0;
}