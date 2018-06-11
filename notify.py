import notify2

def put_top(m,o):
	notify2.init(m)
	n = notify2.Notification(m,o)
	n.show()
