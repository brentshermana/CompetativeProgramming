package frequent;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.*;

/**
 * Created by admin on 3/25/17.
 */
public class TestGenerator {

    static int max = 1000000;
    static double repeatOdds = 0.5;
    public static void main (final String[] args) throws IOException {
        //first arg: length of array
        //second arg: number of queries

        FileWriter solution = new FileWriter(new File("sol.dat"));
        FileWriter test = new FileWriter(new File("test.dat"));
        Scanner in = new Scanner(System.in);
        Random r = new Random(System.currentTimeMillis());

        int len = in.nextInt();
        int queries = in.nextInt();

        test.write(len + " " + queries + "\n");


        int[] values = new int[len];
        int current = 1;
        for (int i = 0; i < values.length; i++) {
            if (r.nextDouble() < repeatOdds)
                values[i] = current;
            else {
                current = current + 2;
                values[i] = current;
            }
            test.write(values[i] + " ");
        }
        test.write("\n");

        //generate queries and answers
        for (int q = 0; q < queries; q++) {
            int lo = rrange(r, 0, len-1);
            int hi = rrange(r, lo+1, len);
            test.write((lo+1) + " " + (hi+1) + "\n");

            int max = 1;
            current = 1;
            for (int i = lo+1; i <= hi; i++) {
                if (values[i] == values[i-1]) {
                    current++;
                }
                else {
                    current = 1;
                }
                max = Math.max(max, current);
            }
            solution.write(max + "\n");
        }

        test.close();
        solution.close();
    }

    static int rrange(Random r, int lo, int hi) { //hi not inclusive
        int diff = hi-lo;
        int val = r.nextInt(diff);
        return val + lo;
    }
}
