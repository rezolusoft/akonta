import uuid

def id_generator()->uuid:

    """Genere un identifiant universel unique"""

    return uuid.uuid4()


def product_code_generator()->str:

    """Genere un code unique pour un objet produit"""

    rand_code = id_generator().hex[:5]
    return f"PROD-{rand_code.upper()}"


def category_code_generator()->str:

    """Genere un code unique pour un objet category"""
    rand_code = id_generator().hex[:5]
    return f"CAT-{rand_code.upper()}"


def sale_code_generator()->str:

    """Genere un code unique pour un objet vente"""
    rand_code = id_generator().hex[:5]
    return f"SALE-{rand_code.upper()}"

def invoice_code_generator()->str:

    """Genere un code unique pour un objet vente"""
    rand_code = id_generator().hex[:5]
    return f"INVOICE-{rand_code.upper()}"
