configure_obs()
obs.sb.new(owner='Maciej Serylak')
obs.sb.description = 'TRAPUM session 5: 47 Tuc'
obs.sb.antenna_spec = 'available'
obs.sb.type = katuilib.ScheduleBlockTypes.OBSERVATION
obs.sb.controlled_resources_spec = 'cbf,sdp,apsuse,fbfuse'
obs.sb.instruction_set = "run-obs-script /home/kat/katsdpscripts/observation/track.py '47 Tuc,radec,00:24:05.67,-72:04:52.6' -t 14400 --fbfuse-config-auth-host='thn00.tuse.mkat.karoo.kat.ac.za:5003'"
obs.sb.desired_start_time = '2020-04-15 00:30:00'
obs.sb.proposal_id = 'SCI-20180923-MK-01'
obs.sb.to_defined()
obs.sb.to_approved()
obs.sb.unload()
