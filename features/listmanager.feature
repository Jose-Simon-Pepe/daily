# -- FILE: features/example.feature
# lang = es
Feature: list manager 

  Scenario: Usuario consulta lista existente
    Given que el sistema tiene al menos una lista
    When el usuario pida ver una
    Then el sistema debe mostrarsela

  Scenario: Usuario quiere que el sistema muestre lista de actividades comunes apenas inicia el pc
    Given que el usuario indico que quiere que el sistema muestre lista de actividades comunes al bootear
    When el pc esta iniciado
    Then el sistema debe mostrar una lista de actividades comunes

  Scenario: Usuario quiere que el sistema muestre lista de actividades comunes al iniciar la app
    Given que el usuario indico que quiere que el sistema muestre lista de actividades comunes al iniciar app
    When inice la app
    Then el sistema debe mostrar una lista de actividades comunes

 
  Scenario: Usuario consulta lista que no existe
    Given que lista x no existe
    When el usuario pida ver x
    Then el sistema debe avisarle que x no existe
  
  Scenario: Usuario quiere modificar una lista
    Given que lista x existe
    When el usuario pida modificar una lista x
    Then el sistema deberia mostrarle un entorno para modificar x

  Scenario: Usuario quiere acceder a una lista que modifico previamente
    Given que usuario modifico x
    When el usuario pida ver x
    Then el sistema deberia mostrar x tal como el usuario la dejo

  Scenario: Usuario quiere que el sistema este iniciado desde el arranque del pc
    Given que usuario ha indicado que quiere que la app inicie cuando bootea
    When el usuario inicie sesion
    Then el sistema deberia estar listo para recibir peticiones
