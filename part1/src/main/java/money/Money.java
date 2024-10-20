package money;

abstract class Money {
    protected int amount;
    protected String currency;

    abstract Money times(int multiplier);
    String currency() {
        return currency;
    }

    public boolean equals(Object object) {
        Money money = (Money) object;
        boolean isSameClass = this.getClass().equals(money.getClass());
        boolean isSameAmount = this.amount == money.amount;

        return isSameClass && isSameAmount;
    }

    static Money dollar(int amount) {
        return new Dollar(amount, "USD");
    }

    static Money franc(int amount) {
        return new Franc(amount, "CHF");
    }
}
