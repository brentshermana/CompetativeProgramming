import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.*;

/**
 * Created by admin on 3/22/17.
 */
/*
public class Enemy {

    public static void main (final String[] args) {
        Scanner in = new Scanner(System.in);
        new Orders().runOn(in);
    }

    void runOn(Scanner in) {
        int numValues = in.nextInt();
        int numQueries = in.nextInt();

        int[] values = new int[numValues];
        for (int i = 0; i < values.length; i++) {
            values[i] = in.nextInt();
        }

        HashMap<Interval, Integer> valueForRange = new HashMap<>();
        LinkedList<Interval> intervals = new LinkedList<Interval>();
        int base = 0;
        int str = values[0];
        for (int i = 0; i < values.length; i++) {
            if (values[i] != str || i == values.length-1) {
                if (i - base > 1) {
                    Interval significantInterval = new Interval(base, true, i-1, true);
                    valueForRange.put(significantInterval, str);
                    intervals.add(significantInterval);

                    str = values[i];
                    base = i;
                }
            }
        }

        //TODO: generate tree?
        Interval[] intervalArr = intervals.toArray(new Interval[intervals.size()]);
        intervals.clear();
        SegmentTree tree = new SegmentTree(intervalArr);

        for (int q = 0; q < numQueries; q++) {
            int lo = in.nextInt();
            int hi = in.nextInt();

            Interval 
        }

    }

    void runToFile(File f, Scanner in) {
        try {
            FileWriter writer = new FileWriter(f);
            int tests = in.nextInt();
            for (int t = 0; t < tests; t++) {
                StringBuffer sb = Orders.testCase(in);
                writer.write(sb.toString() + "\n");
            }
            writer.close();
        }
        catch (IOException e) {
            System.out.println();
        }
    }

    static StringBuffer testCase(Scanner in) {
    }

    static class SegmentTree {
        //binary tree

        //leaves correspond to endpoints of the interval
        //if there are X endpoints among all the intervals, there
        //  are 2X+1 leaves, so that the tree has the following:
        //example: numX = 3: < a x1 b x2 c x3 d >
        //a,b,c,d represent any point that falls between (or outside) these intervals

        //internal nodes correspond to intervals that are a union of elementary intervals
        // simply, a non-leaf node 'n's interval is the union of its children's intervals

        //each node/leaf stores a set of intervals

        //--------------------------------

        public STNode root;
        public Interval[] intervals;

        public SegmentTree(Interval[] intervals) {
            PriorityQueue<Integer> insertionSortQueue = new PriorityQueue<Integer>(intervals.length*2);
            for (Interval i : intervals) {
                insertionSortQueue.add(i.l);
                insertionSortQueue.add(i.r);
            }

            ArrayList<Integer> endPoints = new ArrayList<Integer>();
            endPoints.add(insertionSortQueue.remove());
            while (!insertionSortQueue.isEmpty()) {
                int next = insertionSortQueue.remove();
                if (next != endPoints.get(endPoints.size()-1))
                    endPoints.add(next);
            }
            endPoints.trimToSize();

            //create the tree structure
            LinkedList<STNode> previousLayer;
            LinkedList<STNode> currentLayer = new LinkedList<STNode>();

            //initialize currentLayer with leaves
            for (int i = 0; i < endPoints.size(); i++) {
                currentLayer.addLast(new STNode(new Interval(endPoints.get(i), true, endPoints.get(i), true)));
                if (i + 1 < endPoints.size())
                    currentLayer.addLast(new STNode(new Interval(endPoints.get(i), false, endPoints.get(i+1), false)));
            }

            //generate parents until we converge to root
            while (currentLayer.size() > 1) {
                previousLayer = currentLayer;
                currentLayer = new LinkedList<>();
                //empty previousLayer into currentLayer
                while (!previousLayer.isEmpty()) {
                    if (previousLayer.size() >= 2) {
                        STNode l = previousLayer.remove();
                        STNode r = previousLayer.remove();
                        currentLayer.add(new STNode(l, r));
                    }
                    else {
                        currentLayer.add(previousLayer.remove());
                    }
                }
            }
            //currentLayer's size is 1, containing the root
            this.root = currentLayer.remove();


            //add intervals:
            this.intervals = intervals;
            for (int i = 0; i < intervals.length; i++) {
                addInterval(intervals[i], i, root);
            }
        }




        void addInterval(Interval interval, int index2, STNode str) {
            if (interval.contains(str.interval)) {
                str.addIndex(index2);
            }
            else {
                if (interval.intersects(str.r.interval)) {
                    addInterval(interval, index2, str.r);
                }
                if (interval.intersects(str.l.interval)) {
                    addInterval(interval, index2, str.l);
                }
            }
        }

        public List<Interval> getIntervalsOverPoint(int point) {
            List<Interval> list = new LinkedList<Interval>();
            intervalsOverPoint(point, root, list);
            return list;
        }

        private void intervalsOverPoint(int point, STNode str, List<Interval> list) {
            for (Integer i : str.indexes)
                list.add(intervals[i]);
            if (!str.isLeaf()) {
                for (STNode child : new STNode[]{str.r, str.l}) {
                    if (child.interval.containsPoint(point, true)) {
                        intervalsOverPoint(point, child, list);
                    }
                }
            }
        }

        public String toString() {
            StringBuffer sb = new StringBuffer();
            int layers = numLayers(1, root);
            sb.append("layers " + layers + "\n");

            for (int i = 1; i <= layers; i++) {
                sb.append(layerString(i, root) + "\n");
            }

            return sb.toString();
        }
        private int numLayers(int currentLayer, STNode str) {
            if (str.isLeaf()) return currentLayer;
            else return Math.max(numLayers(currentLayer+1, str.r), numLayers(currentLayer+1, str.l));
        }
        private String layerString(int layer, STNode str) {
            if (layer == 1) return str.interval.toString();
            else {
                if (str.isLeaf())
                    return "<>";
                else
                    return layerString(layer-1, root.l) + " | " + layerString(layer-1, root.r);
            }
        }
    }

    static class Interval {
        int l;
        boolean hardL;
        int r;
        boolean hardR;

        //assumption: intervals left and right merge to form a contiguous union
        public static Interval union(Interval left, Interval right) {
            return new Interval(left.l, left.hardL, right.r, right.hardR);
        }

        public Interval(int left, boolean hardLeft, int right, boolean hardRight) {
            l = left;
            r = right;
            hardL = hardLeft;
            hardR = hardRight;
        }

        public boolean contains (Interval other) {
            if (other.l < l || other.r > r) {
                return false;
            }
            if (other.l == l && other.hardL && !hardL) {
                return false;
            }
            if (other.r == r && other.hardR && !hardR) {
                return false;
            }
            return true;
        }

        public boolean intersects (Interval other) {
            return other.containsPoint(r, hardR) ||
                    other.containsPoint(l, hardL) ||
                    this.containsPoint(other.r, other.hardR) ||
                    this.containsPoint(other.l, other.hardL);
        }

        public boolean containsPoint(int point, boolean hard) {
            if (point < l || point > r) return false; //falls outside interval
            if (point == l)
                return hardL && hard;
            if (point == r)
                return hardR && hard;
            return true; //inside interval
        }

        public boolean equals(Object other) {
            if (other instanceof Interval) {
                Interval i = (Interval) other;
                return i.r == r && i.l == l && i.hardR == hardR && i.hardL == hardL;
            }
            else {
                return false;
            }
        }

        public int hashCode() {
            return r * 29 + l * 127;
        }

        public String toString() {
            return (hardL ? "[" : "(") + l + "," + r + (hardR ? "]" : ")");
        }
    }

    static class STNode {
        public STNode r;
        public STNode l;

        public Interval interval;

        public HashSet<Integer> indexes = new HashSet<Integer>();

        public STNode(STNode l, STNode r) {
            this.interval = Interval.union(l.interval, r.interval);
            this.l = l;
            this.r = r;
        }
        public STNode(Interval i) {
            interval = i;
        }

        public boolean isLeaf() {
            return r == null && l == null;
        }

        public void addIndex(int i) {
            indexes = new HashSet<Integer>();
            indexes.add(i);
        }
    }
}
*/