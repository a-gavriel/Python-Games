
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
    cur.execute(sql, distrito, canton, provincia, pais)
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
    cur.execute(sql, category)
    conn.commit()
    return cur.lastrowid

def create_boardgame(conn, boardgame_title, 
    bg_description = "", bg_original_price = -1, bg_current_price = -1):
    sql = ''' INSERT into Boardgame(Title, Description, OriginalPrice, CurrentPrice) values (?, ?, ?, ?)'''
    cur = conn.cursor()
    cur.execute(sql, boardgame_title, bg_description, bg_original_price, bg_current_price)
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
    cur.execute(sql, category, boardgame)
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
    cur.execute(sql, direccion, distrito, canton, provincia, pais)
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
    cur.execute(sql_dir, name, lastname, email, distrito, canton, provincia, pais, id_, phone1, direccion)
    conn.commit()
    return cur.lastrowid



def create_customer_no_dir(conn, name, lastname, email, id_ = "", fkDistrito = 0, phone1 = 0):
    sql = ''' INSERT into 
    Customer (Name, Lastname, Email1, Identification, fkDistrito, Phone1) values (?,?,?,?,?,?)
    '''


#create_local

#create_item

#create_rental

#assign item_to_rental

