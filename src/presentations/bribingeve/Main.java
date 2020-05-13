package bribingeve;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 * Created by admin on 4/1/17.
 */
public class Main {
    static BufferedReader reader;
    static StringTokenizer st;
    static int nextInt() throws IOException {
        if (!st.hasMoreTokens()) st = new StringTokenizer(reader.readLine());
        return Integer.parseInt(st.nextToken());
    }

    public static void main (final String[] args) throws IOException {
        reader = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(reader.readLine());

        int n = nextInt()-1; //number of competitors

        int a = nextInt();
        int b = nextInt();

        int betterA = 0;
        int betterB = 0;
        int aTie = 0;
        int bTie = 0;

        for (int i = 0; i < n; i++) {
            int ai = nextInt();
            int bi = nextInt();

            if (a < ai) betterA++;
            if (b < bi) betterB++;
            if (a == ai) aTie++;
            if (b == bi) bTie++;
        }

        int best = 1 + Math.min(betterA, betterB);
        int worst = 1 + Math.max(betterA + aTie, betterB + bTie);

        System.out.printf("%d %d\n", best, worst);
    }
}
