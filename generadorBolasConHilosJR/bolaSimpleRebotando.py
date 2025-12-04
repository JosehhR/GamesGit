import pygame
import sys
import threading
import random
import math

class Bola(threading.Thread):
    def __init__(self, x, y, radio, color, vel_x, vel_y, ancho, alto, runer=True):
        super().__init__()
        self.x = x
        self.y = y
        self.radio = radio
        self.color = color
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.ancho = ancho
        self.alto = alto
        self.runer=runer
    
    def mover(self, ancho, alto):
        self.x += self.vel_x
        self.y += self.vel_y
        if self.x - self.radio <= 0 or self.x + self.radio >= ancho:
            self.vel_x *= -1
        if self.y - self.radio <= 0 or self.y + self.radio >= alto:
            self.vel_y *= -1
    
    def stop(self):
        self.runer=False

    def run(self):
        while self.runer:
            self.mover(ancho=self.ancho, alto=self.alto)
            pygame.time.wait(16)



class Ventana:

    def __init__(self, ancho, alto):

        pygame.init()
        self.ancho= ancho
        self.alto = alto
        
        self.ventana = pygame.display.set_mode((ancho, alto))
        pygame.display.set_caption("Bola Rebotando")
        self.bolas = []
        self.generarBolas()
        self.font = pygame.font.Font(None, 36)

    def generar_valor_sin_cero(self):
        while True:
            valor = random.randint(-3, 3)
            if valor !=0: 
                break
        return valor


    def generarBolas(self):
        print(self.generar_valor_sin_cero())
        bola=Bola(x=random.randint(100, 700), y=random.randint(100, 500), radio=random.randint(20, 50), color=(random.randint(0,255), random.randint(0,255), random.randint(0,255)), vel_x=self.generar_valor_sin_cero(), vel_y=self.generar_valor_sin_cero(), ancho=self.ancho, alto=self.alto)
        bola.start()
        self.bolas.append(bola)
        for bola in self.bolas:
            if bola.is_alive():
                pass

            else:
                bola.start()

    
    def dibujarPantalla(self):
        while True:
            self.ventana.fill((255, 255, 255))
                
            self.juego()
    
    def message(self,mensaje):
        textM = self.font.render(f"{mensaje}quieres volver a jugar?", True, (0,0,0))

    
    def juego(self):

        for bola in self.bolas:
            pygame.draw.circle(self.ventana, bola.color, (bola.x, bola.y), bola.radio)


        score_text_surface = self.font.render(f"Bolas Restantes: {len(self.bolas)}", True, (0,0,0))
        score_text_rect = score_text_surface.get_rect(center=(400, 20))
        self.ventana.blit(score_text_surface, score_text_rect)
        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                for bola in self.bolas:
                    bola.stop()
                pygame.quit()
                sys.exit()
            
            if evento.type == pygame.MOUSEBUTTONDOWN:
                mx, my = evento.pos
                nueva_lista=[]
                flag=False
                for bola in self.bolas:
                    if(((mx-bola.x)*(mx-bola.x))+((my-bola.y)*(my-bola.y))<=(bola.radio*bola.radio)):
                        bola.stop()
                        flag=True
                    else:
                        nueva_lista.append(bola)
                        
                self.bolas=nueva_lista
                if flag==True:
                    pass
                else:
                    self.generarBolas()
                pass

            
    

def main():
    ventana = Ventana(800, 600)
    ventana.dibujarPantalla()

# Ejecutar el programa
if __name__ == "__main__":
    main()