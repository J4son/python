import pygame
import time

FOREGROUND=(255,255,255)
FOREGROUND2=(128,128,128)
REDFOREGROUND=(255,128,128)
BACKGROUND=(0,0,0)

class Timer(object):
    def __init__(self, options):
        self.options = options
        opt = pygame.HWSURFACE | pygame.DOUBLEBUF
        if self.options.fullscreen:
            opt |= pygame.FULLSCREEN
        pygame.init()
        self.scr = pygame.display.set_mode((1024,768), opt)
        self.font = pygame.font.Font(pygame.font.get_default_font(), 400)
    
    def write(self, txt, col=None):
        if col is None:
            col = FOREGROUND
        t = self.font.render(txt, True, col)
        self.scr.fill(BACKGROUND)
        self.scr.blit(t, (20,20))
        pygame.display.flip()
#        pygame.display.update()

    def write_time(self, t, col=None):
        self.write("%02i:%02i" % (t/60, t%60), col=col)



    def run(self, t):
        while True:
           self.write_time(t)
           state = "STOPPED"
           tremain = t
           tfin = 0
           while True:
               for event in pygame.event.get():
                   if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == 0x1b:
                       state = "QUIT"
                       break
                   elif event.type == pygame.KEYDOWN:
                       if event.key == ord("r"):
                           state="RESET"
                           break
                       elif state == "STOPPED":
                           state = "STARTED"
                           tfin = time.time()+tremain
                       elif state == "STARTED":
                           if tfin < time.time():
                               state = "RESET"
                               break
                           else:
                               tremain = tfin-time.time()
                               state = "STOPPED"
               if state == "QUIT":
                   break
               elif state == "RESET":
                   break
               elif state == "STARTED":
                   if tfin >= time.time():
                       self.write_time(tfin-time.time())
                   else:
                       self.write_time(0, col=[FOREGROUND, REDFOREGROUND][int((tfin-time.time())*2.5)%2])
               elif state == "STOPPED":
                   self.write_time(tremain, col=[FOREGROUND, FOREGROUND2][int((tfin-time.time())*1.5)%2])
                   
               pygame.time.delay(25)
           if state == "QUIT":
               break



def main():
    from argparse import ArgumentParser

    parser = ArgumentParser(epilog="Keys: [Esc] = exit , [r] = reset , [any other key] = start/stop")
    parser.add_argument("--timer", "-t", default=300, type=int,
                        help="Start countdown at SECONDS", metavar="SECONDS")
    parser.add_argument("--fullscreen", "--fs", "-F", action="store_true",
                        help="Fullscreen")

    options = parser.parse_args()

    print options.fullscreen
    t = Timer(options)
    try:
        t.run(options.timer)
    except KeyboardInterrupt:
        pass
        
 
if __name__ == "__main__":
    main()
