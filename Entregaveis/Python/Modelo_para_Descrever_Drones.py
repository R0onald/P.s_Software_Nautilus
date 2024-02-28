class Drone:
    def __init__(self, num_motores, num_cameras, ano_construcao, nome, atributo_extra):
        self.num_motores = num_motores
        self.num_cameras = num_cameras
        self.ano_construcao = ano_construcao
        self.nome = nome
        self.atributo_extra = atributo_extra
        self.lista_drones = []

    def exibir_todos(self):
        print("Lista de Drones:")
        print("{:<15} {:<10} {:<15} {:<10} {:<15} {:<15}".format('Nome', 'Motores', 'Câmeras', 'Ano', 'Atributo Extra', ''))
        for drone in self.lista_drones:
            print("{:<15} {:<10} {:<15} {:<10} {:<15}".format(drone.nome, drone.num_motores, drone.num_cameras, drone.ano_construcao, drone.atributo_extra))

    def exibir_individual(self, nome_drone):
        for drone in self.lista_drones:
            if drone.nome == nome_drone:
                print("Detalhes do Drone:")
                print("Nome:", drone.nome)
                print("Número de Motores:", drone.num_motores)
                print("Número de Câmeras:", drone.num_cameras)
                print("Ano de Construção:", drone.ano_construcao)
                print("Atributo Extra:", drone.atributo_extra)
                return
        print("Drone não encontrado.")

    def rankear_drones(self):
        print("Ranking dos Drones (do mais novo para o mais antigo):")
        sorted_drones = sorted(self.lista_drones, key=lambda x: x.ano_construcao, reverse=True)
        for idx, drone in enumerate(sorted_drones, start=1):
            print("{:<2} {:<15} {:<10} {:<15} {:<10} {:<15}".format(idx, drone.nome, drone.num_motores, drone.num_cameras, drone.ano_construcao, drone.atributo_extra))

    def outro_metodo(self):
        # Método de livre escolha para o modelo
        pass

# Exemplo de uso:
drone1 = Drone(4, 2, 2023, "Drone1", "Altitude Máxima")
drone2 = Drone(6, 3, 2021, "Drone2", "Tempo de Voo")
drone3 = Drone(8, 4, 2022, "Drone3", "Carga Útil")

drone1.lista_drones.extend([drone2, drone3])

drone1.exibir_todos()
print()
drone1.exibir_individual("Drone2")
print()
drone1.rankear_drones()

