configure_obs()
obs.sb.new(owner='Maciej Serylak')
obs.sb.description = 'TRAPUM session 6: NGC 6624'
obs.sb.antenna_spec = 'available'
obs.sb.type = katuilib.ScheduleBlockTypes.OBSERVATION
obs.sb.controlled_resources_spec = 'cbf,sdp,apsuse,fbfuse,tuse'
obs.sb.instruction_set = "run-obs-script /home/kat/katsdpscripts/observation/track.py 'NGC 6624,radec,18:23:40.510,-30:21:39.700' -t 14400 --fbfuse-config-auth-host='thn00.tuse.mkat.karoo.kat.ac.za:5003'"
obs.sb.desired_start_time = '2020-05-21 00:00:00'
obs.sb.proposal_id = 'SCI-20180923-MK-01'
obs.sb.to_defined()
obs.sb.to_approved()
obs.sb.unload()

# Delay calibration: 
# Phase up: 
# Imaging data: 
# Comments:
# -  antennas used,
