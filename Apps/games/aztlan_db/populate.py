
def create_provincia(conn, project):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = ''' INSERT INTO Provincia(Name, fkPais)
              VALUES (?,?) '''
    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()
    return cur.lastrowid


def create_canton(conn, canton, provincia):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = ''' INSERT INTO Provincia(Name, fkPais)
              VALUES (?,?) '''
    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()
    return cur.lastrowid

def create_distrito(conn, distrito, canton, provincia):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """    
    sql = ''' INSERT INTO Provincia(Name, fkPais)
              VALUES (?,?) '''
    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()
    return cur.lastrowid