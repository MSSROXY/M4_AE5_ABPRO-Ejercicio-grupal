class Bicicleta:
    def __init__(self, id_bici, estado="disponible"):
        self.id_bici = id_bici
        self.estado = estado  # disponible, reservada, mantenimiento

    def __str__(self):
        return f"Bicicleta {self.id_bici} - Estado: {self.estado}"

class ReservaInvalidaError(Exception):
    #Excepción personalizada para errores en reservas
    pass 
    
class Reserva:
    def __init__(self, bicicleta, cliente):
        self.bicicleta = bicicleta
        self.cliente = cliente

    def confirmar(self):
        #Confirma la reserva si la bicicleta está disponible. Lanza excepción si no se puede reservar.
        if self.bicicleta.estado != "disponible":
            raise ReservaInvalidaError(
                f"No se puede reservar la bicicleta {self.bicicleta.id_bici}. Estado: {self.bicicleta.estado}"
            )
        self.bicicleta.estado = "reservada"
        return f"Reserva confirmada para {self.cliente} con la bicicleta {self.bicicleta.id_bici}"


# SISTEMA DE RESERVA
class SistemaReservas:
    def __init__(self):
        self.bicicletas = []  # almacena objetos Bicicleta

    def registrar_bicicleta(self, bicicleta):
        self.bicicletas.append(bicicleta)

    def mostrar_bicicletas(self):
        for bici in self.bicicletas:
            print(bici)

    def reservar_bicicleta(self, id_bici, cliente):
        print("\nIntentando hacer una reserva...")
        
        try:
            bicicleta = None
            for b in self.bicicletas:
                if b.id_bici == id_bici:
                    bicicleta = b
                    break

            if bicicleta is None:
                raise ValueError("La bicicleta con ese ID no existe.")

            # Crear reserva
            reserva = Reserva(bicicleta, cliente)
            mensaje = reserva.confirmar()
            print(mensaje)

        except ValueError as e:
            print(f"Error: {e}")

        except ReservaInvalidaError as e:
            print(f"Error de reserva: {e}")

        except Exception as e:
            print(f"Error inesperado: {e}")

        finally:
            print("Registro: operación de reserva finalizada.\n")



# Crear sistema
sistema = SistemaReservas()

# Registrar bicicletas
sistema.registrar_bicicleta(Bicicleta(1))
sistema.registrar_bicicleta(Bicicleta(2))
sistema.registrar_bicicleta(Bicicleta(3, estado="mantenimiento"))

print("inventario actual:")
sistema.mostrar_bicicletas()

# Reservas
sistema.reservar_bicicleta(1, "Carlos") # Reserva válida
sistema.reservar_bicicleta(1, "Ana") # Error: ya reservada
sistema.reservar_bicicleta(3, "Luis") # Error: en mantenimiento
sistema.reservar_bicicleta(10, "Maria") # Error: no existe