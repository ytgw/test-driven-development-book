package money;

class Dollar extends Money {
    Dollar(int amount) {
        this.amount = amount;
    }
    Dollar times(int multiplier) {
        return new Dollar(this.amount * multiplier);
    }
    public boolean equals(Object object) {
        Money money = (Money) object;
        return this.amount == money.amount;
    }
}
