public class sumDigits {

    public static void main(String[] args) {
        System.out.println(sum_digits(3));
    }

    private static int sum_digits(int n) {
        if (n < 10)
            return n;
        else {
            int all_but_last = (int) Math.floor((double) n / 10), last = n % 10;
            return (int) (sum_digits(all_but_last) + last);
        }
    }
}
