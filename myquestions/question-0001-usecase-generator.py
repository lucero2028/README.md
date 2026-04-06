i, o = generar_caso_de_uso_pipeline_churn_clientes()

print('---- inputs ----')
for k, v in i.items():
    print("\n", k, ":\n", v)

print('\n---- expected output ----\n', o)
