class EcephysApi(object):


    def __init__(self, *args, **kwargs):
        super(EcephysApi, self).__init__(*args, **kwargs)

    
    def get_session_table(self, session_ids=None):
        raise NotImplementedError()


    def get_probe_table(self, session_ids=None):
        raise NotImplementedError()


    def get_stimulus_table(self, session_id):
        raise NotImplementedError()


    def get_channel_table(self, session_id, probe_ids=None):
        raise NotImplementedError()


    def get_unit_table(self, session_id, probe_ids=None):
        raise NotImplementedError()


    def get_unit_waveforms(self, session_id, probe_id):
        raise NotImplementedError()


    def get_event_timestamps(self, session_id, probe_id):
        raise NotImplementedError()


    def get_lfp(self, session_id, probe_id):
        raise NotImplementedError()


    def get_lfp_timestamps(self, session_id, probe_id):
        raise NotImplementedError()


    def get_current_source_density(self, session_id, probe_id):
        raise NotImplementedError()


    def get_current_source_density_timestamps(self, session_id, probe_id):
        raise NotImplementedError()