configure_obs()
obs.sb.new(owner='Maciej Serylak')
obs.sb.description='TRAPUM session 3: Ter 5'
obs.sb.antenna='available'
obs.sb.controlled_resources_spec='cbf,sdp,apsuse,fbfuse'
obs.sb.instruction_set="run-obs-script /home/kat/katsdpscripts/observation/track.py 'Ter 5,radec,17:48:04.80,-24:46:45' -t 14400 --fbfuse-config-auth-host='thn00.tuse.mkat.karoo.kat.ac.za:5003'"
obs.sb.desired_start_time='2020-04-10 01:00:00'
obs.sb.proposal='SCI-20180923-MK-01'
obs.sb.to_defined()
obs.sb.to_approved()
obs.sb.unload()
