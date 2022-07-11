/**
 * @param {number[][]} matrix
 * @param {number} target
 * @return {boolean}
 */

var searchMatrix = function(matrix, target) {
    let p1 = 0;
    let p2 = matrix.length - 1;
    let n = 0;
    
    // look for row
    while(p1<p2){
        let mid = p1+Math.floor((p2-p1)/2);
        if(target>=matrix[mid][0] && target<=matrix[mid][matrix[0].length-1]){
            n = mid;
            break;
        }
        
        if(matrix[mid][0] > target){
            p2 = mid - 1;
        }else{
            p1 = mid + 1;
        }
        
    }
    if(target>=matrix[p1][0] && target<=matrix[p1][matrix[0].length-1]){
            n = p1;
    }
    console.log(n);
    
    // check in row
    p1 = 0;
    p2 = matrix[0].length-1;
    
    while(p1<p2){
        let mid = p1+Math.floor((p2-p1)/2);
        if(mid < 0 || mid > matrix[0].lenght-1){
            return false;
        }
        //console.log(matrix[n][mid]]);
        console.log(mid);
        if(matrix[n][mid] == target) return true;
        
        if(matrix[n][mid] > target){
            p2 = mid - 1;
        }else{
            p1 = mid + 1;
        }
    }
    console.log(n);
    if(matrix[n][p1] == target) return true;
    return false;
    
    
};
