package frequent;
import java.io.*;

import java.util.*;

/**
 * Created by admin on 3/25/17.
 */
//spoj FREQUENT

public class Main {

    public static void main (final String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));
        while (true) {
            //get the data
            StringTokenizer st = new StringTokenizer(in.readLine());
            int size = Integer.parseInt(st.nextToken());
            if (size == 0) break; //end of tests
            int queries = Integer.parseInt(st.nextToken());
            int[] values = new int[size];
            st = new StringTokenizer(in.readLine());
            for (int i = 0; i < size; i++) {
                values[i] = Integer.parseInt(st.nextToken());
            }
            //get all nontrivial (size > 1) intervals of consecutive values
            LinkedList<Interval> intervals = new LinkedList<>();
            int base = 0;
            while (base < size) {
                int current = base + 1;
                while (current < size) {
                    if (values[current] == values[base]) current++;
                    else break;
                }
                if (base-current > 1)
                    intervals.add(new Interval(base, current-1));
                base = current;
            }

            //create the interval tree
            IntervalTree tree = new IntervalTree(intervals);
            //process the queries
            for (int q = 0; q < queries; q++) {
                st = new StringTokenizer(in.readLine());
                int ql = Integer.parseInt(st.nextToken()) - 1;
                int qr = Integer.parseInt(st.nextToken()) - 1;
                Interval query = new Interval(ql, qr);
                LinkedList<Interval> intersecting = tree.intersectingIntervals(query);
                int bestLength = -1;
                for (Interval i : intersecting) {
                    Interval intersection = query.intersection(i);
                    if (intersection.length() > bestLength) {
                        bestLength = intersection.length();
                    }
                }
                out.write(Integer.toString(bestLength));
                out.write("\n");
            }
        }
    }



    public static class IntervalTree {
        Node root;
        IntervalTree(LinkedList<Interval> intervals) {
            if (!intervals.isEmpty()) // avoid div by 0 error when getting average
                root = new Node(intervals); //Node constructor handles heavy lifting
        }
        LinkedList<Interval> intersectingIntervals(Interval i) {
            LinkedList<Interval> set = new LinkedList<>();
            addIntersectingIntervals(i, set, root);
            return set;
        }
        void addIntersectingIntervals(Interval i, LinkedList<Interval> set, Node current) {
            if (current != null) {
                if (i.containsPoint(current.point)) {
                    set.addAll(current.ltor); //same content as rtol, just a different ordering
                }
                else {
                    ListIterator<Interval> it;
                    if (current.point < i.l) //interval is to the right
                        it = current.rtol.listIterator();
                    else //interval is to the left
                        it = current.ltor.listIterator();
                    while (it.hasNext()) {
                        Interval temp = it.next();
                        if (i.intersects(temp)) set.add(temp);
                        else break; //nothing after this one will intersect
                    }
                }
                if (i.l < current.point)
                    addIntersectingIntervals(i, set, current.l);
                if (i.r > current.point)
                    addIntersectingIntervals(i, set, current.r);
            }
        }
    }

    static class Node {

        LinkedList<Interval> ltor = new LinkedList<>();
        LinkedList<Interval> rtol = new LinkedList<>();
        Node r;
        Node l;
        int point;

        public Node(LinkedList<Interval> intervals) {
            //get the average of the endpoints
            this.point = averageOfEndPoints(intervals);
            //sort intervals into three categories:
            LinkedList<Interval> left = new LinkedList<>();
            LinkedList<Interval> right = new LinkedList<>();
            while (!intervals.isEmpty()) {
                Interval i = intervals.remove();
                if (i.containsPoint(point)) {
                    ltor.add(i);
                    rtol.add(i);
                }
                else if (i.r < point) {
                    left.add(i);
                }
                else /*if (i.l > point)*/ {
                    right.add(i);
                }
            }
            //sort the intersecting list by
            //  increasing left endpoint
            //  decreasing right endpoint
            ltor.sort((Interval a, Interval b) ->
                    Integer.compare(a.l, b.l));
            rtol.sort((Interval a, Interval b) ->
                    -Integer.compare(a.r, b.r));

            //create children
            if (!right.isEmpty()) r = new Node(right);
            if (!left.isEmpty()) l = new Node(left);
        }
    }

    static int averageOfEndPoints(Collection<Interval> intervals) {
        long sum = 0;
        for (Interval i : intervals) {
            sum += i.r + i.l;
        }
        sum /= intervals.size()*2;
        return (int) sum;
    }

    static class Interval {
        int l;
        int r;

        //assumption: intervals left and right merge to form a contiguous union
        public static Interval union(Interval left, Interval right) {
            return new Interval(left.l, right.r);
        }

        public Interval(int left, int right) {
            l = left;
            r = right;
            if (l > r) throw new RuntimeException();
        }

        public boolean intersects (Interval other) {
            return !(l > other.r || r < other.l);
        }

        public Interval intersection(Interval other) {
            if (!intersects(other)) throw new RuntimeException();
            return new Interval(Math.max(l, other.l), Math.min(r, other.r));
        }

        public boolean containsPoint(int point) {
            return (point >= l && point <= r);
        }

        public String toString() {
            return "[" + l + ", " + r + "]";
        }

        public int length() {
            return r - l + 1;
        }
    }

}