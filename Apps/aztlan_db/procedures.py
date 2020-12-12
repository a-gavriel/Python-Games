from datetime import timedelta, datetime

#now_datetime = strftime("%Y-%m-%d %H:%M:%S")
#default_delta = timedelta(days=1)
#datetime.fromisoformat( XXX ) 


def create_provincia(conn, provincia, pais):
    """
    Crea nueva pronvincia
    :param conn:
    :param pronvincia:
    :param pais:
    
    """

    
    #sql = ''' INSERT INTO Provincia(Name, fkPais)
    #          VALUES (?,?) '''

    sql = ''' INSERT into Provincia (Name, fkPais) values (?, 
        (select idPais from Pais where Pais.Name = ? limit 1)) '''
    cur = conn.cursor()
    cur.execute(sql, provincia, pais)
    conn.commit()
    return cur.lastrowid


def create_canton(conn, canton, provincia, pais):
    """
  
    """
    sql = ''' INSERT into Canton (Name, fkprovincia) values (?, 
    (select idProvincia from Provincia where Provincia.Name = ? and Provincia.fkPais = 
        (select idPais from Pais where Pais.Name = ? limit 1) 
    limit 1)) '''
    cur = conn.cursor()
    cur.execute(sql, canton, provincia, pais)
    conn.commit()
    return cur.lastrowid

def create_distrito(conn, distrito, canton, provincia, pais, postal_code = 0):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """    
    sql = ''' INSERT into Distrito(Name, fkCanton, postal_code) values (?,
    (select idCanton from Canton where Canton.Name = ? and Canton.fkProvincia = 
        (select idProvincia from Provincia where Provincia.Name = ? and Provincia.fkPais = 
            (select idPais from Pais where Pais.Name = ? limit 1) 
        limit 1)
    limit 1), ? )'''
    cur = conn.cursor()
    cur.execute(sql, (distrito, canton, provincia, pais))
    conn.commit()
    return cur.lastrowid

def create_category(conn, category):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """    
    sql = ''' INSERT into Category(Name) values (?)'''
    cur = conn.cursor()
    cur.execute(sql, (category,))
    conn.commit()
    return cur.lastrowid

def create_boardgame(conn, boardgame_title, 
    bg_description = "", bg_original_price = -1, bg_current_price = -1, base_game = 0, Standalone = 1):
    sql = ''' INSERT into Boardgame(Title, Description, OriginalPrice, CurrentPrice, BaseGame, Standalone) values (?, ?, ?, ?, ?, ?)'''
    cur = conn.cursor()
    cur.execute(sql, (boardgame_title, bg_description, bg_original_price, bg_current_price, base_game, Standalone ))
    conn.commit()
    return cur.lastrowid


def assign_category_to_boardgame(conn, category, boardgame ):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """    
    sql = ''' INSERT into Category_Boardgame(fkCategory, fkBoardgame) values (
        (SELECT idCategory from Category where Name = ? limit 1),
        (SELECT idBoardgame from Boardgame where Name = ? limit 1)
    )'''
    cur = conn.cursor()
    cur.execute(sql, (category, boardgame))
    conn.commit()
    return cur.lastrowid


def create_direction(conn, direccion, distrito, canton, provincia, pais):
    sql = ''' INSERT into Direccion (Descripcion, fkDistrito) values (?,
    (select idDistrito from Distrito where Distrito.Name = ? and Distrito.fkCanton =
        (select idCanton from Canton where Canton.Name = ? and Canton.fkProvincia = 
            (select idProvincia from Provincia where Provincia.Name = ? and Provincia.fkPais = 
                (select idPais from Pais where Pais.Name = ? limit 1) 
            limit 1)
        limit 1)
    limit 1)
    ) '''


    cur = conn.cursor()
    cur.execute(sql, (direccion, distrito, canton, provincia, pais))
    conn.commit()
    return cur.lastrowid


def create_customer(conn, name, lastname, email, distrito, canton, provincia, pais, id_ = "", phone1 = 0, direccion = "" ):

    sql_dir = ''' INSERT into Customer (Name, Lastname, email, fkDistrito, Identification, 
        Phone1, Direccion) values (?, ?, ?, 
    (select idDistrito from Distrito where Distrito.Name = ? and Distrito.fkCanton =
        (select idCanton from Canton where Canton.Name = ? and Canton.fkProvincia = 
            (select idProvincia from Provincia where Provincia.Name = ? and Provincia.fkPais = 
                (select idPais from Pais where Pais.Name = ? limit 1) 
            limit 1)
        limit 1)
    limit 1), ?, ?, ?
    ) '''
    cur = conn.cursor()
    cur.execute(sql_dir, (name, lastname, email, distrito, canton, provincia, pais, id_, phone1, direccion))
    conn.commit()
    return cur.lastrowid




#create_local

def create_item(conn, board_game, description = ""):
    sql_dir = ''' INSERT into Item (fkBoardgame, Description) values (
        (SELECT idBoardgame from Boardgame where Name = ? limit 1), ?)'''
    cur = conn.cursor()
    cur.execute(sql_dir, (board_game, description))
    conn.commit()
    return cur.lastrowid


#def list_items()

def create_rental(conn, idCustomer, price = 0, amount_paid = 0, paid_method = "" , local_store = 1, rental_date = None, expected_date = None, return_date = None , description = "" ):   
    if rental_date is None:
        rental_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if expected_date is None:
        default_delta = timedelta(days=1)
        expected_date = (datetime.fromisoformat( rental_date ) + default_delta ).strftime("%Y-%m-%d %H:%M:%S")

    sql_dir = ''' INSERT into Rental ( Rental_date, Expected_date, Returned_date, fkLocalStore, fkCustomer, Price, Paid, Payment_method, Description ) values (
        (idCustomer, ?)'''
    cur = conn.cursor()
    cur.execute(sql_dir, (board_game, description))
    conn.commit()
    return cur.lastrowid



#assign item_to_rental

