configure_obs()
obs.sb.new(owner='Maciej Serylak')
obs.sb.description='TRAPUM session <NUMBER>: <TARGET>'
obs.sb.antenna='available'
obs.sb.controlled_resources_spec='cbf,sdp,apsuse,fbfuse,tuse'
obs.sb.instruction_set="run-obs-script /home/kat/katsdpscripts/observation/track.py '<TARGET>,radec,<HH:MM:SS.SS>,<DD:MM:SS.SS>' -t <T_OBS> --fbfuse-config-auth-host='thn00.tuse.mkat.karoo.kat.ac.za:5003'"
obs.sb.desired_start_time='YYYY-MM-DD HH:MM:SS'
obs.sb.proposal='SCI-20180923-MK-01'
obs.sb.to_defined()
obs.sb.to_approved()
obs.sb.unload()
