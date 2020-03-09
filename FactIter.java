public class FactIter {

    public static void main(String[] args) {
        System.out.println(fact_iter(3));
    }

    private static int fact_iter(int n) {
        int total = 1, k = 1;
        while (k <= n) {
            total = total * k;
            k = k + 1;
        }
        return total;
    }
}
