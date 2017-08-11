u1={"a":"1","b":"2"}
u2=[{"c":"2","q":"sad"},{"c":"2","qwq":"dsa"},{"c":"4","sdada":"sdda"},{"c":"2","adsd":"dasda"}]
for u in u2:
	if u1.get("b")==u.get("c"):
		print(u)
		break