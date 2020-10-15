create_category(conn, 'Party')
create_category(conn, 'Card Game')
create_category(conn, 'Dice')
create_category(conn, 'Puzzle')
create_category(conn, 'Strategy')
create_category(conn, 'Bluffing')
create_category(conn, 'Action / Dexterity')


create_boardgame(conn, 'Jungle Speed')
create_boardgame(conn, 'Forbidden Sky')
create_boardgame(conn, 'Sagrada')
create_boardgame(conn, 'UNO')
create_boardgame(conn, 'Coup')
create_boardgame(conn, 'Explodding Kittens')

assign_category_to_boardgame(conn, 'Party', 'Jungle Speed')
assign_category_to_boardgame(conn, 'Party', 'UNO')
assign_category_to_boardgame(conn, 'Party', 'Explodding Kittens')
assign_category_to_boardgame(conn, 'Dice', 'Sagrada')
assign_category_to_boardgame(conn, 'Puzzle', 'Sagrada')
assign_category_to_boardgame(conn, 'Strategy', 'Forbidden Sky')
assign_category_to_boardgame(conn, 'Bluffing', 'Coup')

