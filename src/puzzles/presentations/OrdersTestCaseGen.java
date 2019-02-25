import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Arrays;
import java.util.Random;
import java.util.Scanner;

/**
 * Created by admin on 3/23/17.
 */
public class OrdersTestCaseGen {

    public static void main (final String[] args) {
        try {
            File input = new File("in.dat");
            File output = new File("out.dat");

            FileWriter testWriter = new FileWriter(input);
            FileWriter solutionWriter = new FileWriter(output);

            //arg 1: number of testcases
            int testcases = Integer.parseInt(args[0]);

            testWriter.write(testcases + "\n");

            //arg 2: number of soldiers
            int numSoldiers = Integer.parseInt(args[1]);

            int[] ranks = new int[numSoldiers];
            for (int i = 0; i < ranks.length; i++) {
                ranks[i] = i + 1;
            }

            Random r = new Random(System.currentTimeMillis());

            for (int testcase = 0; testcase < testcases; testcase++) {

                //perform random swaps on the ranks
                for (int swaps = 0; swaps < numSoldiers * 3; swaps++) {
                    int i1 = r.nextInt(numSoldiers);
                    int i2 = r.nextInt(numSoldiers);
                    //swap
                    swap(ranks, i1, i2);
                }

                //write the answer to a file
                for (int i = 0; i < ranks.length; i++)
                    solutionWriter.write(ranks[i] + ((i < ranks.length-1) ? " " : ""));
                solutionWriter.write("\n");

                int[] leftMoves = new int[numSoldiers];
                Arrays.setAll(leftMoves, (int i) -> 0);
                //apply the sorting algorithm
                for (int i = 0; i < ranks.length; i++) {
                    int temp = i;
                    while (temp > 0 && ranks[temp] < ranks[temp-1]) {
                        leftMoves[i]++;
                        swap(ranks, temp, temp - 1);
                        temp--;
                    }
                }

                testWriter.write(numSoldiers + "\n");
                for (int i = 0; i < leftMoves.length; i++) {
                    testWriter.write(leftMoves[i] + ((i < ranks.length-1) ? " " : ""));
                }
                testWriter.write("\n");
            }

            solutionWriter.close();
            testWriter.close();

            //run tests
            Orders o = new Orders();
            FileReader reader = new FileReader(input);
            Scanner in = new Scanner(reader);
            File actout = new File("actout.dat");
            o.runToFile(actout, in);
        }
        catch (IOException e) {
            System.out.println("IOError");
        }


    }

    static void swap(int[] arr, int i1, int i2) {
        int temp = arr[i1];
        arr[i1] = arr[i2];
        arr[i2] = temp;
    }
}
