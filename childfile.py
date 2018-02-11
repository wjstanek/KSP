

def main():
    from multiprocessing import Process, Pipe
    from test import sendv, pos
    import time
    import numpy as np

    start = pos()  # calls test.py pos() to get start position once
    # print('Start: ' +str(start))
    parent_conn, child_conn = Pipe()
    p = Process(target=sendv, args=(child_conn,)).start()
    pos = parent_conn.recv()
    # print('Current: ' +str(pos))

    i = True
    while i:
        p = Process(target=sendv, args=(child_conn,)).start()
        pos = parent_conn.recv()
        print('Start: ' + str(round(start[0], 1)) + ' ' + str(round(start[1], 1)))
        print('Curr:  ' + str(round(pos[0], 1)) + ' ' + str(round(pos[1], 1)))
        # haversine formula https://www.movable-type.co.uk/scripts/latlong.html
        radius = 6371000
        phi1 = start[0] * 3.14159 / 180
        phi2 = pos[0] * 3.14159 / 180
        dphi = (phi2 - phi1)
        dlambda = (pos[1] - start[1]) * 3.14159 / 180
        a = np.sin(dphi / 2) * np.sin(dphi / 2) + np.cos(phi1) * np.cos(phi2) * np.sin(dlambda / 2) * np.sin(
            dlambda / 2)
        c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))
        dist = radius * c / 1852

        # dist = round( ((pos[0]-start[0])**2 +(pos[1]-start[1])**2)**(.5)*60,3 )
        print('Dist:  ' + str(round(dist, 1)))
        time.sleep(1)
    return(dist)


if __name__ == '__main__':
    main()