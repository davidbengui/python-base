email_tmp = """
Ola, %(nome)s
Temos uma promoçao de %(produto)s
Existem poucas %(quantidade)d
Se lhe interessar clica no %(link)s

"""

clientes = ["David",  "Jose", "Bengui"]
for cliente in clientes:
    print ( email_tmp
        % { 
            "nome": "cliente",
            "produto": "produto",
            "quantidade": 1,
            "link": "www.dbengui.com",
    }
    )





    