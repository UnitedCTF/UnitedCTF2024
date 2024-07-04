package Rides;

public class FerrisWheel extends Ride {


    private String rotatingSpeed;

    public FerrisWheel(int seats, int price, String name, String rotatingSpeed) {
        super(seats, price, name);
        this.rotatingSpeed = rotatingSpeed;
    }


    public String getRotatingSpeed() {
        return rotatingSpeed;
    }

    public void setRotatingSpeed(String rotatingSpeed) {
        this.rotatingSpeed = rotatingSpeed;
    }
}