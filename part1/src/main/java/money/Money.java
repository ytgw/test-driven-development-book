package money;

class Money {
    protected int amount;
    protected String currency;

    Money(int amount, String currency) {
        this.amount = amount;
        this.currency = currency;
    }

    Money times(int multiplier) {
        return new Money(this.amount * multiplier, currency);
    }

    Money plus(Money addend) {
        return new Money(this.amount + addend.amount, this.currency);
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
