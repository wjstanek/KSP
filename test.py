import krpc
conn = krpc.connect("test")

vessel = conn.space_center.active_vessel

control = vessel.control
control.sas = False
control.rcs = False
control.lights = True

launch = True
while launch:
    ap = vessel.auto_pilot
    ap.target_pitch = 90
    ap.target_heading = 90
    ap.target_roll = 90
    ap.engage()
    control.activate_next_stage()


#ap.sas_mode = conn.space_center.SASMode.retrograde



#for panels in vessel.parts.solar_panels:
#sw   panels.deployed = True