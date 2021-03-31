package telephone;

import java.util.Random;
import java.util.concurrent.locks.ReentrantLock;

public class Telephone {
    private final ReentrantLock locker;
    private boolean inUse;

    public Telephone() {
        this.locker = new ReentrantLock();
        this.inUse = false;
    }

    private void isEmpty() {
        if (inUse)
            throw new RuntimeException();
    }

    public void doCall() {
        isEmpty();
        locker.lock();
        inUse = true;
        threadSleep();
        inUse = false;
        locker.unlock();
    }

    private void threadSleep() {
        try {
            Thread.sleep(sleepTime());
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
    private long sleepTime() {
        Random random = new Random();
        return (random.nextInt(10 - 5) + 5) * 1000;
    }
}
