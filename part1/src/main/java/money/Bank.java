package money;

import java.util.Map;
import java.util.HashMap;

class Bank {
    private Map<Pair, Integer> rates = new HashMap<>();

    Money reduce(Expression source, String to) {
        return source.reduce(this, to);
    }

    void addRate(String from, String to, int rate) {
        this.rates.put(new Pair(from, to), rate);
    }

    int rate(String from, String to) {
        if (from == to) return 1;
        return this.rates.get(new Pair(from, to));
    }
}
