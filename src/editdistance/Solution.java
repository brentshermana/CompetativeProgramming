package editdistance;

import java.util.*;
import java.util.function.Consumer;

public class Solution  {

    public static void main (final String[] args) {
        Scanner in = new Scanner(System.in);
        String a = in.next();
        String b = in.next();
        System.out.println(new Solution().minDistance(a,b));

    }

    static class Snapshot {

        public int changes;
        public int index1;
        public int index2;

        public Snapshot(int changes, int index1, int index2) {
            this.changes = changes;
            this.index1=index1;
            this.index2 = index2;
        }

        @Override
        public int hashCode() {
            return index1 + index2 * 179;
        }

        @Override
        public boolean equals(Object other) {
            if (other instanceof Snapshot) {
                Snapshot s = (Snapshot)other;

                return index1 == s.index1 && index2 == s.index2;
            }
            return false;
        }
    }

    //remember: convert word 1 into word 2, not the other way around!
    public int minDistance(String word1, String word2) {
        HashMap<Snapshot, Integer> minCost = new HashMap<>();

        PriorityQueue<Snapshot> q = new PriorityQueue<>(
                Comparator.comparingInt((Snapshot s) -> s.changes)
        );

        Consumer<Snapshot> addToQ = (Snapshot s) -> {
            if (s != null) {
                Integer current = minCost.get(s);
                if (current == null) {
                    minCost.put(s, s.changes);
                    q.add(s);
                }
                else if (current > s.changes) {
                    minCost.put(s, s.changes);
                    q.add(s);
                }
            }
        };

        addToQ.accept(new Snapshot(0, 0,0));
        while (true) { //the queue will just continue growing until we reach the solution:
            Snapshot current = q.remove();

            //check for matching condition:
            if (current.index2 == word2.length() && current.index1 == word1.length())
                return current.changes;

            //check to see if this is still the best option, based off of cost array
            if (minCost.get(current) < current.changes) {
                continue;
            }

            if (current.index1 == word1.length()) {
                //word1 has no characters remaining, the only change we can make is
                // to add the remaining characters in word2
                int moreChanges = word2.length() - current.index2;
                addToQ.accept( new Snapshot(current.changes + moreChanges, word1.length(), word2.length()));
            }
            else {
                if (current.index2 == word2.length()) {
                    //we have more chars remaining in word1, so our only remaining option
                    // is to remove all of them to produce a match
                    int moreChanges = word1.length()-current.index1;
                    addToQ.accept(new Snapshot(current.changes + moreChanges, word1.length(), word2.length()));
                }
                else {
                    char myChar = word1.charAt(current.index1);
                    char otherChar = word2.charAt(current.index2);
                    if (myChar == otherChar) {
                        //no changes need to be made, just look at the next char:
                        addToQ.accept(new Snapshot(
                                current.changes,
                                current.index1 + 1,
                                current.index2 + 1)
                        );
                    }
                    else {
                        //remove:
                        addToQ.accept(new Snapshot(current.changes+1, current.index1 + 1, current.index2));
                        //replace:
                        addToQ.accept( new Snapshot(current.changes+1, current.index1 + 1,current.index2 + 1));
                        //add:
                        addToQ.accept( new Snapshot(current.changes+1, current.index1, current.index2 + 1));
                    }
                }
            }
        }
    }

}