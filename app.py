class Registrar_jugador:

    def _init_(self,nombre,fichas):
        self.nombre = nombre
        self.fichas = fichas

    def registrar_jugador(self):
        pass

class Iniciar_juego:

    def _init_(self, carta):
        self.carta = carta

    def revolver(self):
        pass

    def iniciar_juego(self, apuesta):
        self.apuesta = apuesta

    def inicializar_mano(self, cartas):
        self.cartas = cartas

        def repartir_carta(self, tapada: bool):
            pass

        def backjack(self):
            pass

class Hacer_jugada_del_jugador:
        def _init_(self, hacer_jugada):
            pass

        def pedir_carta(self):
            pass

        def repartir_carta(self):
            pass

        def mano_del_jugador_menor_21(self):
            pass

        def mano_del_jugador_mayor_21(self):
            pass

        def jugador_se_planta(self):
            pass

class Hacer_jugada_de_la_casa:

        def _init_(self, destapar_la_carta_oculta):
            pass

        def mano_blackjack(self, finalizar_juego):
            pass

        def mano_no_es_blackjack(self, repartir_carta):
            pass

        def calcular_valor_mano(self):
            pass

        def mano_jugador_menor_21(self, jugada):
            pass

        def mano_casa_mayor_igual_menor(self):
            pass

        def mano_mayor_21(self):
            pass

class Finalizar_juego:

        def _init_(self, destapas_carta):
            pass

        def jugador_gano(self, doblar_fichas):
            pass

        def jugador_perdio(self, restar_fichas):
            pass

        def empate(self, devolver_ficha_jugador):
            pass

        def menu(self, iniciar_juego, finalizar_juego):
            pass

        def no_tiene_fichas(self, finalizar_juego):
            pass