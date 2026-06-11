public class Solution {
    public string AddBinary(string a, string b) {
        
        int indexA = a.Length - 1;
        int indexB = b.Length - 1;
        int carry = 0;
        List<string> result = new List<string>();

        while (indexA >= 0 || indexB >= 0 || carry > 0){
            int total = carry;
            if (indexA > -1){
                total += a[indexA] - '0';
                indexA--;
            }
            if (indexB > -1){
                total += b[indexB] - '0';
                indexB--;
            }
            result.Add((total % 2).ToString());
            carry = total / 2;
        }
        result.Reverse();
        return string.Join("", result);
    

    }
}