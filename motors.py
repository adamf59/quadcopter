import pigpio

class MotorUnit():
    
    def __init__(self) -> None:
        """
        A collection of motor objects, with access to GPIO pins for controlling them.
        """
        # get access to pigpio daemon
        self._gpio = pigpio.pi()

        # --- Define motors here ---
        self.motor_a = Motor(4, self._gpio)
        self.motor_b = Motor(17, self._gpio)
        self.motor_c = Motor(27, self._gpio)
        self.motor_d = Motor(22, self._gpio)
        # --- --- --- -- --- --- ---
    
    def arm_all(self):
        """
        Arms all motor ESCs.
        """
        self.motor_a.arm()
        self.motor_b.arm()
        self.motor_c.arm()
        self.motor_d.arm()

    def disarm_all(self):
        """
        Disarms all motor ESCs immediately. This function should not be run while in flight (for obvious reasons!).
        """
        pass

    def disconnect_gpio(self):
        """
        Closes resources used by pigpio. Cannot be reused once function is run.
        """
        self._gpio.stop()

class Motor:

    def __init__(self, gpio_pin: int, pi_gpio) -> None:
        """
        Create a new motor, controlled by an ESC connected to `gpio_pin`. See [pinout.xyz](https://pinout.xyz) for pinouts.
        """
        self._gpio_pin = gpio_pin

        self.pi_gpio = pi_gpio
        self._current_power = 0
        self._armed = False
    
    def arm(self):
        """
        Arms the ESC attached to the motor.
        """
        if not self._armed:
            self._armed = True
            self.pi

    def disarm(self):
        """
        Disarms the ESC attached to the motor.
        """
        if self._armed:
            pass
