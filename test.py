import krpc, time, os, childfile
from multiprocessing import Process, Pipe

class MissionParameters(object):
    def __init__(self,
                 tgtOrbit = 200000,
                 grav_turn_finish = 80000,
                 force_roll = True,
                 roll = 0,
                 deploy_solar = False,
                 max_q = 30000):
        self.tgtOrbit = tgtOrbit
        self.grav_turn_finish = grav_turn_finish
        self.force_roll = force_roll
        self.roll = roll
        self.deploy_solar = deploy_solar
        self.max_q = max_q

def main():
    print('Main Program')
    conn = krpc.connect("test")
    launch_params = MissionParameters()
    #launch_params.tgtOrbit = input('Target Orbit: ')
    sc = conn.space_center
    v = sc.active_vessel
    ## DEBUG INTERRUPT
    #while True:
    #    time.sleep(0.1)
    #print(childfile.main())
    launch(conn, v, launch_params)
    grav_turn(v, launch_params)
    #ascent(conn,launch_params)

def launch(conn, v, launch_params):
    print('Launch Program')
    v.auto_pilot.engage()
    v.auto_pilot.target_roll = 90
    v.auto_pilot.target_pitch_and_heading(90,90)
    v.control.throttle = 1

    # Launch Sequence
    i = True
    v.control.activate_next_stage()

    while v.thrust < 0.99*v.available_thrust:
        time.sleep(0.1)

    v.control.activate_next_stage()
    flight = v.flight()

    while flight.surface_altitude < 100:
        #print(round(flight.surface_altitude,0))
        time.sleep(0.1)
    print('Tower clear, Roll Program')
    if launch_params.force_roll:
        v.auto_pilot.target_roll = launch_params.roll
        v.auto_pilot.wait()


    # Pitch Maneuver
    while flight.surface_altitude < 500:
        time.sleep(0.2)

def grav_turn(v, launch_params):
    print('Gravity Turn')
    i = True
    tgtPitch = 90
    while i:
        autostage(v)
        if tgtPitch == 30:
            tgtPitch = max(5,90*(1-(v.orbit.apoapsis_altitude)/140000))
        if tgtPitch > 30:
            tgtPitch = max(30,90*(1-(v.orbit.apoapsis_altitude)/120000))
        v.auto_pilot.target_pitch = tgtPitch
        #print(round(v.auto_pilot.target_pitch,1))
        if v.orbit.apoapsis_altitude > launch_params.tgtOrbit:
            v.control.throttle = 0
            i = False
        time.sleep(0.1)

def pos():
    conn = krpc.connect("test")
    sc = conn.space_center
    v = sc.active_vessel
    flight = v.flight()
    pos = []
    pos.append(flight.latitude)
    pos.append(flight.longitude)
    return pos

def sendv(child_conn):
    conn = krpc.connect("test")
    sc = conn.space_center
    v = sc.active_vessel
    flight = v.flight()
    pos = []
    pos.append(flight.latitude)
    pos.append(flight.longitude)
    child_conn.send(pos)
    child_conn.close()

def sendalt(child_conn):
    conn = krpc.connect("test")
    sc = conn.space_center
    v = sc.active_vessel
    flight = v.flight()
    alt = flight.mean_altitude
    child_conn.send(alt)
    child_conn.close()

def autostage(v):
    res = v.resources_in_decouple_stage(v.control.current_stage-1,cumulative=False)
    fuel = 'Kerosene'
    if res.max(fuel) > 0 and res.amount(fuel) == 0:
        print('Staging: ' + str(v.control.current_stage))
        print('Fuel Max: ' + str(round(res.max(fuel),0)) + ' Remaining: ' + str(round(res.amount(fuel),0)))
        v.control.activate_next_stage()

def ascent(conn, launch_params):
    sc = conn.space_center
    v = sc.active_vessel

    v.auto_pilot.engage()
    v.auto_pilot.target_heading = 90

    v.control.throttle = 1.0

if __name__ == "__main__":
    main()
    print('Complete')