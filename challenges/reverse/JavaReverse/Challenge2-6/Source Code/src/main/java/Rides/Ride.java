package Rides;

public class Ride {
    private int seats;
    private int price;
    private String name;

    public Ride(int seats, int price, String name) {
        this.seats = seats;
        this.price = price;
        this.name = name;
    }

    public int getSeats() {
        return seats;
    }

    public void setSeats(int seats) {
        this.seats = seats;
    }

    public int getPrice() {
        return price;
    }

    public void setPrice(int price) {
        this.price = price;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

}