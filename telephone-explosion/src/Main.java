import telephone.Telephone;

class MyThread extends Thread {
    private final Telephone telephone;

    public MyThread(String name, Telephone telephone) {
        super(name);
        this.telephone = telephone;
    }

    @Override
    public void run() {
        try {
            telephone.doCall();
        } catch (RuntimeException e) {
            System.out.println("Telephone station has been exploded");
        }
    }
}

public class Main {
    public static void main(String[] args) {
        Telephone telephone = new Telephone();

        new MyThread("Bob", telephone).start();
        new MyThread("Alex", telephone).start();
        new MyThread("Jack", telephone).start();
        new MyThread("None", telephone).start();
    }
}
