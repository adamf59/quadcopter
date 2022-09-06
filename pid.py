class PIDController:

    def __init__(self, kP, kI, kD, kG) -> None:
        """
        Create a new PID controller, with constants kP, kI, and kD and a gain term.
        """

        # initialize constants
        self._p = kP
        self._i = kI
        self._d = kD
        self._g = kG
        
        # initialize error tracking terms
        self._error_sum = 0
        self._error_last = None
    
    def set_kP(self, kP):
        """
        Set the proportional term kP
        """
        self._p = kP
    
    def set_kI(self, kI):
        """
        Set the integral term kI
        """
        self._p = kI
    
    def set_kD(self, kD):
        """
        Set the derivative term kD
        """
        self._p = kD

    def set_kG(self, kG):
        """
        Set the gain term kG
        """
        self._g = kG
    
    def output(self, error):
        """
        Gets the output from the PID controller given the error.
        """

        # check if the previous error was None (meaning this is the first data point)
        if self._error_last is None:
            self._error_last = error

        # calculate derivative
        error_delta = error - self._error_last
        self._error_last = error

        # accumulate error
        self._error_sum += error

        return (error * self._p) + (error_delta * self._d) + (self._error_sum * self._i) + self._g
        
