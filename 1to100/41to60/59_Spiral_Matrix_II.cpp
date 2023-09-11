class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        vector<vector<int>> matrix(n, vector<int>(n, 0));
        int x = 1; // Start from 1
        int RS = 0; // Row start
        int RE = n - 1; // Row end
        int CS = 0; // Column start
        int CE = n - 1; // Column end

        while(x <= n * n){
            for(int i = CS; i <= CE; i++){
                matrix[RS][i] = x++;
            }
            RS++;

            for(int i = RS; i <= RE; i++){
                matrix[i][CE] = x++;
            }
            CE--;

            for(int i = CE; i >= CS; i--){
                matrix[RE][i] = x++;
            }
            RE--;

            for(int i = RE; i >= RS; i--){
                matrix[i][CS] = x++;
            }
            CS++;
        }

        return matrix;
    }
};
