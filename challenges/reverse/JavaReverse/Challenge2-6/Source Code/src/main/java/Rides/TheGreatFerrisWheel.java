package Rides;

public class TheGreatFerrisWheel extends FerrisWheel {
    String currentColor;
    boolean lightsOn;

    public TheGreatFerrisWheel(String name) {
        super(100, 12, name, "10m/s");
        this.currentColor = "Red";
        this.lightsOn = false;
    }
}