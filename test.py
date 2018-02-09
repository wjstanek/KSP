import krpc, time

class MissionParameters(object):
    def __init__(self,
                 tgtOrbit = 200000,
                 grav_turn_finish = 80000,
                 force_roll = True,
                 roll = 90,
                 deploy_solar = False,
                 max_q = 30000):
        self.tgtOrbit = tgtOrbit
        self.grav_turn_finish = grav_turn_finish
        self.force_roll = force_roll
        self.roll = roll
        self.deploy_solar = deploy_solar
        self.max_q = max_q

# Initialize
vessel = conn.space_center.active_vessel
ap = vessel.auto_pilot
ap.sas = False
vessel.control.throttle = 0
vessel.control.rcs = False

listRCS = vessel.parts.rcs
listParts = vessel.parts.all
for part in listRCS:
    part.enabled = True

def main():
    conn = krpc.connect("test")
    launch_params = MissionParameters()
    ascent(conn,launch_params)

def ascent(conn, launch_params)
    conn = conn
    sc = conn.space_center
    v = sc.active_vessel

    v.auto_pilot.engage()
    v.auto_pilot.target_heading = 90
    if launch_params.force_roll:
        v.auto_pilot.target_roll=launch_params.roll
    v.control.throttle = 1.0
