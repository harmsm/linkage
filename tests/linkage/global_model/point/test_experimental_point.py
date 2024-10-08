
from linkage.global_model.point.experimental_point import ExperimentalPoint

import numpy as np

def test_ExperimentalPoint():

    # Test properties and basic setter/getter
    idx = 0
    expt_idx = 1
    obs_key = "test"
    micro_array = np.ones(10)
    macro_array = np.ones(3)
    del_macro_array = np.zeros(3)
    total_volume = 200e-6
    injection_volume = 1e-6
    e = ExperimentalPoint(idx=idx,
                          expt_idx=expt_idx,
                          obs_key=obs_key,
                          micro_array=micro_array,
                          macro_array=macro_array,
                          del_macro_array=del_macro_array,
                          total_volume=total_volume,
                          injection_volume=injection_volume)
    
    assert e.idx == 0
    assert e.expt_idx == 1
    assert e.obs_key == "test"

    assert e._micro_array is micro_array
    assert e._macro_array is macro_array
    assert e._del_macro_array is del_macro_array
    
    assert e._total_volume == total_volume
    assert e._injection_volume == injection_volume

    