package money;

class Dollar extends Money {
    private String currency;

    Dollar(int amount) {
        this.amount = amount;
        this.currency = "USD";
    }

    String currency() {
        return currency;
    }

    Money times(int multiplier) {
        return new Dollar(this.amount * multiplier);
    }
}
