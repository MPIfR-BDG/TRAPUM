configure_obs()
obs.sb.new(owner='Maciej Serylak')
obs.sb.description = 'TRAPUM session <NUMBER>: <TARGET>'
obs.sb.antenna_spec = 'available'
obs.sb.type = katuilib.ScheduleBlockTypes.OBSERVATION
obs.sb.controlled_resources_spec = 'cbf,sdp,apsuse,fbfuse,tuse'  # delete where necessary
obs.sb.instruction_set = "run-obs-script /home/kat/katsdpscripts/observation/track.py '<TARGET>,radec,<HH:MM:SS.SS>,<DD:MM:SS.SS>' -t <T_IBS> --fbfuse-config-auth host='thn00.tuse.mkat.karoo.kat.ac.za:5003'"
obs.sb.desired_start_time = 'YYYY-MM-DD HH:MM:SS'
obs.sb.proposal_id = 'SCI-20180923-MK-01'
obs.sb.to_defined()
obs.sb.to_approved()
obs.sb.unload()
