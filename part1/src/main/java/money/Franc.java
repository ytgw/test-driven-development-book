package money;

class Franc extends Money {
    private String currency;

    Franc(int amount) {
        this.amount = amount;
        this.currency = "CHF";
    }

    String currency() {
        return currency;
    }

    Money times(int multiplier) {
        return new Franc(this.amount * multiplier);
    }
}
