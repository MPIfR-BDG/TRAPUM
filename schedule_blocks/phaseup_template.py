configure_obs()
obs.sb.new(owner='Operator')
obs.sb.type = katuilib.ScheduleBlockTypes.OBSERVATION
obs.sb.controlled_resources_spec = 'cbf,sdp'
obs.sb.description = 'TRAPUM phase up with flatten bandpass'
obs.sb.instruction_set = "run-obs-script /home/kat/katsdpscripts/observation/bf_phaseup.py '/home/kat/katsdpcatalogues/three_calib.csv' --max-gap-MHz=128 -t 256 --flatten-bandpass"
obs.sb.proposal_id = 'SCI-20180923-MK-99'
obs.sb.desired_start_time = 'YYYY-MM-DD HH:MM'
obs.sb.to_defined()
obs.sb.to_approved()
obs.sb.unload()
