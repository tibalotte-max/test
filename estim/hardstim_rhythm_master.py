# HardStim Rhythm Master Debug Application

# This script is for debugging the HardStim Rhythm Master application.

class HardStim:
    def __init__(self):
        self.state = 'off'

    def turn_on(self):
        self.state = 'on'
        print('HardStim is now ON')

    def turn_off(self):
        self.state = 'off'
        print('HardStim is now OFF')

    def get_state(self):
        return self.state

# Example usage
if __name__ == '__main__':
    hardstim = HardStim()
    hardstim.turn_on()
    print('Current state:', hardstim.get_state())
    hardstim.turn_off()