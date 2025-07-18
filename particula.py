class Particula:
    def __init__(self, x, y, vx, vy, massa):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.massa = massa
        self.trajetoria_x = [x]
        self.trajetoria_y = [y]

    def newton(self, fx, fy, dt):
        # Atualiza a velocidade
        self.vx += fx * dt / self.massa
        self.vy += fy * dt / self.massa
        # Atualiza a posição
        self.x += self.vx * dt
        self.y += self.vy * dt
        # Salva a nova posição na trajetória
        self.trajetoria_x.append(self.x)
        self.trajetoria_y.append(self.y)

    def evoluir(self, fx_func, fy_func, dt):
        """Simula a evolução temporal enquanto y >= 0."""
        while self.y >= 0:
            fx = fx_func(self)
            fy = fy_func(self)
            self.newton(fx, fy, dt)
