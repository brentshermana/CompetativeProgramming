package coinchange;

import java.util.Arrays;
import java.util.Hashtable;
import java.util.Scanner;

/**
 * Created by admin on 4/21/17.
 */
public class Main {

    private static int[] coins;
    private static long[][] dp;

    public static void main (String[] args) {
        Scanner in = new Scanner(System.in);

        int n = in.nextInt(); //n <= 250
        int m = in.nextInt();
        dp = new long[n+1][m];
        //-1 denotes unsolved subproblem
        for (int i = 0; i < n+1; i++) {
            Arrays.fill(dp[i], -1);
        }

        coins = new int[m];
        for (int i = 0; i < m; i++) {
            coins[i] = in.nextInt();
        }

        Arrays.sort(coins); //in practice, low-high orderings have yielded higher
                            // instances of being able to use 'dp' array
        long answer = recurse(0, n);
        System.out.println(answer);
    }

    private static long recurse(int index, int rem) {
        //base cases
        if (rem == 0) { //served exact change
            return 1;
        }
        else if (index == coins.length) { //no more coins to consider
            return 0;
        }

        //not base cases
        if (dp[rem][index] != -1) { //already precomputed subproblem
            return dp[rem][index];
        }
        else { //have to do the work
            long value = 0;
            for (int cTake = 0; cTake * coins[index] <= rem; cTake++) {
                value += recurse(index+1, rem-cTake*coins[index]);
            }
            dp[rem][index] = value;
            return value;
        }
    }

    /*
    static int key(int index2, int rem) {
        //we know that the maximum amount of change
        // that can be asked for (and therefore the maximum value of rem)
        // is 250, so this simple function guarantees unique integer keys
        // for all subproblems
        return index2 * 251 + rem;
    }
    */

}
