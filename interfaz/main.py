from src.view.view import App_View          # Vista
from src.model.model import cuestionario  # Modelo
from src.controller.controller import Cuestionario_Controller  # Controlador


def main():
    # Instanciar modelo y vista
    modelo = cuestionario()
    vista = App_View()

    # Crear el controlador y conectar las capas
    controlador = Cuestionario_Controller(vista, modelo)

    # Iniciar la interfaz
    vista.mainloop()


if __name__ == "__main__":
    main()
