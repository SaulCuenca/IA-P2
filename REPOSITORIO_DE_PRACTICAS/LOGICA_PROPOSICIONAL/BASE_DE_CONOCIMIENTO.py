from pyke import knowledge_engine

engine = knowledge_engine.engine(__file__)

# Definir una base de conocimientos
engine.produce_plan('bc', 'assert_fact', (engine.knowledge_base, 'p'))
engine.produce_plan('bc', 'assert_fact', (engine.knowledge_base, 'q'))

engine.produce_plan('bc', 'assert_fact', (engine.knowledge_base, 'r'))
engine.produce_plan('bc', 'assert_fact', (engine.knowledge_base, 's'))

engine.produce_plan('bc', 'add_rule',
                    (engine.knowledge_base, 'expresion1', 'p & q => r'))

engine.produce_plan('bc', 'add_rule',
                    (engine.knowledge_base, 'expresion2', 'p & q => s'))

# Evaluar expresiones lógicas
def evaluar_expresion(expresion):
    try:
        engine.produce_plan('bc', 'add_goal', (engine.knowledge_base, 'resultado', expresion))
        engine.run()
        return engine.get_kb('bc').goal[0].as_str()
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    expresion = input("Ingrese una expresión lógica: ")
    resultado = evaluar_expresion(expresion)
    print(f"Resultado de la expresión: {resultado}")
