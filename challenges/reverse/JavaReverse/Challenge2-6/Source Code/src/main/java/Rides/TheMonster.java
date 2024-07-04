package Rides;

public class TheMonster extends Ride {

    private String height;
    private String speed;
    private String length;

    public TheMonster(int price, String name, String speed) {
        super(30, price, name);
        this.height = "100m";
        this.speed = speed;
        this.length = "500m";
    }

    public String getHeight() {
        return height;
    }

    public void setHeight(String height) {
        this.height = height;
    }

    public String getSpeed() {
        return speed;
    }

    public void setSpeed(String speed) {
        this.speed = speed;
    }

    public String getLength() {
        return length;
    }

    public void setLength(String length) {
        this.length = length;
    }

}