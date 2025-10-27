#Listing pineapple routes

def main():
    portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]
    port1 = 0
    for port2 in range(5):
        for port3 in range(5):
            for port4 in range(5):
                for port5 in range(5):
                    routes = [port1,port2,port3,port4,port5]
                    if set(routes) == {0,1,2,3,4}:
                        print(' '.join(portnames[i] for i in routes))
main()