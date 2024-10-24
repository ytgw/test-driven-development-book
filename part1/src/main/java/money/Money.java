package money;

class Money implements Expression {
    protected int amount;
    protected String currency;

    Money(int amount, String currency) {
        this.amount = amount;
        this.currency = currency;
    }

    Expression times(int multiplier) {
        return new Money(this.amount * multiplier, currency);
    }

    Expression plus(Expression addend) {
        return new Sum(this, addend);
    }

    public Money reduce(Bank bank, String to) {
        int rate = bank.rate(this.currency, to);
        return new Money(this.amount / rate, to);
    }

    String currency() {
        return currency;
    }

    public boolean equals(Object object) {
        Money money = (Money) object;
        boolean isSameCurrency = this.currency == money.currency;
        boolean isSameAmount = this.amount == money.amount;

        return isSameCurrency && isSameAmount;
    }

    public String toString() {
        return this.amount + " " + this.currency;
    }

    static Money dollar(int amount) {
        return new Money(amount, "USD");
    }

    static Money franc(int amount) {
        return new Money(amount, "CHF");
    }
}
