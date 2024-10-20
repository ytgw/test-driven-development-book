package money;

public class Money {
    protected int amount;

    public boolean equals(Object object) {
        Money money = (Money) object;
        boolean isSameClass = this.getClass().equals(money.getClass());
        boolean isSameAmount = this.amount == money.amount;

        return isSameClass && isSameAmount;
    }

    static Dollar dollar(int amount) {
        return new Dollar(amount);
    }
}
