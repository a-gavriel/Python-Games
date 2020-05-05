from random import choice


cartas = {
"1" : "+ 1 gems",
"2" : "+ 2 gems",
"3" : "+ 3 gems",
"4" : "+ 4 gems",
"5" : "+ 5 gems",
"6" : "+ 5 gems",
"7" : "+ 7 gems",
"8" : "+ 7 gems",
"9" : "+ 9 gems",
"10" : "+ 11 gems",
"11" : "+ 11 gems",
"12" : "+ 13 gems",
"13" : "+ 14 gems",
"14" : "+ 15 gems",
"15" : "+ 17 gems",
"16" : "Serpents",
"17" : "Serpents",
"18" : "Serpents",
"19" : "Spiders",
"20" : "Spiders",
"21" : "Spiders",
"22" : "Boulders",
"23" : "Boulders",
"24" : "Boulders",
"25" : "Lava",
"26" : "Lava",
"27" : "Lava",
"28" : "Spikes",
"29" : "Spikes",
"30" : "Spikes",
"31" : "Treasure 1",
"32" : "Treasure 2",
"33" : "Treasure 3",
"34" : "Treasure 4",
"35" : "Treasure 5"
}

values = []
traps_out = []
traps_round = [0,0,0,0,0]
treasure_out = []

def newgame():
	global values, traps_out, traps_round
	traps_out = []
	traps_round = [0,0,0,0,0]
	values = []
	treasure_out = []


def newround():
	global values, traps_out , traps_round
	traps_round = [0,0,0,0,0]
	values = []
	for x in range(35):
		if ((x+1) not in traps_out) and ((x+1) not in treasure_out):
			values.append(x+1)


def verify_trap(id):
	r_value = 0
	if 15<id<31:
		traps_out.append(id)
		if ((id==16) or (id==17) or (id==18)):
			if (traps_round[0]):
				r_value = 1
			traps_round[0] = 1
		elif ((id==19) or (id==20) or (id==21)):			
			if (traps_round[1]):
				r_value = 1
			traps_round[1] = 1
		elif ((id==22) or (id==23) or (id==24)):			
			if (traps_round[2]):
				r_value = 1
			traps_round[2] = 1
		elif ((id==25) or (id==26) or (id==27)):			
			if (traps_round[3]):
				r_value = 1
			traps_round[3] = 1
		elif ((id==28) or (id==29) or (id==30)):			
			if (traps_round[4]):
				r_value = 1
			traps_round[4] = 1			
	return r_value


def verify_treasure(id):
	global treasure_out
	r_value = 0
	if id>30:
		r_value = 1
		treasure_out.append(id)
	return r_value



def play():
	global values , traps_round, traps_out, treasure_out
	newran = choice(values)
	values.remove(newran)
	lost = verify_trap(newran)
	verify_treasure(newran)
	print( cartas[str(newran)]  )
	if (lost):
		print ("Lost Round!")
