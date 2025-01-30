import pygame
import random
import math
import matplotlib.pyplot as plt

# Constants
WIDTH, HEIGHT = 800, 600
POPULATION_SIZE = 200
INFECTION_RADIUS = 10
INFECTION_PROBABILITY = 0.2
RECOVERY_TIME = 300  # frames, not time, sprite has to move before recovering
MORTALITY_RATE = 0.2  # chance of dying per frame after infection
SPEED = 10  

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)  # healthy and susceptible
RED = (255, 0, 0)    # infected
BLUE = (0, 0, 255)   # recovered
BLACK = (0, 0, 0)    # dead or removed
LIGHT_RED = (255, 150, 150)  # infection field

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pandemic Simulator")
clock = pygame.time.Clock()

# Graph data
infected_count = []
recovered_count = []
deceased_count = []

def plot_graph():
    plt.figure(figsize=(8, 5))
    plt.plot(infected_count, label="Infected", color='red')
    plt.plot(recovered_count, label="Recovered", color='blue')
    plt.plot(deceased_count, label="Deceased", color='black')
    plt.xlabel("Time (frames)")
    plt.ylabel("Population Count")
    plt.legend()
    plt.title("Pandemic Simulation Statistics")
    plt.show()

class Person:
    def __init__(self, x, y, status="Healthy"):
        self.x = x
        self.y = y
        self.status = status
        self.dx = random.uniform(-SPEED, SPEED)
        self.dy = random.uniform(-SPEED, SPEED)
        self.infection_time = 0  # frames since infected
    
    def move(self):
        if self.status != "Deceased":
            self.x += self.dx
            self.y += self.dy
            
            # Keep within bounds
            if self.x <= 0 or self.x >= WIDTH:
                self.dx *= -1
            if self.y <= 0 or self.y >= HEIGHT:
                self.dy *= -1
    
    def draw(self):
        if self.status == "Healthy":
            color = GREEN
        elif self.status == "Infected":
            color = RED
        elif self.status == "Recovered":
            color = BLUE
        else:
            color = BLACK
        
        # Draw infection radius for infected persons
        if self.status == "Infected":
            pygame.draw.circle(screen, LIGHT_RED, (int(self.x), int(self.y)), INFECTION_RADIUS, 1)
        
        pygame.draw.circle(screen, color, (int(self.x), int(self.y)), 5)
    
    def update_infection(self):
        if self.status == "Infected":
            self.infection_time += 1
            if self.infection_time >= RECOVERY_TIME:
                if random.random() < MORTALITY_RATE:
                    self.status = "Deceased"
                else:
                    self.status = "Recovered"

class Simulation:
    def __init__(self):
        self.people = [Person(random.randint(0, WIDTH), random.randint(0, HEIGHT)) for _ in range(POPULATION_SIZE)]
        # infect one random person
        self.people[random.randint(0, POPULATION_SIZE-1)].status = "Infected"
    
    def update(self):
        infected = 0
        recovered = 0
        deceased = 0
        
        for person in self.people:
            person.move()
            person.update_infection()
            self.check_infection(person)
            person.draw()
            
            if person.status == "Infected":
                infected += 1
            elif person.status == "Recovered":
                recovered += 1
            elif person.status == "Deceased":
                deceased += 1
        
        infected_count.append(infected)
        recovered_count.append(recovered)
        deceased_count.append(deceased)
    
    def check_infection(self, person):
        if person.status == "Healthy":
            for other in self.people:
                if other.status == "Infected":
                    distance = math.sqrt((person.x - other.x) ** 2 + (person.y - other.y) ** 2)
                    if distance <= INFECTION_RADIUS and random.random() < INFECTION_PROBABILITY:
                        person.status = "Infected"
                        break
    
    def run(self):
        running = True
        while running:
            screen.fill(WHITE)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_g:
                    plot_graph()
            
            self.update()
            pygame.display.flip()
            clock.tick(30)
        pygame.quit()

if __name__ == "__main__":
    sim = Simulation()
    sim.run()
