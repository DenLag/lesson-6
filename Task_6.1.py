from time import sleep


class TrafficLight:
    __color = "Чёрный"

    def running(self):
        while True:
            print('TrafficLight is red')
            sleep(7)
            print('TrafficLight is yellow')
            sleep(2)
            print('TrafficLight is green')
            sleep(7)
            print('TrafficLight is yellow')
            sleep(2)


trafficlight = TrafficLight()
trafficlight.running()
#commit for pull request