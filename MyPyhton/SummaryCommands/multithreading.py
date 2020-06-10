import threading
import time

# We can literally cut this time by a magnitude of four if we run each process on its own thread
def paint_wall():
  print('Painting wall...')
  # Wait 30m
  time.sleep(1800)
  print('Done painting wall')

walls_to_paint = 4

for k in range(0, walls_to_paint):
     t = threading.Thread(target=paint_wall)
     t.start()
     



# multithreading in abstract class
import threading
import time
import abc


class TradingSystem(abc.ABC):

    @abc.abstractclassmethod
    def absractloop(self):
        pass

    def mainloop(self):
        while(True):
            self.absractloop()
            time.sleep(self.timeframe)


    def __init__(self, ticker, timeframe):
        self.ticker = ticker
        self.timeframe = timeframe
        t = threading.Thread(target=self.mainloop)
        t.start()