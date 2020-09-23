
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

def create_distrito(conn, distrito, canton, provincia, pais):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """    
    sql = ''' INSERT into Distrito(Name, fkCanton) values (?,
    (select idCanton from Canton where Canton.Name = ? and Canton.fkProvincia = 
        (select idProvincia from Provincia where Provincia.Name = ? and Provincia.fkPais = 
            (select idPais from Pais where Pais.Name = ? limit 1) 
        limit 1)
    limit 1))'''
    cur = conn.cursor()
    cur.execute(sql, distrito, canton, provincia, pais)
    conn.commit()
    return cur.lastrowid

