# -- FILE: features/example.feature
# lang = es
Feature:list manager 

  Escenario: Usuario consulta lista existente
    Dado que el sistema tiene al menos una lista
    Cuando el usuario pida ver una
    Entonces el sistema debe mostrarsela

  Escenario: Usuario quiere que el sistema muestre lista de actividades comunes apenas inicia el pc
    Dado que el usuario indico que quiere que el sistema muestre lista de actividades comunes al bootear
    Cuando el pc esta iniciado
    Entonces el sistema debe mostrar una lista de actividades comunes

  Escenario: Usuario quiere que el sistema muestre lista de actividades comunes al iniciar la app
    Dado que el usuario indico que quiere que el sistema muestre lista de actividades comunes al iniciar app
    Cuando inice la app
    Entonces el sistema debe mostrar una lista de actividades comunes

 
  Escenario: Usuario consulta lista que no existe
    Dado que lista x no existe
    Cuando el usuario pida ver x
    Entonces el sistema debe avisarle que x no existe
  
  Escenario: Usuario quiere modificar una lista
    Dado que lista x existe
    Cuando el usuario pida modificar una lista x
    Entonces el sistema deberia mostrarle un entorno para modificar x

  Escenario: Usuario quiere acceder a una lista que modifico previamente
    Dado que usuario modifico x
    Cuando el usuario pida ver x
    Entonces el sistema deberia mostrar x tal como el usuario la dejo

  Escenario: Usuario quiere que el sistema este iniciado desde el arranque del pc
    Dado que usuario ha indicado que quiere que la app inicie cuando bootea
    Cuando el usuario inicie sesion
    Entonces el sistema deberia estar listo para recibir peticiones
